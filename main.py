# --- SRIKAKULAM DISTRICT LOGISTICS PROJECT ---
# I started by mapping the towns and distances in my home district.
# Using a dictionary to represent the graph (Adjacency List).

road_data = {
    'Srikakulam_City': {'Narasannapeta': 25, 'Amadalavalasa': 15},
    'Amadalavalasa': {'Srikakulam_City': 15, 'Rajam': 35},
    'Narasannapeta': {'Srikakulam_City': 25, 'Tekkali': 30, 'Kotabommali': 20},
    'Tekkali': {'Narasannapeta': 30, 'Palasa': 40, 'Pathapatnam': 25},
    'Palasa': {'Tekkali': 40, 'Ichchapuram': 35, 'Customer_Point': 10},
    'Kotabommali': {'Narasannapeta': 20, 'Palasa': 45},
    'Rajam': {'Amadalavalasa': 35, 'Ponduru': 20},
    'Ponduru': {'Rajam': 20}, 
    'Pathapatnam': {'Tekkali': 25},
    'Ichchapuram': {'Palasa': 35},
    'Customer_Point': {'Palasa': 10}
}

print("--- LOGISTICS OPTIMIZER (Initial Setup) ---")
print("Successfully mapped", len(road_data), "local towns.")
print("Next step: Implement Dijkstra logic for shortest path.")