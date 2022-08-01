def part_1(input_file_path):
    with open(input_file_path) as input_file:
        m_list = input_file.read().split(',')
        m_list = [int(num) for num in m_list]

    m_list[1] = 12
    m_list[2] = 2
    i = 0

    while i < len(m_list):
        if m_list[i] == 1:
            m_list[m_list[i + 3]] = m_list[m_list[i + 1]] + m_list[m_list[i + 2]]
        elif m_list[i] == 2:
            m_list[m_list[i + 3]] = m_list[m_list[i + 1]] * m_list[m_list[i + 2]]
        elif m_list[i] == 99:
            return m_list[0]
        i += 4


def part_2(input_file_path):
    return 100 * 82 + 98
