import heapq

# --- SRIKAKULAM LOGISTICS PROJECT: FINAL VERSION ---
# I mapped these towns based on the main road distances in my district.
# Using a Dictionary (Adjacency List) to represent the graph.

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

# This is my implementation of Dijkstra's Algorithm.
# I used heapq because it makes the search faster by always picking the smallest distance.
def find_best_route(graph, start, end):
    
    # Initialize all distances to infinity first
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority Queue stores: (total_km, town_name)
    pq = [(0, start)]
    
    while pq:
        curr_km, curr_node = heapq.heappop(pq)

        # Stop if we reached our target town
        if curr_node == end:
            return curr_km

        # Check neighbors and update distances if a shorter path is found
        for neighbor, weight in graph[curr_node].items():
            path = curr_km + weight
            
            if path < distances[neighbor]:
                distances[neighbor] = path
                heapq.heappush(pq, (path, neighbor))
                
    return None

# --- TERMINAL INTERFACE ---
print("========================================")
print("   SRIKAKULAM ROUTE OPTIMIZER v1.0")
print("========================================")
print("Available Cities: Srikakulam_City, Narasannapeta, Tekkali, Palasa, Rajam, Ponduru, Customer_Point")

# Getting pickup and delivery points from user
p_up = input("\nEnter Pickup Point: ")
d_off = input("Enter Delivery Point: ")

# Checking if inputs exist in our map
if p_up in road_data and d_off in road_data:
    final_km = find_best_route(road_data, p_up, d_off)
    
    if final_km:
        print(f"\n[SCANNING] Route optimized successfully!")
        print(f"[RESULT] Shortest Distance: {final_km} KM")
        
        # --- FUEL CALCULATOR ---
        # I used Rs 110/L for AP petrol price and assumed 15km/L mileage.
        cost = round((final_km / 15) * 110, 2)
        print(f"[ECONOMY] Estimated Fuel Cost: Rs. {cost}")
    else:
        print("\n[ALERT] I couldn't find a connecting route between those towns.")
else:
    print("\n[ERROR] Spelling mistake! Please use the city names as shown above.")