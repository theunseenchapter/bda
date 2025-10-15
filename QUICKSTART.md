# Quick Start Guide - Friend Recommendation System

## 🎯 Goal
Get the Friend Recommendation System running in **5 minutes**!

## ✅ Prerequisites Checklist
- [ ] Python 3.8+ installed
- [ ] Neo4j installed and running (Desktop, Community, or Docker)
- [ ] Neo4j password set

## 🚀 Installation Steps

### Step 1: Navigate to Project
```powershell
cd d:\bda\project1-neo4j-friend-recommendation
```

### Step 2: Run Automated Setup
```powershell
.\setup.ps1
```

This script will:
- ✅ Check Python installation
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create `.env` configuration file

### Step 3: Configure Neo4j Connection

Edit `.env` file with your Neo4j credentials:
```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=YOUR_PASSWORD_HERE
```

**Don't know your Neo4j password?**
- **Neo4j Desktop**: Check database settings
- **First time?**: Default is often `neo4j` but you must change it on first login
- **Forgot?**: Reset in Neo4j Browser (http://localhost:7474)

### Step 4: Start Neo4j
- **Neo4j Desktop**: Click "Start" on your database
- **Neo4j Community**: Run `neo4j console` in Neo4j directory
- **Docker**: `docker start neo4j-friend-recommender`

### Step 5: Run the Application
```powershell
.\run.ps1
```

Or manually:
```powershell
.\venv\Scripts\Activate.ps1
python app.py
```

### Step 6: Access the Application
Open your browser and go to:
```
http://localhost:5000
```

## 🎮 First-Time Usage

### Quick Demo (1 minute)
1. Click **"Load Demo Data"** button on home page
2. Wait for success message
3. Click **"Run Analysis"** to see recommendations
4. Click **"Visualization"** to see the graph

### Manual Data Upload
1. Prepare CSV file with format:
   ```csv
   Alice,Bob
   Bob,Charlie
   Charlie,Alice
   ```
2. Click **"Upload Custom Data"**
3. Select your CSV file
4. Click **"Upload & Load"**

## 📊 Features to Explore

### 1. Analysis Page
- **Top Influencers**: See most connected users
- **Friend Recommendations**: Click any user to see their recommendations
- **Mutual Friends**: Select two users to find common connections

### 2. Visualization Page
- **Interactive Graph**: Drag nodes, zoom in/out
- **Color Coding**: 
  - Blue = Highly connected (5+ friends)
  - Green = Well connected (3-4 friends)
  - Orange = Moderately connected (2 friends)
  - Red = Lightly connected (1 friend)
- **Node Details**: Click any node to see user info

### 3. Home Page
- **Statistics Dashboard**: View network metrics
- **Data Management**: Load or clear data
- **Quick Actions**: Navigate to features

## 🐛 Troubleshooting

### Problem: "Could not connect to Neo4j"
**Solution:**
1. Check Neo4j is running: `http://localhost:7474`
2. Verify credentials in `.env` file
3. Test connection in Neo4j Browser

### Problem: "No module named 'neo4j'"
**Solution:**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Problem: "Port 5000 already in use"
**Solution:**
Edit `app.py`, change last line to:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Then access: `http://localhost:5001`

### Problem: "Demo file not found"
**Solution:**
Check that `data/social_network_demo.csv` exists in your project folder.

### Problem: Virtual environment not activating
**Solution:**
Enable PowerShell scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📝 Common Commands

### Start Everything
```powershell
# Start Neo4j (if using Docker)
docker start neo4j-friend-recommender

# Activate environment and run
cd d:\bda\project1-neo4j-friend-recommendation
.\run.ps1
```

### Stop Everything
```powershell
# Press Ctrl+C in terminal to stop Flask

# Stop Neo4j (if using Docker)
docker stop neo4j-friend-recommender
```

### Reset Database
1. Go to `http://localhost:5000`
2. Click **"Clear Database"** button
3. Reload demo data or upload new data

### Check Logs
Flask logs appear in your terminal. Look for:
```
* Running on http://0.0.0.0:5000
* Restarting with stat
* Debugger is active!
```

## 🎓 Learning Path

### Beginner
1. Load demo data and explore UI
2. Try finding mutual friends
3. View different user recommendations
4. Play with graph visualization

### Intermediate
1. Upload your own social network CSV
2. Analyze the influencers
3. Understand Cypher queries in `app.py`
4. Modify recommendation algorithm

### Advanced
1. Add new features (e.g., community detection)
2. Optimize Neo4j queries
3. Add authentication
4. Deploy to cloud (Heroku, AWS, etc.)

## 📚 Next Steps

### Explore the Code
- `app.py`: Flask routes and Neo4j queries
- `templates/`: HTML pages with Bootstrap
- `templates/visualization.html`: D3.js graph code

### Modify the System
- Change graph colors in `visualization.html`
- Add new statistics in `app.py`
- Customize UI in template files

### Learn More
- **Neo4j Cypher**: https://neo4j.com/developer/cypher/
- **Flask Tutorials**: https://flask.palletsprojects.com/
- **D3.js Examples**: https://observablehq.com/@d3/gallery

## 🎯 Assignment Ideas (for Students)

1. **Basic**: Add a "Delete User" feature
2. **Intermediate**: Implement "friend suggestions" based on common interests
3. **Advanced**: Add PageRank algorithm to find influencers
4. **Expert**: Create REST API for mobile app integration

## ✅ Success Criteria

You'll know it's working when:
- ✅ Home page loads with statistics
- ✅ Demo data loads successfully
- ✅ Analysis page shows influencers
- ✅ Recommendations appear for users
- ✅ Graph visualization is interactive
- ✅ No error messages in browser or terminal

## 📞 Need Help?

1. Check `README.md` for detailed documentation
2. Review error messages in terminal
3. Check Neo4j Browser: `http://localhost:7474`
4. Verify all files exist in project structure

---

**Estimated Time**: 5-10 minutes for complete setup  
**Difficulty**: Beginner-Friendly  
**Status**: Ready to Run! ✅

🎉 **Happy Learning!**
