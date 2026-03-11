import heapq

# --- MY PROJECT: SRIKAKULAM DELIVERY ROUTE OPTIMIZER ---
# Road network is now fully mapped.
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

# --- ADDING THE LOGIC IN PART 2 ---
# Implementing Dijkstra Algorithm using a Priority Queue (heapq)
def find_best_route(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)] # Min-heap to pick the shortest path next
    
    while pq:
        curr_km, curr_node = heapq.heappop(pq)

        if curr_node == end:
            return curr_km

        for neighbor, weight in graph[curr_node].items():
            path = curr_km + weight
            if path < distances[neighbor]:
                distances[neighbor] = path
                heapq.heappush(pq, (path, neighbor))

    return "No Route"

print("--- Step 2: Pathfinding Logic Implemented ---")
# Testing the logic internally
test_dist = find_best_route(road_data, 'Srikakulam_City', 'Palasa')
print(f"Test Run (Srikakulam to Palasa): {test_dist} KM")