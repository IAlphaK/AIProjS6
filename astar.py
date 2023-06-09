import networkx as nx
import heapq

def printPath(graph, start_state, goal_states, heuristic):
    visited = set()
    queue = [(heuristic(start_state), 0, start_state, [])]  # (priority, cost, current_node, path)

    traversal_path = []  # Store the complete traversal path
    path_graph = nx.Graph()  # Create an empty graph to store the path
    path_graph.add_node(start_state)  # Add the start node to the traversal graph

    while queue:
        _, cost, current_state, path = heapq.heappop(queue)

        if current_state in visited:
            continue

        visited.add(current_state)
        path.append(current_state)
        traversal_path.append(current_state)
        path_graph.add_node(current_state)  # Add the current state to the traversal graph

        if current_state in goal_states:
            for i in range(len(path) - 1):
                source = path[i]
                target = path[i + 1]
                weight = int(graph.get_edge_data(source, target)['w'])  # Convert weight to int
                path_graph.add_edge(source, target, weight=weight)
            return path, path_graph.subgraph(path)  # Return the traversal path and the subgraph

        if current_state in graph:
            neighbors = graph[current_state]
            for neighbor_state, edge_data in neighbors.items():
                if neighbor_state not in visited:
                    new_cost = cost + int(edge_data['w'])  # Convert weight to int
                    priority = new_cost + heuristic(neighbor_state)
                    heapq.heappush(queue, (priority, new_cost, neighbor_state, path[:]))
                    path_graph.add_edge(current_state, neighbor_state, weight=int(edge_data['w']))  # Convert weight to int and add the edge to the traversal graph

    return None, None  # No path found, return an empty path and empty graph
