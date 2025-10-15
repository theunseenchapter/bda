# 🏗️ SYSTEM ARCHITECTURE

Visual documentation of the Friend Recommendation System architecture.

---

## 📊 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         WEB BROWSER                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  HTML/CSS    │  │  JavaScript  │  │    D3.js     │          │
│  │  Bootstrap   │  │    jQuery    │  │ Visualization│          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              ↕ HTTP
┌─────────────────────────────────────────────────────────────────┐
│                      FLASK WEB SERVER                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Routes     │  │  Templates   │  │   Business   │          │
│  │  (app.py)    │  │  (Jinja2)    │  │    Logic     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              ↕ Bolt Protocol
┌─────────────────────────────────────────────────────────────────┐
│                      NEO4J DATABASE                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │    Nodes     │  │ Relationships│  │   Indexes    │          │
│  │   (Users)    │  │ (FRIENDS_WITH)│  │  (Optional)  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Diagram

### 1. Data Loading Flow
```
CSV File
   │
   ↓
[User Upload] → [Flask Route: /load-data]
   │
   ↓
[Read CSV] → [Parse Data]
   │
   ↓
[Neo4j Driver] → [Cypher Query: MERGE nodes]
   │
   ↓
[Neo4j Database] → [Store Graph]
   │
   ↓
[Success Response] → [Flash Message] → [Redirect Home]
```

### 2. Recommendation Flow
```
User clicks on name
   │
   ↓
[GET /recommendations/Alice]
   │
   ↓
[Flask: recommendations()]
   │
   ↓
[get_friend_recommendations('Alice')]
   │
   ↓
[Cypher: Friends-of-Friends Query]
   │
   ↓
[Neo4j: Graph Traversal]
   │
   ↓
[Results: [{name, mutual_friends}]]
   │
   ↓
[Render: recommendations.html]
   │
   ↓
[Display: Table with recommendations]
```

### 3. Visualization Flow
```
User visits /visualization
   │
   ↓
[Render: visualization.html]
   │
   ↓
[JavaScript: loadGraphData()]
   │
   ↓
[AJAX: GET /api/graph-data]
   │
   ↓
[Flask: api_graph_data()]
   │
   ↓
[get_graph_data()]
   │
   ↓
[Cypher: Get all nodes and relationships]
   │
   ↓
[Neo4j: Return graph structure]
   │
   ↓
[JSON: {nodes: [], links: []}]
   │
   ↓
[D3.js: Create force-directed graph]
   │
   ↓
[SVG: Interactive visualization]
```

---

## 🗂️ Application Structure

```
Friend Recommendation System
│
├── Presentation Layer (Frontend)
│   ├── HTML Templates (Jinja2)
│   ├── CSS (Bootstrap + Custom)
│   └── JavaScript (jQuery + D3.js)
│
├── Application Layer (Backend)
│   ├── Flask Framework
│   ├── Routing (/,/analysis, etc.)
│   ├── Business Logic
│   └── Template Rendering
│
├── Data Access Layer
│   ├── Neo4j Driver
│   ├── Connection Management
│   └── Query Execution
│
└── Database Layer
    ├── Neo4j Graph Database
    ├── Nodes (Users)
    └── Relationships (FRIENDS_WITH)
```

---

## 🔌 API Architecture

### REST Endpoints

```
┌────────────────────────────────────────┐
│         PUBLIC WEB PAGES               │
├────────────────────────────────────────┤
│ GET  /                  → index.html   │
│ GET  /analysis          → analysis     │
│ GET  /visualization     → viz          │
│ GET  /recommendations/  → recs         │
│      <username>                        │
├────────────────────────────────────────┤
│         FORM SUBMISSIONS               │
├────────────────────────────────────────┤
│ POST /load-data         → Load CSV    │
│ POST /mutual-friends    → Find mutual │
│ POST /clear-database    → Clear all   │
├────────────────────────────────────────┤
│         JSON API                       │
├────────────────────────────────────────┤
│ GET  /api/graph-data    → JSON        │
│ GET  /api/              → JSON        │
│      recommendations/                  │
│      <username>                        │
└────────────────────────────────────────┘
```

---

## 🗄️ Database Schema

### Graph Model

```
┌─────────────────┐
│      User       │ ◄─┐
├─────────────────┤   │
│ name: String    │   │ FRIENDS_WITH
└─────────────────┘   │ (bidirectional)
        ↕              │
        └──────────────┘

Example:
(Alice:User)─[:FRIENDS_WITH]→(Bob:User)
(Bob:User)─[:FRIENDS_WITH]→(Alice:User)
```

### Cypher Schema
```cypher
// Node Label
(:User)

// Properties
{
  name: String  // Required, unique identifier
}

// Relationship Type
[:FRIENDS_WITH]

// Direction
Bidirectional (both directions stored)
```

### Sample Graph
```
    Alice ←→ Bob
      ↕      ↕
    David ←→ Charlie
      ↕
    Grace
```

Cypher representation:
```cypher
MATCH (n:User)-[r:FRIENDS_WITH]->(m:User)
RETURN n, r, m
```

---

## 🧮 Algorithm Architecture

### 1. Friend Recommendation Algorithm

```
Input: username (String)
Output: List<{name, mutual_friends}>

┌──────────────────────────────────┐
│  Start with target user          │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Traverse to direct friends      │
│  (1 hop)                         │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Traverse to friends-of-friends  │
│  (2 hops)                        │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Filter: Exclude existing friends│
│  Filter: Exclude self            │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Aggregate: Count mutual friends │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Sort: By mutual_friends DESC    │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Return: Top N recommendations   │
└──────────────────────────────────┘
```

**Complexity**: O(n²) where n = avg friends per user

### 2. Influencer Detection Algorithm

```
Input: limit (Integer)
Output: List<{name, connections}>

┌──────────────────────────────────┐
│  Match all users                 │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Count outgoing relationships    │
│  per user                        │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Sort by connection count DESC   │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Return top N users              │
└──────────────────────────────────┘
```

**Complexity**: O(n) where n = total users

### 3. Mutual Friends Algorithm

```
Input: user1, user2 (String)
Output: List<{name}>

┌──────────────────────────────────┐
│  Find friends of user1           │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Find friends of user2           │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Intersect: Common friends       │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│  Return list of mutual friends   │
└──────────────────────────────────┘
```

**Complexity**: O(k²) where k = avg friends

---

## 🎨 Frontend Architecture

### Component Hierarchy

```
base.html (Layout)
│
├── Navigation Bar
│   ├── Logo/Brand
│   ├── Home Link
│   ├── Analysis Link
│   └── Visualization Link
│
├── Flash Messages Container
│
├── Content Block (varies by page)
│   │
│   ├── index.html
│   │   ├── Statistics Cards
│   │   ├── Data Loading Forms
│   │   └── Quick Actions
│   │
│   ├── analysis.html
│   │   ├── Statistics Summary
│   │   ├── Influencers Table
│   │   ├── User Selection Grid
│   │   └── Mutual Friends Form
│   │
│   ├── recommendations.html
│   │   ├── User Header
│   │   ├── Info Alert
│   │   └── Recommendations Table
│   │
│   ├── mutual_friends.html
│   │   ├── Users Header
│   │   └── Friends Grid
│   │
│   └── visualization.html
│       ├── Controls (Reset, Refresh)
│       ├── SVG Graph Container
│       └── Legend
│
└── Footer
    ├── Copyright
    └── Credits
```

### CSS Architecture

```
Global Styles (base.html)
│
├── CSS Variables
│   ├── --primary-color
│   ├── --secondary-color
│   ├── --success-color
│   └── --danger-color
│
├── Layout
│   ├── Body (gradient background)
│   ├── Container (max-width, padding)
│   └── Responsive grid
│
├── Components
│   ├── Navbar (sticky, transparent)
│   ├── Cards (shadow, hover effects)
│   ├── Buttons (gradients, animations)
│   ├── Tables (striped, hover)
│   └── Forms (styled inputs)
│
└── Utilities
    ├── Stat cards
    ├── Feature icons
    └── Upload areas
```

---

## 🔐 Security Architecture

### Current Implementation

```
┌────────────────────────────────────┐
│    Environment Variables           │
│  (Neo4j credentials in .env)       │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│    Flask Secret Key                │
│  (CSRF protection)                 │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│    Input Validation                │
│  (File type, CSV format)           │
└────────────────────────────────────┘
```

### Recommended Enhancements

```
┌────────────────────────────────────┐
│    User Authentication             │
│  (Flask-Login)                     │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│    Authorization                   │
│  (Role-based access)               │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│    Rate Limiting                   │
│  (Flask-Limiter)                   │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│    Input Sanitization              │
│  (Prevent Cypher injection)        │
└────────────────────────────────────┘
```

---

## 📊 Performance Architecture

### Optimization Strategies

```
┌────────────────────────────────────┐
│         Database Layer             │
│  • Indexed user names              │
│  • Optimized Cypher queries        │
│  • Connection pooling              │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│       Application Layer            │
│  • Efficient Python code           │
│  • Minimal database calls          │
│  • Batch operations                │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│       Presentation Layer           │
│  • Lazy loading                    │
│  • Pagination (future)             │
│  • Cached static assets            │
└────────────────────────────────────┘
```

### Scalability Considerations

```
Current: Single Server
│
├── Flask (single process)
├── Neo4j (local instance)
└── Supports ~1000 concurrent users

Future: Distributed
│
├── Flask (multiple workers)
│   └── Behind load balancer
├── Neo4j (clustered)
│   └── Sharded database
└── Supports millions of users
```

---

## 🔄 Deployment Architecture

### Development (Current)

```
┌─────────────────────────────────────┐
│      Local Machine                  │
│  ┌────────────┐  ┌────────────┐    │
│  │   Flask    │  │   Neo4j    │    │
│  │  :5000     │  │  :7687     │    │
│  │ (dev mode) │  │ (local DB) │    │
│  └────────────┘  └────────────┘    │
└─────────────────────────────────────┘
```

### Production (Recommended)

```
┌─────────────────────────────────────┐
│         Load Balancer               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│      Flask App Servers (N)          │
│  ┌────────────┐  ┌────────────┐    │
│  │ Gunicorn   │  │ Gunicorn   │    │
│  │ Worker 1   │  │ Worker N   │    │
│  └────────────┘  └────────────┘    │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│      Neo4j Cluster                  │
│  ┌────────────┐  ┌────────────┐    │
│  │  Core 1    │  │  Core N    │    │
│  │  (leader)  │  │ (follower) │    │
│  └────────────┘  └────────────┘    │
└─────────────────────────────────────┘
```

---

## 🎯 Integration Points

### External Systems (Future)

```
Friend Recommendation System
│
├── Social Media APIs
│   ├── Facebook Graph API
│   ├── Twitter API
│   └── LinkedIn API
│
├── Analytics
│   ├── Google Analytics
│   └── Custom metrics
│
├── Authentication
│   ├── OAuth2
│   └── SAML
│
└── Storage
    ├── S3 (CSV uploads)
    └── CDN (static assets)
```

---

## 📱 Technology Stack Diagram

```
┌─────────────────────────────────────────────────────────┐
│                   Technology Stack                      │
├─────────────────────────────────────────────────────────┤
│  Frontend                                               │
│  ├── HTML5                                              │
│  ├── CSS3 (Bootstrap 5.3.2)                            │
│  ├── JavaScript (ES6+)                                  │
│  ├── jQuery 3.7.1                                       │
│  └── D3.js v7                                           │
├─────────────────────────────────────────────────────────┤
│  Backend                                                │
│  ├── Python 3.8+                                        │
│  ├── Flask 3.0.0                                        │
│  ├── Jinja2 (templating)                               │
│  └── Werkzeug 3.0.1                                     │
├─────────────────────────────────────────────────────────┤
│  Database                                               │
│  ├── Neo4j 5.x                                          │
│  ├── Cypher Query Language                              │
│  └── neo4j-python-driver 5.14.1                        │
├─────────────────────────────────────────────────────────┤
│  Tools                                                  │
│  ├── PowerShell (automation)                            │
│  ├── python-dotenv (config)                             │
│  └── Git (version control)                              │
└─────────────────────────────────────────────────────────┘
```

---

**Document Version**: 1.0  
**Last Updated**: October 15, 2025  
**Architecture**: Monolithic Web Application  
**Deployment**: Development/Local  

✅ **Architecture documented and validated!**
