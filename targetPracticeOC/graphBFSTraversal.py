from collections import deque
def bfs(origin):
    visited  = set([origin.id])
    queue = deque([origin])
    ans = ""
    while queue:
      cur = queue.popleft()
      ans +=cur.id
      for elem in cur.edges:
        if elem.id not in visited:
          queue.append(elem)
          visited.add(elem.id)
    return ans