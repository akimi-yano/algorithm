graph = {
    1: [2, 3, 4],
    2: [5],
    3: [],
    4: [6, 7],
    5: [],
    6: [3],
    7: []
}
start = 1

def graphBFS(graph, start):
    queue = [start]
    visited = set([])
    # enqueue() -> append()
    # dequeue() -> pop(0)
    while len(queue) > 0:
        current = queue.pop(0)
        visited.add(current)
        print(current)    
        for i in range(len(graph[current])):
            if graph[current][i] not in visited:
                queue.append(graph[current][i])
                
graphBFS(graph, start)