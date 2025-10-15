# 🚀 SUPABASE SETUP GUIDE

## ✅ Project Converted to Supabase!

Your Friend Recommendation System now uses **Supabase (PostgreSQL)** instead of Neo4j.

---

## 📋 Step-by-Step Setup

### Step 1: Create Supabase Account & Project

1. **Go to**: https://supabase.com
2. **Click**: "Start your project"
3. **Sign up**: Using GitHub, Google, or email
4. **Create new project**:
   - Organization: Create one or use existing
   - Name: `friend-recommender` 
   - Database Password: Set a strong password
   - Region: Choose closest to you
   - Click "Create new project"
   
5. **Wait**: ~2 minutes for project to be ready

### Step 2: Create Database Tables

Once your project is ready:

1. Click **"SQL Editor"** in the left sidebar
2. Click **"New query"**
3. **Copy and paste** this SQL:

```sql
-- Create users table
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::TEXT, NOW()) NOT NULL
);

-- Create friendships table
CREATE TABLE friendships (
    id BIGSERIAL PRIMARY KEY,
    user1_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
    user2_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::TEXT, NOW()) NOT NULL,
    UNIQUE(user1_id, user2_id)
);

-- Create indexes for better performance
CREATE INDEX idx_friendships_user1 ON friendships(user1_id);
CREATE INDEX idx_friendships_user2 ON friendships(user2_id);
CREATE INDEX idx_users_name ON users(name);

-- Enable Row Level Security (optional but recommended)
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE friendships ENABLE ROW LEVEL SECURITY;

-- Create policies to allow all operations (for development)
CREATE POLICY "Enable read access for all users" ON users FOR SELECT USING (true);
CREATE POLICY "Enable insert access for all users" ON users FOR INSERT WITH CHECK (true);
CREATE POLICY "Enable update access for all users" ON users FOR UPDATE USING (true);
CREATE POLICY "Enable delete access for all users" ON users FOR DELETE USING (true);

CREATE POLICY "Enable read access for all users" ON friendships FOR SELECT USING (true);
CREATE POLICY "Enable insert access for all users" ON friendships FOR INSERT WITH CHECK (true);
CREATE POLICY "Enable update access for all users" ON friendships FOR UPDATE USING (true);
CREATE POLICY "Enable delete access for all users" ON friendships FOR DELETE USING (true);
```

4. Click **"Run"** button
5. You should see "Success. No rows returned"

### Step 3: Get Your Supabase Credentials

1. Click **"Settings"** (gear icon) in the left sidebar
2. Click **"API"** 
3. You'll see:
   - **Project URL**: Copy this (looks like: `https://xxxxx.supabase.co`)
   - **Project API keys** → **anon** **public**: Copy this key

### Step 4: Update `.env` File

Create or edit `.env` file in your project:

```env
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key-here

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

Replace with your actual values!

### Step 5: Install Dependencies

```powershell
cd d:\bda\project1-neo4j-friend-recommendation
pip install -r requirements.txt
```

### Step 6: Run the Application

```powershell
python app.py
```

### Step 7: Load Data

1. Open browser: `http://localhost:5000`
2. Click **"Load Demo Data"**
3. Wait for success message
4. Explore! 🎉

---

## 🔍 Verify Data in Supabase

1. Go to your Supabase project dashboard
2. Click **"Table Editor"** in sidebar
3. Click **"users"** table - you should see 100 Indian names
4. Click **"friendships"** table - you should see 1600+ rows (832 connections × 2 directions)

---

## 📊 What Changed from Neo4j?

| Aspect | Neo4j | Supabase |
|--------|-------|----------|
| Database Type | Graph DB | Relational (PostgreSQL) |
| Connection | bolt://localhost:7687 | HTTPS API |
| Query Language | Cypher | SQL |
| Setup | Local installation | Cloud-based |
| Cost | Free (local) | Free tier available |
| Hosting | Your computer | Supabase cloud |

---

## ✅ Advantages of Supabase

- ✅ **No local installation** needed
- ✅ **Cloud-based** - accessible anywhere
- ✅ **Automatic backups**
- ✅ **Real-time subscriptions** available
- ✅ **Built-in authentication** (if needed later)
- ✅ **Free tier** generous (500MB database, 2GB bandwidth)
- ✅ **Web interface** to view/edit data

---

## 🎯 Quick Reference

**Supabase Dashboard**: https://app.supabase.com  
**Flask App**: http://localhost:5000  
**Documentation**: https://supabase.com/docs

---

## 🐛 Troubleshooting

### "Could not connect to Supabase"
- Check `.env` file has correct URL and KEY
- Verify project is active in Supabase dashboard
- Check internet connection

### "Table doesn't exist"
- Run the SQL script in Step 2 again
- Check Table Editor to verify tables exist

### "No data showing"
- Load demo data first from home page
- Check Supabase Table Editor to verify data

---

**Status**: ✅ Ready to use Supabase!
**Next**: Create your Supabase account and follow the steps above!
