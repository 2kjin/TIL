stack = []
stack.append()
visited = set()
visited = add(s)
while stack:
    value = stack[-1]

    for next in Graph(value):
        if next not in visited:
            visited.add(next)
            stack.append(next)
            break
    else:
