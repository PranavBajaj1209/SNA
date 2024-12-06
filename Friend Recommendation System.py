import networkx as nx

# Create a sample graph
G = nx.Graph()

# Add edges (connections between users)
edges = [
    (1, 2), (1, 3), (2, 4), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 7)
]
G.add_edges_from(edges)

# Function for friend recommendation based on common neighbors
def recommend_friends(graph, node):
    if node not in graph:
        return f"Node {node} is not in the graph."
    
    # Find friends of the node
    friends = set(graph.neighbors(node))
    # Find potential friends (common neighbors)
    recommendations = {}
    
    for potential_friend in graph.nodes:
        if potential_friend != node and potential_friend not in friends:
            # Count common neighbors
            common_neighbors = len(list(nx.common_neighbors(graph, node, potential_friend)))
            if common_neighbors > 0:
                recommendations[potential_friend] = common_neighbors
    
    # Sort by the number of common neighbors
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations

# Test the recommendation function
node_to_recommend = 1
recommendations = recommend_friends(G, node_to_recommend)

print(f"Friend recommendations for node {node_to_recommend}:")
for friend, score in recommendations:
    print(f"Node {friend} (Common Neighbors: {score})")

# Visualize the graph (optional)
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.show()
