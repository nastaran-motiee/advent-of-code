def part_1_2(m_input_path):
    a, b = open(m_input_path).read().split('\n')
    a, b = [x.split(',') for x in [a, b]]

    a_points = f_wire_points(a)
    b_points = f_wire_points(b)

    mutual = set(a_points) & set(b_points)
    m_distance = float('inf')
    m_steps = float('inf')

    for point in mutual:
        dis = abs(point[0]) + abs(point[1])  # for part 1
        if dis < m_distance:
            m_distance = dis

    for point in mutual:
        t_st = 0
        for p in a_points:
            t_st += 1
            if p == point:
                break
        for p in b_points:
            t_st += 1
            if p == point:
                break

        if t_st < m_steps:
            m_steps = t_st

    return f"part 1: {m_distance} ,part 2: {m_steps}"


def f_wire_points(wire):
    wire_loc = {'x': 0, 'y': 0}
    wire_points = []
    for d in wire:
        direction = d[0]
        n = int(d[1:])

        match direction:
            case 'R':
                for _ in range(n):
                    wire_loc['x'] += 1
                    wire_points.append(tuple(wire_loc.values()))

            case 'L':
                for _ in range(n):
                    wire_loc['x'] -= 1
                    wire_points.append(tuple(wire_loc.values()))

            case 'U':
                for _ in range(n):
                    wire_loc['y'] += 1
                    wire_points.append(tuple(wire_loc.values()))

            case 'D':
                for _ in range(n):
                    wire_loc['y'] -= 1
                    wire_points.append(tuple(wire_loc.values()))

    return wire_points
