# 🚀 STEP-BY-STEP STARTUP GUIDE

## ✅ Current Status
- ✅ Python installed (3.13.0)
- ✅ Virtual environment created
- ✅ Dependencies installed
- ✅ Flask app ready
- ❌ **Neo4j NOT running** ← YOU ARE HERE

---

## 📋 What You Need To Do Now

### Step 1: Start Neo4j Database

#### Option A: If you have Neo4j Desktop (Recommended)
1. Open **Neo4j Desktop** application
2. Find your database (or create one if you don't have any)
3. Click the **"Start"** button
4. Wait for the status to show **"Running"**
5. Note the password you set (default user is `neo4j`)

#### Option B: If you have Neo4j Community Edition
```powershell
# Navigate to your Neo4j installation directory
cd "C:\neo4j-community-<version>"  # Adjust path as needed
.\bin\neo4j.bat console
```

#### Option C: If you have Docker
```powershell
# Start Neo4j in Docker
docker run -d `
  --name neo4j-friend-recommender `
  -p 7474:7474 -p 7687:7687 `
  -e NEO4J_AUTH=neo4j/password `
  neo4j:latest

# Or if container already exists:
docker start neo4j-friend-recommender
```

#### Option D: Install Neo4j Now
If you don't have Neo4j installed:
1. Download Neo4j Desktop: https://neo4j.com/download/
2. Install it
3. Create a new database
4. Set password
5. Start the database

---

### Step 2: Update .env File with Your Password

Edit the file: `d:\bda\project1-neo4j-friend-recommendation\.env`

Change this line:
```
NEO4J_PASSWORD=password
```

To your actual Neo4j password (keep `neo4j` as username unless you changed it).

---

### Step 3: Verify Neo4j is Running

Open your browser and go to:
```
http://localhost:7474
```

You should see the **Neo4j Browser** interface.

**Test connection:**
- Username: `neo4j`
- Password: (your password)
- Connect URL: `bolt://localhost:7687`

If you can log in, Neo4j is running! ✅

---

### Step 4: Restart Flask Application

The Flask app is already running but couldn't connect. Once Neo4j is started:

1. Go back to the terminal running Flask
2. Press `Ctrl+C` to stop it
3. Run again:
   ```powershell
   python app.py
   ```

Or just refresh your browser at `http://localhost:5000`

---

## 🎯 Once Everything is Running

### Step 5: Load Demo Data

1. Open browser: `http://localhost:5000`
2. Click the big green button: **"Load Demo Data"**
3. Wait for success message
4. You should see statistics update!

### Step 6: Verify Data in Neo4j

#### Method 1: Using Neo4j Browser
1. Open: `http://localhost:7474`
2. Run this query:
   ```cypher
   MATCH (n:User) RETURN n LIMIT 25
   ```
3. You should see a beautiful graph visualization!

#### Method 2: Count Users
```cypher
MATCH (n:User) RETURN count(n) as total_users
```
Should return: **26 users**

#### Method 3: View All Connections
```cypher
MATCH (u1:User)-[r:FRIENDS_WITH]->(u2:User)
RETURN u1.name, u2.name
LIMIT 50
```

#### Method 4: Visualize Full Network
```cypher
MATCH (n:User)-[r:FRIENDS_WITH]->(m:User)
RETURN n, r, m
```
Click the "Graph" tab to see the full network!

---

## 📸 What You Should See

### In Flask App (http://localhost:5000)
```
Statistics Dashboard:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Total Users    │  │  Connections    │  │  Avg per User   │
│      26         │  │      50+        │  │      ~4         │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### In Neo4j Browser (http://localhost:7474)
You'll see a **network graph** with:
- 26 nodes (users: Alice, Bob, Charlie, etc.)
- 50+ relationships (FRIENDS_WITH connections)
- Interactive visualization you can drag and zoom

---

## 🐛 Troubleshooting

### "Connection Refused" Error
**Problem**: Neo4j is not running  
**Solution**: Start Neo4j (see Step 1 above)

### "Authentication Failed"
**Problem**: Wrong password in `.env` file  
**Solution**: Update `.env` with correct password

### "Database Not Found"
**Problem**: Database doesn't exist in Neo4j  
**Solution**: Create a database in Neo4j Desktop

### Flask Won't Start
**Problem**: Port 5000 in use  
**Solution**: Change port in `app.py` line 291:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## ✅ Success Checklist

- [ ] Neo4j is running (check http://localhost:7474)
- [ ] Can log into Neo4j Browser
- [ ] `.env` file has correct password
- [ ] Flask app is running (check http://localhost:5000)
- [ ] Home page loads without errors
- [ ] Clicked "Load Demo Data"
- [ ] Statistics show 26 users
- [ ] Can see graph in Neo4j Browser
- [ ] Can click "Visualization" and see interactive graph

---

## 🎉 Next Steps After Setup

1. **Explore Analysis Page**: Click "Run Analysis"
2. **View Recommendations**: Click on any user name
3. **Find Mutual Friends**: Select two users
4. **See Graph**: Go to "Visualization" page
5. **Check Neo4j**: Run queries in Neo4j Browser

---

## 📞 Quick Reference

**Flask App**: http://localhost:5000  
**Neo4j Browser**: http://localhost:7474  
**Neo4j Bolt**: bolt://localhost:7687  

**Default Credentials**:
- Username: `neo4j`
- Password: (yours - set during Neo4j setup)

---

## 🚨 IMPORTANT: What To Show

To demonstrate that data is in Neo4j, show:

### 1. In Neo4j Browser (http://localhost:7474):
```cypher
// Show all users
MATCH (n:User) RETURN n

// Show network graph
MATCH (n:User)-[r:FRIENDS_WITH]->(m:User)
RETURN n, r, m

// Count everything
MATCH (n:User) RETURN count(n) as users
```

### 2. In Flask App (http://localhost:5000):
- Statistics dashboard showing user count
- Click "Analysis" → See influencers table
- Click "Visualization" → Interactive graph

### 3. Screenshot Evidence:
Take screenshots of:
- ✅ Neo4j Browser showing the graph
- ✅ Flask app showing statistics
- ✅ Flask app showing recommendations
- ✅ Interactive visualization

---

**Current Status**: Flask is ready, waiting for Neo4j to start! 🚀

**Next Action**: Start Neo4j, then refresh browser!
