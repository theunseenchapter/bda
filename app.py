"""
Friend Recommendation System using Supabase (PostgreSQL)
Flask Web Application
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
from datetime import datetime
from supabase import create_client, Client
from collections import defaultdict
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL', 'your-supabase-url')
SUPABASE_KEY = os.getenv('SUPABASE_KEY', 'your-supabase-anon-key')

# Initialize Supabase client
supabase: Client = None

def get_supabase_client():
    global supabase
    if supabase is None:
        try:
            # Create client with only URL and key (no additional options for v2.3.0)
            supabase = create_client(
                supabase_url=SUPABASE_URL,
                supabase_key=SUPABASE_KEY
            )
        except Exception as e:
            print(f"Error connecting to Supabase: {e}")
            return None
    return supabase

# Database Operations
def clear_database():
    """Clear all data from tables"""
    client = get_supabase_client()
    if client:
        try:
            client.table('friendships').delete().neq('id', 0).execute()
            client.table('users').delete().neq('id', 0).execute()
            return True
        except Exception as e:
            print(f"Error clearing database: {e}")
            return False
    return False

def load_data_from_csv(filepath):
    """Load social network data from CSV into Supabase"""
    client = get_supabase_client()
    if not client:
        return False, "Could not connect to Supabase"
    
    try:
        # Clear existing data
        clear_database()
        
        # Read CSV and collect unique users
        users = set()
        friendships = []
        
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header if exists
            
            for row in reader:
                if len(row) >= 2:
                    user1, user2 = row[0].strip(), row[1].strip()
                    if user1 and user2:
                        users.add(user1)
                        users.add(user2)
                        friendships.append((user1, user2))
        
        # Insert users
        user_data = [{'name': user} for user in users]
        client.table('users').insert(user_data).execute()
        
        # Get user IDs
        users_result = client.table('users').select('*').execute()
        user_id_map = {user['name']: user['id'] for user in users_result.data}
        
        # Insert friendships (both directions for undirected graph)
        friendship_data = []
        added_pairs = set()
        
        for user1, user2 in friendships:
            user1_id = user_id_map.get(user1)
            user2_id = user_id_map.get(user2)
            
            if user1_id and user2_id:
                # Add both directions
                pair_key = tuple(sorted([user1_id, user2_id]))
                if pair_key not in added_pairs:
                    friendship_data.append({
                        'user1_id': user1_id,
                        'user2_id': user2_id
                    })
                    friendship_data.append({
                        'user1_id': user2_id,
                        'user2_id': user1_id
                    })
                    added_pairs.add(pair_key)
        
        # Batch insert friendships
        if friendship_data:
            client.table('friendships').insert(friendship_data).execute()
        
        return True, f"Successfully loaded {len(users)} users and {len(added_pairs)} connections"
    except Exception as e:
        return False, f"Error loading data: {str(e)}"

def get_friend_recommendations(user_name, limit=10):
    """Get friend recommendations based on mutual friends"""
    client = get_supabase_client()
    if not client:
        return []
    
    try:
        # Get user ID
        user_result = client.table('users').select('id').eq('name', user_name).execute()
        if not user_result.data:
            return []
        
        user_id = user_result.data[0]['id']
        
        # Get user's direct friends
        friends_result = client.table('friendships').select('user2_id').eq('user1_id', user_id).execute()
        friend_ids = [f['user2_id'] for f in friends_result.data]
        
        if not friend_ids:
            return []
        
        # Get friends of friends
        foaf_result = client.table('friendships').select('user2_id').in_('user1_id', friend_ids).execute()
        
        # Count mutual friends
        mutual_count = defaultdict(int)
        for foaf in foaf_result.data:
            foaf_id = foaf['user2_id']
            if foaf_id != user_id and foaf_id not in friend_ids:
                mutual_count[foaf_id] += 1
        
        # Get user names for recommendations
        recommendations = []
        for foaf_id, count in sorted(mutual_count.items(), key=lambda x: x[1], reverse=True)[:limit]:
            user_data = client.table('users').select('name').eq('id', foaf_id).execute()
            if user_data.data:
                recommendations.append({
                    'recommended_friend': user_data.data[0]['name'],
                    'mutual_friends': count
                })
        
        return recommendations
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return []

def get_mutual_friends(user1_name, user2_name):
    """Get mutual friends between two users"""
    client = get_supabase_client()
    if not client:
        return []
    
    try:
        # Get user IDs
        user1_result = client.table('users').select('id').eq('name', user1_name).execute()
        user2_result = client.table('users').select('id').eq('name', user2_name).execute()
        
        if not user1_result.data or not user2_result.data:
            return []
        
        user1_id = user1_result.data[0]['id']
        user2_id = user2_result.data[0]['id']
        
        # Get friends of both users
        friends1 = client.table('friendships').select('user2_id').eq('user1_id', user1_id).execute()
        friends2 = client.table('friendships').select('user2_id').eq('user1_id', user2_id).execute()
        
        friend1_ids = set(f['user2_id'] for f in friends1.data)
        friend2_ids = set(f['user2_id'] for f in friends2.data)
        
        # Find intersection
        mutual_ids = friend1_ids & friend2_ids
        
        # Get names
        mutual_friends = []
        for mutual_id in mutual_ids:
            user_data = client.table('users').select('name').eq('id', mutual_id).execute()
            if user_data.data:
                mutual_friends.append({'mutual_friend': user_data.data[0]['name']})
        
        return sorted(mutual_friends, key=lambda x: x['mutual_friend'])
    except Exception as e:
        print(f"Error getting mutual friends: {e}")
        return []

def get_influencers(limit=10):
    """Get most connected users (influencers)"""
    client = get_supabase_client()
    if not client:
        return []
    
    try:
        # Count connections per user
        friendships = client.table('friendships').select('user1_id').execute()
        
        connection_count = defaultdict(int)
        for f in friendships.data:
            connection_count[f['user1_id']] += 1
        
        # Get top users
        top_users = sorted(connection_count.items(), key=lambda x: x[1], reverse=True)[:limit]
        
        # Get user names
        influencers = []
        for user_id, count in top_users:
            user_data = client.table('users').select('name').eq('id', user_id).execute()
            if user_data.data:
                influencers.append({
                    'name': user_data.data[0]['name'],
                    'connections': count
                })
        
        return influencers
    except Exception as e:
        print(f"Error getting influencers: {e}")
        return []

def get_all_users():
    """Get all users in the database"""
    client = get_supabase_client()
    if not client:
        return []
    
    try:
        result = client.table('users').select('name').order('name').execute()
        return [{'name': user['name']} for user in result.data]
    except Exception as e:
        print(f"Error getting users: {e}")
        return []

def get_graph_data():
    """Get graph data for visualization"""
    client = get_supabase_client()
    if not client:
        return {'nodes': [], 'links': []}
    
    try:
        # Get all users
        users_result = client.table('users').select('*').execute()
        
        # Get friendships (avoid duplicates)
        friendships_result = client.table('friendships').select('user1_id, user2_id').execute()
        
        # Count connections per user
        connection_count = defaultdict(int)
        for f in friendships_result.data:
            connection_count[f['user1_id']] += 1
        
        # Build nodes
        nodes = []
        for user in users_result.data:
            nodes.append({
                'id': user['name'],
                'connections': connection_count.get(user['id'], 0)
            })
        
        # Build links (avoid duplicates)
        links = []
        added_pairs = set()
        user_name_map = {user['id']: user['name'] for user in users_result.data}
        
        for f in friendships_result.data:
            user1_id = f['user1_id']
            user2_id = f['user2_id']
            
            if user1_id < user2_id:  # Only add one direction
                pair_key = (user1_id, user2_id)
                if pair_key not in added_pairs:
                    links.append({
                        'source': user_name_map.get(user1_id),
                        'target': user_name_map.get(user2_id)
                    })
                    added_pairs.add(pair_key)
        
        return {'nodes': nodes, 'links': links}
    except Exception as e:
        print(f"Error getting graph data: {e}")
        return {'nodes': [], 'links': []}

def get_statistics():
    """Get database statistics"""
    client = get_supabase_client()
    if not client:
        return {}
    
    try:
        stats = {}
        
        # Total users
        users_result = client.table('users').select('id', count='exact').execute()
        stats['total_users'] = users_result.count if users_result.count else 0
        
        # Total friendships (divide by 2 for undirected)
        friendships_result = client.table('friendships').select('id', count='exact').execute()
        stats['total_connections'] = (friendships_result.count // 2) if friendships_result.count else 0
        
        # Average connections per user
        if stats['total_users'] > 0:
            stats['avg_connections'] = round(stats['total_connections'] * 2 / stats['total_users'], 2)
        else:
            stats['avg_connections'] = 0
        
        return stats
    except Exception as e:
        print(f"Error getting statistics: {e}")
        return {'total_users': 0, 'total_connections': 0, 'avg_connections': 0}

# Flask Routes
@app.route('/')
def index():
    """Home page"""
    stats = get_statistics()
    return render_template('index.html', stats=stats)

@app.route('/load-data', methods=['POST'])
def load_data():
    """Load data from CSV file"""
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            filepath = os.path.join('data', 'uploaded_data.csv')
            os.makedirs('data', exist_ok=True)
            file.save(filepath)
            success, message = load_data_from_csv(filepath)
        else:
            success, message = False, "No file selected"
    else:
        # Load demo data
        demo_file = os.path.join('data', 'social_network_demo.csv')
        if os.path.exists(demo_file):
            success, message = load_data_from_csv(demo_file)
        else:
            success, message = False, "Demo file not found"
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    
    return redirect(url_for('index'))

@app.route('/analysis')
def analysis():
    """Analysis page"""
    stats = get_statistics()
    influencers = get_influencers(15)
    users = get_all_users()
    return render_template('analysis.html', stats=stats, influencers=influencers, users=users)

@app.route('/recommendations/<username>')
def recommendations(username):
    """Get recommendations for a specific user"""
    recs = get_friend_recommendations(username, 15)
    return render_template('recommendations.html', username=username, recommendations=recs)

@app.route('/mutual-friends', methods=['POST'])
def mutual_friends():
    """Get mutual friends between two users"""
    user1 = request.form.get('user1')
    user2 = request.form.get('user2')
    
    if user1 and user2:
        mutual = get_mutual_friends(user1, user2)
        return render_template('mutual_friends.html', user1=user1, user2=user2, mutual_friends=mutual)
    else:
        flash('Please select both users', 'error')
        return redirect(url_for('analysis'))

@app.route('/visualization')
def visualization():
    """Graph visualization page"""
    return render_template('visualization.html')

@app.route('/api/graph-data')
def api_graph_data():
    """API endpoint for graph data"""
    data = get_graph_data()
    return jsonify(data)

@app.route('/api/recommendations/<username>')
def api_recommendations(username):
    """API endpoint for recommendations"""
    recs = get_friend_recommendations(username, 10)
    return jsonify(recs)

@app.route('/clear-database', methods=['POST'])
def clear_db():
    """Clear all data from database"""
    if clear_database():
        flash('Database cleared successfully', 'success')
    else:
        flash('Error clearing database', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("=" * 60)
    print("Friend Recommendation System - Supabase + Flask")
    print("=" * 60)
    print(f"Supabase URL: {SUPABASE_URL}")
    print("Starting Flask server...")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
