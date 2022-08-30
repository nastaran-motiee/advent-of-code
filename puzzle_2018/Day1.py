def part_1_2(m_input_file):
    # part 1
    frequency = 0
    arr = open(m_input_file).read().split('\n')

    for i in range(len(arr)):
        frequency += int(arr[i])

    # part 2
    arr2 = [0]
    repeated = float('inf')
    f = 0
    while repeated == float('inf'):
        for i in range(len(arr)):
            print(f)
            f += int(arr[i])
            if f in arr2:
                repeated = f
                break
            else:
                arr2.append(f)

    return frequency, repeated
