def part_1(m_input_path):
    A, B = open(m_input_path).read().split('\n')
    A, B = [x.split(',') for x in [A,B]]

    A_points = set()
    B_points=set()
    
    A_loc = {'x': 0, 'y': 0}
    B_loc = {'x': 0, 'y': 0}

    for d in A:
        direction = d[0]
        n = int(d[1:])

        match direction:
            case 'R':
                 for _ in range(n):
                    A_loc['x'] += 1
                    A_points.add(tuple(A_loc.values()))

            case 'L':
                 for _ in range(n):
                    A_loc['x'] -= 1
                    A_points.add(tuple(A_loc.values()))        

            case 'U':
                for _ in range(n):
                    A_loc['y'] += 1
                    A_points.add(tuple(A_loc.values()))
                        
            case 'D':
                for _ in range(n):
                    A_loc['y'] -= 1
                    A_points.add(tuple(A_loc.values()))  

    for d in B:
        direction = d[0]
        n = int(d[1:])

        match direction:
            case 'R':
                 for _ in range(n):
                    B_loc['x'] += 1
                    B_points.add(tuple(B_loc.values()))

            case 'L':
                 for _ in range(n):
                    B_loc['x'] -= 1
                    B_points.add(tuple(B_loc.values()))       

            case 'U':
                for _ in range(n):
                    B_loc['y'] += 1
                    B_points.add(tuple(B_loc.values()))
                        
            case 'D':
                for _ in range(n):
                    B_loc['y'] -= 1
                    B_points.add(tuple(B_loc.values())) 
            
    mutual = A_points & B_points

    for point in mutual:
        m_distance = abs(point[0]) + abs(point[1])
        break

    for point in mutual:
        temp =  abs(point[0]) + abs(point[1])
        if temp < m_distance:
            m_distance = temp
    
    return m_distance

  

            
       
        
       
            



