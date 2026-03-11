# Srikakulam Route Optimizer

### What is this?
I built this Python tool to solve delivery route problems in my home district, Srikakulam. It uses **Dijkstra's Algorithm** to find the shortest distance between towns and even calculates the fuel cost.

### How it works:
* **The Brain:** I used the `heapq` library to implement a Priority Queue. This makes the Dijkstra search very fast.
* **The Map:** I created a dictionary (Adjacency List) of towns like Palasa, Tekkali, and Rajam with their real distances.
* **Fuel Math:** It calculates the cost based on Rs. 110/L (current price in AP) and a 15km/L mileage.

### My Progress:
- [x] Mapped Srikakulam road network.
- [x] Finished Dijkstra logic.
- [x] Added User Input and Fuel Cost features.

### How to use:
Just run `main.py` and type the town names exactly as they appear in the list.