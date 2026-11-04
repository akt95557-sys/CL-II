import numpy as np
import networkx as nx

# 1. Define the Web Graph (Adjacency Matrix / Directed Edges)
# Edges representing incoming and outgoing links between 4 Webpages (A, B, C, D)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'C')]

# 2. Build Directed Graph using NetworkX
G = nx.DiGraph()
G.add_edges_from(edges)

# 3. Calculate PageRank Scores (Standard Damping Factor d = 0.85)
pagerank_scores = nx.pagerank(G, alpha=0.85)

# 4. Display PageRank Scores for Each Webpage
print("--- PAGERANK SCORES ---")
for node, score in sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"Page {node} : {score:.4f}")

# 5. Display Highest Ranked Page
highest_page = max(pagerank_scores, key=pagerank_scores.get)
print(f"\nMost Important Page: Page {highest_page}")
