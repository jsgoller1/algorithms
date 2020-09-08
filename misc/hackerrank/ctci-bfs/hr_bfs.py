from collections import deque

class Graph():
    def __init__(self, node_count):
        self.nodes = {}
        for i in range(node_count):
            self.nodes[i] = []

    def connect(self, a, b):
        self.nodes[a].append(b)
        self.nodes[b].append(a)

    def find_all_distances(self, label):
        original_label = label
        distance = 0
        paths = {}
        q = deque([(label, distance, self.nodes[label])])

        while(q and distance < 100):
            label, distance, neighbors = q.popleft()
            print("Evaluating: "+ str(label))
            if label in paths:
                paths[label] = min(distance, paths[label]) # todo: is this necessary?
            else:
                paths[label] = distance
            for neighbor in neighbors:
                if neighbor not in paths: # prevent cycles
                    q.append((neighbor, distance + 6, self.nodes[neighbor]))

        # Process output
        for node in self.nodes:
            if node not in paths:
                paths[node] = -1
        del paths[original_label]
        return [paths[node] for node in paths]


def test_fad():
    g = Graph(6)
    g.connect(0, 1)
    g.connect(1, 2)
    g.connect(1, 3)
    print(g.find_all_distances(0))

# tests graph and node construction
def test_graph():
    g = Graph(5)
    print(g)
    print(g.nodes)


# Tests connect() and add_child()
def test_connect():
    g = Graph(2)
    g.connect(0, 1)
    a = g.nodes[0]
    b = g.nodes[1]
    print(a)
    print(b)


#test_graph()
#test_connect()
#test_fad()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            graph.connect(x-1,y-1)
        s = int(input())
        print(*graph.find_all_distances(s-1))
