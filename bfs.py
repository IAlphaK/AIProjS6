import networkx as nx

def printPath(graph, start, goals):
    queue = []
    visited = set()
    queue.append((start, [start]))  # Store the node and its path
    visited.add(start)

    traversal_path = []  # Store the complete traversal path

    path_graph = nx.Graph()  # Create an empty graph to store the path

    while queue:
        node, path = queue.pop(0)
        traversal_path.append(node)  # Store the visited node in the traversal path
        path_graph.add_node(node)  # Add the visited node to the path graph

        if node in goals:
            for i in range(len(path) - 1):
                source = path[i]
                target = path[i + 1]
                weight = graph.get_edge_data(source, target)['w']
                path_graph.add_edge(source, target, weight=weight)
            return traversal_path, path_graph.subgraph(traversal_path)  # Return the complete traversal path and the subgraph

        neighbors = graph.neighbors(node)  # Get the neighbors of the current node from the graph

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  # Update the path
                visited.add(neighbor)
                weight = graph.get_edge_data(node, neighbor)['w']  # Get the weight of the edge
                path_graph.add_edge(node, neighbor, weight=weight)  # Add the edge with its weight to the path graph

    # If goal node is not found, return None or a custom value
    return None, None