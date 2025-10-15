# 🎯 Friend Recommendation System using Neo4j Graph Database

A complete web-based friend recommendation system built with **Neo4j**, **Flask**, and **D3.js** for Big Data Analytics courses.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![Neo4j](https://img.shields.io/badge/Neo4j-5.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Algorithms](#algorithms)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## 🌟 Overview

This project demonstrates graph database concepts and social network analysis using Neo4j. It provides:
- **Friend recommendations** based on mutual connections
- **Influencer detection** (most connected users)
- **Mutual friend finder** between any two users
- **Interactive graph visualization** with D3.js
- **Beautiful web UI** with Bootstrap 5

Perfect for learning Big Data Analytics, Graph Databases, and Full-Stack Python Development!

## ✨ Features

### Core Functionality
- ✅ **Auto-load demo data** - Quick start with pre-configured social network
- ✅ **CSV upload** - Import your own social network data
- ✅ **Smart recommendations** - Friends-of-friends algorithm
- ✅ **Influencer analysis** - Find most connected users
- ✅ **Mutual friends** - Discover common connections
- ✅ **Interactive visualization** - Drag, zoom, and explore the network
- ✅ **Real-time statistics** - User count, connections, averages

### UI Features
- 🎨 Modern, responsive design with Bootstrap 5
- 📊 Interactive D3.js graph visualization
- 📈 Statistical dashboards and charts
- 🎯 One-click data loading and analysis
- 📱 Mobile-friendly interface

## 🛠 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.8+, Flask 3.0 |
| **Database** | Neo4j 5.x (Graph Database) |
| **Driver** | neo4j-python-driver 5.14 |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Visualization** | D3.js v7 |
| **Icons** | Font Awesome 6 |

## 📦 Prerequisites

### Required Software
1. **Python 3.8 or higher**
   ```powershell
   python --version
   ```

2. **Neo4j Database** (Community or Desktop)
   - Download from: https://neo4j.com/download/
   - OR use Neo4j Desktop (recommended for beginners)
   - OR use Docker:
     ```powershell
     docker run -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:latest
     ```

3. **Git** (for cloning the repository)
   ```powershell
   git --version
   ```

## 🚀 Installation

### Step 1: Clone or Download Project
```powershell
cd d:\bda
# Project is already in: d:\bda\project1-neo4j-friend-recommendation
```

### Step 2: Create Virtual Environment (Recommended)
```powershell
cd project1-neo4j-friend-recommendation
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```powershell
pip install -r requirements.txt
```

Expected packages:
- Flask 3.0.0
- neo4j 5.14.1
- python-dotenv 1.0.0
- Werkzeug 3.0.1

### Step 4: Set Up Neo4j Database

#### Option A: Neo4j Desktop (Easiest)
1. Download and install Neo4j Desktop
2. Create a new project
3. Create a new database with password
4. Start the database
5. Note the connection URI (usually `bolt://localhost:7687`)

#### Option B: Neo4j Community Edition
1. Download and extract Neo4j
2. Start Neo4j:
   ```powershell
   .\bin\neo4j.bat console
   ```
3. Access Neo4j Browser at `http://localhost:7474`
4. Set initial password for `neo4j` user

#### Option C: Docker
```powershell
docker run -d `
  --name neo4j-friend-recommender `
  -p 7474:7474 -p 7687:7687 `
  -e NEO4J_AUTH=neo4j/password `
  neo4j:latest
```

### Step 5: Configure Connection

Create `.env` file in project root:
```powershell
cp .env.example .env
```

Edit `.env` with your Neo4j credentials:
```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password_here
FLASK_ENV=development
FLASK_DEBUG=True
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `NEO4J_URI` | Neo4j connection URI | `bolt://localhost:7687` |
| `NEO4J_USER` | Neo4j username | `neo4j` |
| `NEO4J_PASSWORD` | Neo4j password | `password` |
| `FLASK_ENV` | Flask environment | `development` |
| `FLASK_DEBUG` | Enable debug mode | `True` |

### Data Format

CSV files should have two columns (no header required):
```csv
user1,user2
Alice,Bob
Bob,Charlie
Charlie,David
```

Each row represents a friendship connection between two users.

## 🎮 Usage

### Quick Start (3 Steps!)

1. **Start Neo4j Database**
   ```powershell
   # If using Neo4j Desktop: Start your database
   # If using Docker: Container should be running
   # If using Community: neo4j console should be running
   ```

2. **Run Flask Application**
   ```powershell
   python app.py
   ```

3. **Open Browser**
   - Navigate to: `http://localhost:5000`
   - Click **"Load Demo Data"** to populate with sample network
   - Click **"Run Analysis"** to see recommendations

### Step-by-Step Workflow

#### 1. Load Data
- **Option A**: Click "Load Demo Data" for instant setup with 25+ users
- **Option B**: Upload your own CSV file

#### 2. Run Analysis
- Go to **Analysis** page
- View **Top Influencers** (most connected users)
- Select a user to see **Friend Recommendations**
- Find **Mutual Friends** between any two users

#### 3. Visualize Network
- Go to **Visualization** page
- Interact with the graph:
  - **Drag** nodes to rearrange
  - **Scroll** to zoom in/out
  - **Click** nodes for details
  - **Reset Zoom** button to reset view

#### 4. Explore Recommendations
- Click on any user to see their recommendations
- Recommendations ranked by number of mutual friends
- Visual progress bars show recommendation strength

## 📁 Project Structure

```
project1-neo4j-friend-recommendation/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment configuration template
├── .env                       # Your configuration (create this)
├── README.md                  # This file
│
├── data/
│   └── social_network_demo.csv # Demo dataset (25+ users)
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Home page
│   ├── analysis.html          # Analysis dashboard
│   ├── recommendations.html   # Friend recommendations
│   ├── mutual_friends.html    # Mutual friends finder
│   └── visualization.html     # Graph visualization
│
└── docs/                       # Documentation
    ├── SETUP_GUIDE.md         # Detailed setup instructions
    ├── ALGORITHMS.md          # Algorithm explanations
    └── API_DOCUMENTATION.md   # API reference
```

## 🧮 Algorithms

### 1. Friend Recommendation Algorithm
```cypher
MATCH (user:User {name: $user_name})-[:FRIENDS_WITH]->(friend)-[:FRIENDS_WITH]->(foaf)
WHERE NOT (user)-[:FRIENDS_WITH]->(foaf) AND user <> foaf
WITH foaf, COUNT(DISTINCT friend) AS mutual_friends
RETURN foaf.name AS recommended_friend, mutual_friends
ORDER BY mutual_friends DESC
```

**How it works:**
- Finds friends-of-friends (FOAF)
- Excludes existing friends
- Ranks by number of mutual connections
- Higher mutual friends = stronger recommendation

### 2. Influencer Detection
```cypher
MATCH (user:User)-[r:FRIENDS_WITH]->()
WITH user, COUNT(r) AS connections
RETURN user.name AS name, connections
ORDER BY connections DESC
```

**How it works:**
- Counts outgoing FRIENDS_WITH relationships
- Sorts users by connection count
- Top users are "influencers"

### 3. Mutual Friends Finder
```cypher
MATCH (u1:User {name: $user1})-[:FRIENDS_WITH]->(mutual)<-[:FRIENDS_WITH]-(u2:User {name: $user2})
RETURN mutual.name AS mutual_friend
```

**How it works:**
- Finds paths from user1 → mutual friend ← user2
- Returns all common connections

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/load-data` | POST | Load data from CSV |
| `/analysis` | GET | Analysis dashboard |
| `/recommendations/<username>` | GET | User recommendations |
| `/mutual-friends` | POST | Find mutual friends |
| `/visualization` | GET | Graph visualization |
| `/api/graph-data` | GET | JSON graph data |
| `/api/recommendations/<username>` | GET | JSON recommendations |
| `/clear-database` | POST | Clear all data |

### Example API Usage

```python
import requests

# Get graph data
response = requests.get('http://localhost:5000/api/graph-data')
data = response.json()

# Get recommendations
response = requests.get('http://localhost:5000/api/recommendations/Alice')
recommendations = response.json()
```

## 📸 Screenshots

### Home Page
- Statistics dashboard with user count, connections, average
- One-click demo data loading
- File upload for custom datasets

### Analysis Page
- Top influencers table with connection counts
- User selection for recommendations
- Mutual friends finder

### Visualization Page
- Interactive D3.js force-directed graph
- Color-coded by connection count
- Zoom, pan, and drag functionality

## 🐛 Troubleshooting

### Common Issues

#### 1. "Could not connect to Neo4j"
**Solution:**
- Verify Neo4j is running: Check Neo4j Desktop or console
- Check connection URI in `.env` file
- Test connection: `http://localhost:7474`
- Verify credentials are correct

#### 2. "No module named 'neo4j'"
**Solution:**
```powershell
pip install neo4j
# OR
pip install -r requirements.txt
```

#### 3. "Port 5000 already in use"
**Solution:**
Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

#### 4. "Demo file not found"
**Solution:**
Ensure `data/social_network_demo.csv` exists in project root

#### 5. Neo4j Authentication Failed
**Solution:**
- Reset Neo4j password in Neo4j Browser
- Update `.env` file with new password
- Restart Flask application

### Debugging Tips

**Enable verbose logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Check Neo4j connectivity:**
```python
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
driver.verify_connectivity()
driver.close()
```

## 🎓 Educational Use

### Learning Objectives
- ✅ Understand graph databases vs relational databases
- ✅ Write Cypher queries for graph traversal
- ✅ Implement social network analysis algorithms
- ✅ Build full-stack Python web applications
- ✅ Create interactive data visualizations

### Exercises for Students
1. **Beginner**: Modify recommendation count limit
2. **Intermediate**: Add "2nd degree" recommendations
3. **Advanced**: Implement community detection algorithm
4. **Expert**: Add real-time graph updates with WebSockets

### Assessment Ideas
- Compare performance: Neo4j vs SQL for friend recommendations
- Analyze time complexity of algorithms
- Implement new metrics (clustering coefficient, betweenness centrality)
- Create presentation on graph database advantages

## 📝 License

This project is created for educational purposes. Feel free to use, modify, and distribute.

## 👥 Contributing

Contributions welcome! Areas for improvement:
- Additional graph algorithms
- Performance optimizations
- More visualization options
- Extended test coverage

## 📞 Support

For issues or questions:
1. Check [Troubleshooting](#troubleshooting) section
2. Review Neo4j documentation: https://neo4j.com/docs/
3. Flask documentation: https://flask.palletsprojects.com/

## 🔗 Resources

- [Neo4j Graph Academy](https://graphacademy.neo4j.com/)
- [Cypher Query Language](https://neo4j.com/developer/cypher/)
- [D3.js Gallery](https://observablehq.com/@d3/gallery)
- [Flask Tutorial](https://flask.palletsprojects.com/tutorial/)

---

## 🚀 Quick Command Reference

```powershell
# Setup
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Run
python app.py

# Access
# Browser: http://localhost:5000
# Neo4j Browser: http://localhost:7474

# Clean up
pip uninstall -r requirements.txt -y
deactivate
```

---

**Built with ❤️ for Big Data Analytics Education**

**Project Type:** Educational Mini-Project  
**Difficulty:** Intermediate  
**Time to Complete:** 2-3 hours  
**Status:** Production Ready ✅
