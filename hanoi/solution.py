def towers_str(towers):
    """
    Print towers.
    """
    height = max([len(tower) for tower in towers])
    max_ring = max([max(tower, default=0) for tower in towers])

    towers_lines = []
    for i in range(height):
        towers_line = []
        for tower in towers:
            tower_line = []
            if i >= len(tower):
                tower_line += [' ' for _ in range(max_ring)]
                tower_line += '|'
                tower_line += [' ' for _ in range(max_ring)]
            else:
                ring_size = tower[i]
                tower_line += [' ' for _ in range(max_ring - ring_size)]
                tower_line += ['=' for _ in range(ring_size)]
                tower_line += '|'
                tower_line += ['=' for _ in range(ring_size)]
                tower_line += [' ' for _ in range(max_ring - ring_size)]
            towers_line.append(''.join(tower_line))
        towers_lines.append(' '.join(towers_line))
    
    towers_str = ''
    while len(towers_lines) > 0:
        towers_str += towers_lines.pop() + '\n'
    return towers_str


def hanoi(towers, n, source, destination, temp):
    """
    Move tower of Hanoi from source to destination.

    towers: list of towers. Each tower is a list of numbers that represent the ring size.
            ex: [[3, 2, 1], [], []]
    n: number of rings to move from source to destination
    source: the position in towers to move the rings from
    destination: the position in towers to move the rings to
    temp: temporary position in towers
    """
    if n == 1:
        print(f"hanoi(n={n}) Moving ring...\n" + towers_str(towers))
        ring = towers[source].pop()
        towers[destination].append(ring)
        print(f"hanoi(n={n}) Moved ring...\n" + towers_str(towers))
        return 
    else:
        hanoi(towers, n-1, source, temp, destination)
        print(f"hanoi(n={n}) Moving ring...\n" + towers_str(towers))
        ring = towers[source].pop()
        towers[destination].append(ring)
        print(f"hanoi(n={n}) Moved ring...\n" + towers_str(towers))
        hanoi(towers, n-1, temp, destination, source)


# NEVER DO OVER 10!!!!
tower_size = 3
towers = [[i for i in range(tower_size, 0, -1)], [], []]
print("Before moving:\n" + towers_str(towers))
hanoi(towers, tower_size, 0, 1, 2)
print("After moving:\n" + towers_str(towers))