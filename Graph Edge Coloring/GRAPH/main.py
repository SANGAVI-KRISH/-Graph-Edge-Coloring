from EdgeColoring.GraphStructure.graph import show
from EdgeColoring.GraphStructure.color import func
from EdgeColoring.GraphStructure.color import graph

n = int(input("Enter Number of Nodes: "))

print("1. Complete Graph\n2. Cycle Graph\n3. Star Graph\n4. Fan Graph\n5. Sibling Graph\n6. Binary Graph\n7. Path Graph")
k = int(input("Enter Graph Number: "))


graph_input = show(n, k)

graph(graph_input)