import networkx as nx
import matplotlib.pyplot as plt
import time  # Import the time module

def edge_coloring(graph_dict):
    G = nx.Graph()

    # Add edges to the graph
    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    color_map = {}
    colors_used = set()

    # A dictionary to track the colors used by each node
    node_colors = {node: set() for node in G.nodes()}

    # Assign colors to edges
    for edge in G.edges():
        # Get the colors already used by edges incident to the same nodes
        node1, node2 = edge
        neighbor_colors = node_colors[node1].union(node_colors[node2])
        
        # Assign the smallest color that is not in the neighbor colors
        color = 0
        while color in neighbor_colors:
            color += 1
        
        # Assign the color to the edge
        color_map[edge] = color
        colors_used.add(color)

        # Update the colors used by the nodes
        node_colors[node1].add(color)
        node_colors[node2].add(color)

    return color_map, len(colors_used), G

def visualize_graph(graph, color_map):
    """Visualizes the graph with colored edges."""
    edge_colors = [color_map[edge] for edge in graph.edges()]
    
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, edge_color=edge_colors, width=2.0, node_size=700, node_color='lightblue', font_size=15)
    
    plt.title("Edge Coloring Visualization")
    plt.show()
    return

def func(graph_input):
    color_map, num_colors, G = edge_coloring(graph_input)

    print("Number of colors used:", num_colors)

    visualize_graph(G, color_map)
    return

def graph(graph_input):
    start_time = time.time()  # Record the start time
    func(graph_input)  # Call the func function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the time difference
    print(f"Execution time: {execution_time:.6f} seconds")
    return