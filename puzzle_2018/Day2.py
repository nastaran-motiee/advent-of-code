def part_1(input_file_path):
    m_input = open(input_file_path).read().split('\n')
    two = 0
    three = 0
    for line in m_input:
        if there_is_two(line):
            two += 1
        if there_is_three(line):
            three += 1

    return two * three


def there_is_two(m_str):
    for letter in m_str:
        if m_str.count(letter) == 2:
            return True
    return False


def there_is_three(m_str):
    for letter in m_str:
        if m_str.count(letter) == 3:
            return True
    return False


def part_2(input_file_path):
    m_input = open(input_file_path).read().split('\n')
    for i in range(0, len(m_input)):
        for line in m_input[: i] + m_input[i+1: ]:
            if difference_count(m_input[i], line) == 1:
                return find_common(m_input[i], line)


def difference_count(str1, str2):
    count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count


def find_common(str1, str2):
    common = ''
    for i in range(0, len(str1)):
        if str1[i] == str2[i]:
            common += str1[i]
    return common
