# --- STEP 1: THE MAP ---
# This is an 'Adjacency List'. Each city points to its neighbors and the distance.

graph = {
    'Warehouse': {'Point_A': 5, 'Point_B': 2},
    'Point_A': {'Warehouse': 5, 'Point_C': 4, 'Point_D': 2},
    'Point_B': {'Warehouse': 2, 'Point_D': 7},
    'Point_C': {'Point_A': 4, 'Customer': 3},
    'Point_D': {'Point_A': 2, 'Point_B': 7, 'Customer': 1},
    'Customer': {'Point_C': 3, 'Point_D': 1}
}

print("--- Logistics System: Initialized ---")
print("Available routes from Warehouse:", graph['Warehouse'])