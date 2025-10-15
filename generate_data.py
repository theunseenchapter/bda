"""
Generate Social Network Demo Data with Indian Names
Creates 1000+ connections between users
"""

import random
import csv

# Indian names for social network
indian_names = [
    # Male names
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Arnav", "Ayaan", "Krishna", "Ishaan",
    "Shaurya", "Atharva", "Advik", "Pranav", "Reyansh", "Muhammad", "Siddharth", "Samar", "Advait", "Dhruv",
    "Kabir", "Kiaan", "Vedant", "Aryan", "Ayush", "Aarush", "Daksh", "Veer", "Yash", "Shivansh",
    "Rudra", "Kian", "Parth", "Rohan", "Ritvik", "Aaryan", "Aayan", "Aayansh", "Darsh", "Devansh",
    "Karthik", "Lakshay", "Madhav", "Mayank", "Neil", "Nirav", "Om", "Pranay", "Raghav", "Rishi",
    "Tanish", "Vihaan", "Viraj", "Yug", "Aadhya", "Advay", "Agastya", "Akarsh", "Anay", "Anirudh",
    
    # Female names
    "Aadhya", "Ananya", "Diya", "Pari", "Saanvi", "Sara", "Anika", "Navya", "Angel", "Aaradhya",
    "Myra", "Shanaya", "Pihu", "Prisha", "Anvi", "Riya", "Siya", "Ira", "Aanya", "Alina",
    "Kiara", "Khushi", "Nora", "Zara", "Mira", "Ishika", "Tara", "Avni", "Sana", "Aditi",
    "Anaya", "Aria", "Ayesha", "Disha", "Eva", "Hiya", "Inaya", "Jiya", "Kavya", "Larisa",
    "Mahika", "Naira", "Palak", "Ria", "Samara", "Tanya", "Vanya", "Zoya", "Aisha", "Divya",
    "Naina", "Nidhi", "Pooja", "Priya", "Rhea", "Shreya", "Simran", "Sneha", "Srishti", "Tanvi",
    
    # Additional names for variety
    "Abhay", "Ajay", "Akash", "Ankit", "Ashish", "Chetan", "Deepak", "Gaurav", "Harsh", "Karan",
    "Manish", "Nikhil", "Pawan", "Rahul", "Raj", "Ravi", "Sachin", "Sandeep", "Suresh", "Varun",
    "Amit", "Anand", "Anil", "Arun", "Bharat", "Dev", "Dinesh", "Ganesh", "Hari", "Jay",
    "Kavita", "Komal", "Lakshmi", "Meera", "Neha", "Payal", "Radha", "Rekha", "Ritu", "Seema",
    "Shweta", "Sonal", "Sunita", "Usha", "Veena", "Vidya", "Anjali", "Bhavna", "Chandni", "Deepa",
]

# Ensure we have exactly 100 unique names
indian_names = list(set(indian_names))[:100]

def generate_social_network(num_users=100, connections_per_user_avg=10):
    """
    Generate a realistic social network
    
    Args:
        num_users: Number of users in the network
        connections_per_user_avg: Average number of friends per user
    
    Returns:
        List of tuples representing friendships
    """
    connections = set()
    
    # Create random connections ensuring some clustering
    for i, user1 in enumerate(indian_names[:num_users]):
        # Number of friends varies (5-15 friends per person)
        num_friends = random.randint(5, 15)
        
        for _ in range(num_friends):
            # Higher probability of connecting to nearby users (creates clusters)
            if random.random() < 0.7:
                # Connect to someone nearby in the list (clustering)
                range_size = min(20, num_users - 1)
                offset = random.randint(1, range_size)
                user2_idx = (i + offset) % num_users
            else:
                # Connect to anyone (long-distance connections)
                user2_idx = random.randint(0, num_users - 1)
            
            user2 = indian_names[user2_idx]
            
            # Avoid self-connections
            if user1 != user2:
                # Store in sorted order to avoid duplicates
                connection = tuple(sorted([user1, user2]))
                connections.add(connection)
    
    return list(connections)

def create_demo_csv(filename, num_users=100):
    """
    Create a CSV file with social network connections
    
    Args:
        filename: Output CSV filename
        num_users: Number of users to include
    """
    connections = generate_social_network(num_users)
    
    # Write to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['user1', 'user2'])
        
        # Write connections
        for user1, user2 in connections:
            writer.writerow([user1, user2])
    
    print(f"✅ Generated {len(connections)} connections between {num_users} users")
    print(f"✅ Average connections per user: {len(connections) * 2 / num_users:.1f}")
    print(f"✅ Saved to: {filename}")
    
    # Show sample data
    print(f"\nSample connections:")
    for conn in list(connections)[:10]:
        print(f"  {conn[0]} ←→ {conn[1]}")

if __name__ == "__main__":
    # Generate the demo dataset
    create_demo_csv(
        'data/social_network_demo.csv',
        num_users=100  # Using 100 users to get 1000+ connections
    )
    
    print("\n" + "="*60)
    print("✅ Demo data generation complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Make sure Neo4j is running")
    print("2. Start Flask app: python app.py")
    print("3. Go to http://localhost:5000")
    print("4. Click 'Load Demo Data'")
    print("5. Explore the social network!")
