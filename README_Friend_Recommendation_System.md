
# Friend Recommendation System Using Social Network Analysis

## Introduction
This project implements a basic Friend Recommendation System using Social Network Analysis. By leveraging graph theory concepts, the system identifies potential friends for users in a social network based on the number of common neighbors.

## Features
- Suggests friends based on shared connections (common neighbors).
- Visualizes the social network graph with recommendations.
- Implements a simple and scalable algorithm using Python's NetworkX library.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: NetworkX, Matplotlib
- **Dataset**: Synthetic graph dataset (can be replaced with real-world datasets)

## How It Works
1. **Graph Construction**: Nodes represent users, and edges represent friendships.
2. **Recommendation Algorithm**: 
   - Calculates the number of common neighbors for each pair of users.
   - Ranks potential friends based on the number of shared connections.
3. **Visualization**: Displays the social network and highlights existing connections.

## Setup and Usage
1. Clone this repository to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install networkx matplotlib
   ```
3. Run the Python script to generate recommendations and visualize the graph:
   ```bash
   python friend_recommendation.py
   ```

## Example Output
For a given user in the network (e.g., Node 1), the system outputs potential friend recommendations:
```
Friend recommendations for Node 1:
Node 5 (Common Neighbors: 2)
Node 6 (Common Neighbors: 1)
```
A graph visualization is also displayed.

## Future Enhancements
- Integrate real-world datasets using APIs like Twitter or Facebook.
- Use advanced metrics (e.g., Jaccard similarity, Adamic-Adar index).
- Build a web or mobile interface for live interaction.

## References
1. NetworkX Documentation: [https://networkx.org/](https://networkx.org/)
2. SNAP Datasets: [http://snap.stanford.edu/data/](http://snap.stanford.edu/data/)
3. Social Network Analysis Book: Wasserman, S., & Faust, K. (1994). *Social Network Analysis: Methods and Applications*.

---
Developed as a 4th-year college project.
