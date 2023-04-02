import matplotlib.pyplot as plt
import networkx as nx

def plot_network1():
    network = nx.Graph()
    network.add_nodes_from([1,2,3,4,5,6,7,8,9,10]) 

    # Add region names to nodes
    region_names = {
        1: "2",
        2: "2.1",
        3: "2.1.1",
        4: "2.2",
        5: "2.2.1",
        6: "2.3",
        7: "2.3.1",
        8: "2.3.2",
        9: "2.4",
        10: "2.4.1"
    }
    nx.set_node_attributes(network, region_names, "region")
    print(f"This network has now {network.number_of_nodes()} nodes.")
    network.add_edge(1, 2, weight=1)
    network.add_edge(2, 3, weight=2)

    network.add_edge(1, 4, weight=1)
    network.add_edge(4, 5, weight=2)

    network.add_edge(1, 6, weight=1)
    network.add_edge(6, 7, weight=2)
    network.add_edge(6, 8, weight=2)
    network.add_edge(6, 8, weight=2)
    network.add_edge(7, 8, weight=3)

    network.add_edge(1, 9, weight=1)
    network.add_edge(9, 10, weight=2)

    color_list = ["Yellow","Yellow","Yellow","Yellow","Yellow","Yellow","Yellow","Yellow","Yellow","Yellow"]
    plt.figure(figsize=(20, 20))
    plt.title("EV charger in Thailand (North)", size=14)
    pos = {
        1: (0, 0),
        2: (-2, 1),
        3: (-2, 2),
        4: (-1, 1),
        5: (-1, 2),
        6: (1, 1),
        7: (1, 2),
        8: (1, 3),
        9: (2, 1),
        10: (2, 2)
    }

    # Draw the network graph with edges and nodes
    nx.draw_networkx(network, node_color=color_list, with_labels=False, pos=pos)

    # Draw edge labels
    edge_labels = {(u,v):d['weight'] for u,v,d in network.edges(data=True)}
    nx.draw_networkx_edge_labels(network, pos=pos, edge_labels=edge_labels, font_size=12, font_color="black", font_family="sans-serif")

    # Draw node labels at fixed positions
    node_labels = nx.get_node_attributes(network, "region")
    nx.draw_networkx_labels(network, pos=pos, labels=node_labels, font_size=16, font_color="black", font_family="serif")

    plt.show()

    source = int(input("Enter the source node: "))
    target = int(input("Enter the target node: "))
    shortest_path = nx.shortest_path(network, source=source, target=target)
    print(f"Shortest path from node {source} to node {target}: {shortest_path}")

def plot_network2():
    network = nx.Graph()
    network.add_nodes_from([1,2,3,4,5,6,7,8,9])

    # Add region names to nodes
    region_names = {
        1: "3",
        2: "3.1",
        3: "3.1.1",
        4: "3.1.2",
        5: "3.2",
        6: "3.2.1",
        7: "3.3",
        8: "3.3.1",
        9: "3.3.2",
    }
    nx.set_node_attributes(network, region_names, "region")
    print(f"This network has now {network.number_of_nodes()} nodes.")
    network.add_edge(1, 2, weight=1)
    network.add_edge(2, 3, weight=2)
    network.add_edge(3, 4, weight=3)

    network.add_edge(1, 5, weight=1)
    network.add_edge(5, 6, weight=2)

    network.add_edge(1, 7, weight=1)
    network.add_edge(7, 8, weight=2)
    network.add_edge(8, 9, weight=3)

    color_list = ["Cyan","Cyan","Cyan","Cyan","Cyan","Cyan","Cyan","Cyan","Cyan"]
    plt.figure(figsize=(20, 20))
    plt.title("EV charger in Thailand (Northeast)", size=14)
    pos = {
    1: (0, 0),
    2: (1, 1),
    3: (2, 1),
    4: (3, 1),

    5: (1, 0),
    6: (2, 0),

    7: (1, -1),
    8: (2, -1),
    9: (3, -1)
    
    }

    # Draw the network graph with edges and nodes
    nx.draw_networkx(network, node_color=color_list, with_labels=False, pos=pos)

    # Draw edge labels
    edge_labels = {(u,v):d['weight'] for u,v,d in network.edges(data=True)}
    nx.draw_networkx_edge_labels(network, pos=pos, edge_labels=edge_labels, font_size=12, font_color="black", font_family="sans-serif")

    # Draw node labels at fixed positions
    node_labels = nx.get_node_attributes(network, "region")
    nx.draw_networkx_labels(network, pos=pos, labels=node_labels, font_size=16, font_color="black", font_family="serif")

    plt.show()

    source = int(input("Enter the source node: "))
    target = int(input("Enter the target node: "))
    shortest_path = nx.shortest_path(network, source=source, target=target)
    print(f"Shortest path from node {source} to node {target}: {shortest_path}")

def plot_network3():
    network = nx.Graph()
    network.add_nodes_from([1,2,3,4,5,6,7])

    # Add region names to nodes
    region_names = {
        1: "1",
        2: "1.1",
        3: "1.1.1",
        4: "1.1.2",
        5: "1.1.3",
        6: "1.1.4",
        7: "1.1.5",
    }
    nx.set_node_attributes(network, region_names, "region")
    print(f"This network has now {network.number_of_nodes()} nodes.")
    network.add_edge(1, 2, weight=1)
    network.add_edge(2, 3, weight=1)
    network.add_edge(2, 4, weight=1)

    network.add_edge(2, 5, weight=1)
    network.add_edge(2, 6, weight=1)
    network.add_edge(2, 7, weight=1)

    color_list = ["Red","Red","Red","Red","Red","Red","Red"]
    plt.figure(figsize=(20, 20))
    plt.title("EV charger in Thailand (Central)", size=14)
    pos = {
    1: (0, 0),
    2: (-1, 0),
    3: (-2, -2),
    4: (-2, -1),
    5: (-2, 0),
    6: (-2, 1),
    7: (-2, 2),
    }

    # Draw the network graph with edges and nodes
    nx.draw_networkx(network, node_color=color_list, with_labels=False, pos=pos)

    # Draw edge labels
    edge_labels = {(u,v):d['weight'] for u,v,d in network.edges(data=True)}
    nx.draw_networkx_edge_labels(network, pos=pos, edge_labels=edge_labels, font_size=12, font_color="black", font_family="sans-serif")

    # Draw node labels at fixed positions
    node_labels = nx.get_node_attributes(network, "region")
    nx.draw_networkx_labels(network, pos=pos, labels=node_labels, font_size=16, font_color="black", font_family="serif")

    plt.show()

    source = int(input("Enter the source node: "))
    target = int(input("Enter the target node: "))
    shortest_path = nx.shortest_path(network, source=source, target=target)
    print(f"Shortest path from node {source} to node {target}: {shortest_path}")

def plot_network4():
    network = nx.Graph()
    network.add_nodes_from([1,2,3,4,5,6,7,8,9])

    # Add region names to nodes
    region_names = {
        1: "4",
        2: "4.1",
        3: "4.1.1",
        4: "4.2",
        5: "4.2.1",
        6: "4.3",
        7: "4.3.1",
        8: "4.3.2",
        9: "4.3.4",
    }
    nx.set_node_attributes(network, region_names, "region")
    print(f"This network has now {network.number_of_nodes()} nodes.")
    network.add_edge(1, 2,weight=1)
    network.add_edge(2, 3,weight=5)

    network.add_edge(1, 4,weight=1)
    network.add_edge(4, 5,weight=2)

    network.add_edge(1, 6,weight=1)
    network.add_edge(6, 7,weight=2)
    network.add_edge(7, 8,weight=3)
    network.add_edge(8, 9,weight=4)

    color_list = ["limegreen","limegreen","limegreen","limegreen","limegreen","limegreen","limegreen","limegreen","limegreen"]
    plt.figure(figsize=(20, 20))
    plt.title("EV charger in Thailand (South)", size=14)
    pos = {
    1: (0, 0),
    2: (-1, -1),
    3: (-1, -2),

    4: (0, -1),
    5: (0, -2),

    6: (1, -1),
    7: (1, -2),
    8: (1, -3),
    9: (1, -4)
    }

    # Draw the network graph with edges and nodes
    nx.draw_networkx(network, node_color=color_list, with_labels=False, pos=pos)

    # Draw edge labels
    edge_labels = {(u,v):d['weight'] for u,v,d in network.edges(data=True)}
    nx.draw_networkx_edge_labels(network, pos=pos, edge_labels=edge_labels, font_size=12, font_color="black", font_family="sans-serif")

    # Draw node labels at fixed positions
    node_labels = nx.get_node_attributes(network, "region")
    nx.draw_networkx_labels(network, pos=pos, labels=node_labels, font_size=16, font_color="black", font_family="serif")

    plt.show()

    source = int(input("Enter the source node: "))
    target = int(input("Enter the target node: "))
    shortest_path = nx.shortest_path(network, source=source, target=target)
    print(f"Shortest path from node {source} to node {target}: {shortest_path}")


print("Which region would you like to show?")
print("1. North")
print("2. Northeast")
print("3. Central")
print("4. South")
choice = input("Enter the number of your choice: ")

if choice == "1":
    plot_network1()
elif choice == "2":
    plot_network2()
elif choice == "3":
    plot_network3()
elif choice == "4":
    plot_network4()
else:
    print("Invalid choice.")
