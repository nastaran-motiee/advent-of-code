def part_1(input_file_path):
    input_file = open(input_file_path)
    line = None
    m_sum = 0
    while line != '':
        try:
            line = int(int(input_file.readline()) / 3) - 2
            m_sum += line
        except ValueError:
            break
    input_file.close()
    return m_sum


def part_2(input_file_path):
    input_file = open(input_file_path)
    line = None
    m_sum = 0
    while line != '':
        try:
            line = int(int(input_file.readline()) / 3) - 2
            while line >= 0:
                m_sum += line
                line = int(line / 3) - 2

        except ValueError:
            break
    input_file.close()
    return m_sum
