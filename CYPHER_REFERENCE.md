# Neo4j Cypher Queries Reference

This document explains all the Cypher queries used in the Friend Recommendation System.

## 📚 Table of Contents
1. [Basic Operations](#basic-operations)
2. [Data Loading](#data-loading)
3. [Analysis Queries](#analysis-queries)
4. [Visualization Queries](#visualization-queries)

---

## Basic Operations

### Clear Database
```cypher
MATCH (n) DETACH DELETE n
```
**Purpose**: Delete all nodes and relationships  
**Use Case**: Reset database before loading new data

---

## Data Loading

### Create Users and Friendships
```cypher
MERGE (u1:User {name: $user1})
MERGE (u2:User {name: $user2})
MERGE (u1)-[:FRIENDS_WITH]->(u2)
MERGE (u2)-[:FRIENDS_WITH]->(u1)
```
**Parameters**:
- `$user1`: First user's name
- `$user2`: Second user's name

**Purpose**: Create bidirectional friendship between two users  
**Notes**: 
- `MERGE` ensures no duplicates
- Bidirectional relationships for undirected friendship graph

---

## Analysis Queries

### 1. Friend Recommendations (Friends-of-Friends)

```cypher
MATCH (user:User {name: $user_name})-[:FRIENDS_WITH]->(friend)-[:FRIENDS_WITH]->(foaf)
WHERE NOT (user)-[:FRIENDS_WITH]->(foaf) AND user <> foaf
WITH foaf, COUNT(DISTINCT friend) AS mutual_friends
RETURN foaf.name AS recommended_friend, mutual_friends
ORDER BY mutual_friends DESC
LIMIT $limit
```

**Parameters**:
- `$user_name`: Target user
- `$limit`: Maximum recommendations

**Algorithm Explanation**:
1. Start from target user
2. Follow FRIENDS_WITH to direct friends
3. Follow FRIENDS_WITH again to friends-of-friends (foaf)
4. Filter out existing friends and self
5. Count mutual connections
6. Return top N recommendations

**Example**:
- Alice → Bob → Charlie
- Alice → David → Charlie
- Charlie is recommended to Alice with 2 mutual friends (Bob, David)

**Time Complexity**: O(n²) where n = average friends per user

---

### 2. Mutual Friends Finder

```cypher
MATCH (u1:User {name: $user1})-[:FRIENDS_WITH]->(mutual)<-[:FRIENDS_WITH]-(u2:User {name: $user2})
RETURN mutual.name AS mutual_friend
ORDER BY mutual_friend
```

**Parameters**:
- `$user1`: First user
- `$user2`: Second user

**Algorithm Explanation**:
1. Find paths from user1 → mutual friend
2. Find paths from user2 → mutual friend
3. Return intersection (common friends)

**Graph Pattern**:
```
(user1) → (mutual) ← (user2)
```

---

### 3. Influencer Detection

```cypher
MATCH (user:User)-[r:FRIENDS_WITH]->()
WITH user, COUNT(r) AS connections
RETURN user.name AS name, connections
ORDER BY connections DESC
LIMIT $limit
```

**Parameters**:
- `$limit`: Number of top influencers

**Algorithm Explanation**:
1. Match all users with outgoing FRIENDS_WITH relationships
2. Count connections per user
3. Sort by connection count descending
4. Return top N users

**Metric**: Degree Centrality (number of direct connections)

---

### 4. Get All Users

```cypher
MATCH (u:User) 
RETURN u.name AS name 
ORDER BY name
```

**Purpose**: List all users alphabetically  
**Use Case**: Populate dropdowns, user selection

---

### 5. Database Statistics

#### Total Users
```cypher
MATCH (u:User) 
RETURN COUNT(u) AS count
```

#### Total Connections
```cypher
MATCH ()-[r:FRIENDS_WITH]->() 
RETURN COUNT(r) AS count
```
**Note**: Divide by 2 for undirected graph (bidirectional relationships)

---

## Visualization Queries

### Get All Relationships (for Graph Display)

```cypher
MATCH (u1:User)-[r:FRIENDS_WITH]->(u2:User)
WHERE ID(u1) < ID(u2)
RETURN u1.name AS source, u2.name AS target
```

**Purpose**: Get unique edges for visualization  
**Notes**: 
- `ID(u1) < ID(u2)` ensures each relationship returned once
- Avoids duplicate edges in undirected graph

---

### Get Users with Connection Counts

```cypher
MATCH (u:User)-[r:FRIENDS_WITH]->()
WITH u, COUNT(r) AS connections
RETURN u.name AS name, connections
ORDER BY connections DESC
```

**Purpose**: Size nodes by connection count in visualization

---

## Query Optimization Tips

### 1. Use Indexes
```cypher
CREATE INDEX user_name_index FOR (u:User) ON (u.name)
```

### 2. Profile Queries
```cypher
PROFILE MATCH (user:User {name: 'Alice'})-[:FRIENDS_WITH]->(friend)
RETURN friend.name
```

### 3. Explain Query Plan
```cypher
EXPLAIN MATCH (user:User {name: 'Alice'})-[:FRIENDS_WITH*2]-(foaf)
RETURN foaf.name
```

---

## Advanced Patterns

### Find Shortest Path Between Users
```cypher
MATCH path = shortestPath(
  (u1:User {name: $user1})-[:FRIENDS_WITH*]-(u2:User {name: $user2})
)
RETURN length(path) AS degrees_of_separation, 
       [node in nodes(path) | node.name] AS path
```

### Community Detection (Connected Components)
```cypher
CALL gds.wcc.stream('myGraph')
YIELD nodeId, componentId
RETURN gds.util.asNode(nodeId).name AS name, componentId
ORDER BY componentId, name
```
**Note**: Requires Neo4j Graph Data Science library

### PageRank for Influence
```cypher
CALL gds.pageRank.stream('myGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC
LIMIT 10
```

---

## Performance Considerations

### Query Performance by Operation

| Query | Typical Time | Complexity |
|-------|-------------|------------|
| Get All Users | <10ms | O(n) |
| Influencer Detection | <50ms | O(n) |
| Mutual Friends | <20ms | O(k²) |
| Friend Recommendations | <100ms | O(n²) |
| Graph Visualization | <200ms | O(n + e) |

*n = nodes, e = edges, k = avg connections*

### Scaling Tips
1. **Index user names** for faster lookups
2. **Limit result sets** to avoid memory issues
3. **Use PROFILE** to identify bottlenecks
4. **Consider pagination** for large datasets

---

## Testing Queries in Neo4j Browser

Access Neo4j Browser: `http://localhost:7474`

### Test Friend Recommendations
```cypher
// Create test data
MERGE (a:User {name: 'Alice'})
MERGE (b:User {name: 'Bob'})
MERGE (c:User {name: 'Charlie'})
MERGE (d:User {name: 'David'})
MERGE (a)-[:FRIENDS_WITH]->(b)
MERGE (b)-[:FRIENDS_WITH]->(c)
MERGE (b)-[:FRIENDS_WITH]->(d);

// Get recommendations for Alice
MATCH (user:User {name: 'Alice'})-[:FRIENDS_WITH]->(friend)-[:FRIENDS_WITH]->(foaf)
WHERE NOT (user)-[:FRIENDS_WITH]->(foaf) AND user <> foaf
WITH foaf, COUNT(DISTINCT friend) AS mutual_friends
RETURN foaf.name, mutual_friends
ORDER BY mutual_friends DESC;
```

---

## Resources

- **Cypher Manual**: https://neo4j.com/docs/cypher-manual/
- **Cypher Refcard**: https://neo4j.com/docs/cypher-refcard/
- **Graph Algorithms**: https://neo4j.com/docs/graph-data-science/

---

**Note**: All queries in this document are used in `app.py`. Modify them carefully to maintain functionality.
