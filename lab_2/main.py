import math
import unittest
def angry_cows_location(n: int, c: int, free_section: list)-> int:
    if n < 2 or n > 100000 or n > len(free_section):
        return -1
    if c < 2 or c > n:
        return -1

    free_section.sort()
    if c == 2:
        return free_section[-1] - free_section[0]

    delta = (free_section[-1] - free_section[0]) // (c - 1)
    position = [free_section[0]]
    for i in range(c - 2):
        new_element = free_section[0] + delta * (i + 1)
        free_section.append(new_element)
        free_section.sort()
        index = free_section.index(new_element)
        difference_to_less = new_element - free_section[index - 1]
        difference_to_more = free_section[index + 1] - new_element

        if difference_to_more > difference_to_less:
            position.append(free_section[index - 1])
        elif difference_to_more < difference_to_less:
            position.append(free_section[index + 1])
        else:
            position.append(free_section[index - 1])
            position.append(free_section[index + 1])

        free_section.remove(new_element)
    position.append(free_section[-1])

    temp = ""
    for element in position:
        if element == temp:
            position.remove(element)
        else:
            temp = element

    position_length = len(position)
    if position_length == c:
        difference = 1000000000
        for i in range(position_length - 1):
            temp = position[i + 1] - position[i]
            if temp < difference:
                difference = temp
        return position, difference
    else:
        difference_list = []
        temp = position[0]
        for element in position:
            difference = element - temp
            difference_list.append(difference)
            temp = element
        difference_list.sort()
        difference = difference_list[-c]

        l = len(difference_list)
        help_array = difference_list[l - c:]
        result_array: list = [free_section[0]]
        temp = free_section[0]
        for i in range(len(help_array)):
            for element in help_array:
                temp = temp + element
                if temp in free_section:
                    result_array.append(temp)
            return result_array, difference


def place_in_board(n: int, w: int, h: int)-> int:
    # if n < 1 or n > 1012:
    #     return -1
    # if w < 1 or w > 109:
    #     return -1
    # if h < 1 or h > 109:
    #     return -1

    # paper_area = n * w * h
    # length = math.ceil(math.sqrt(paper_area))
    # number_of_columns = length // w
    # number_of_lines = length // h
    # counter = 0
    # while number_of_lines * number_of_columns < n:
    #     length += 1
    #     number_of_columns = length // w
    #     number_of_lines = length // h
    #     counter += 1
    # return length, counter

    l, r = 1, max(w, h) * n
    counter = 0
    while l < r:
        mid = (r + l) // 2

        number_of_columns = mid // w
        number_of_lines = mid // h
        total = number_of_lines * number_of_columns

        if total >= n:
            r = mid
        else:
            l = mid + 1

        counter += 1
    return math.ceil(l), counter




if __name__ == '__main__':
    # free_section = [1,2,3,4,5,10,30,40,60,90]
    # n = 10
    # c = 4
    # print(angry_cows_location(n,c,free_section))

    n, w, h = 10, 1, 2
    print(place_in_board(n, w, h))

    # a, b, c = 1012, 109, 109
    # print(place_in_board(a, b, c))


# class TestAngryCowsLocation(unittest.TestCase):
#
#     def test_example(self):
#         free_section = [1, 2, 8, 4, 9]
#         n = 5
#         c = 3
#         assert_result = 3
#         actual_result = angry_cows_location(n, c, free_section)
#         self.assertEquals(assert_result, actual_result)
#
#     def test_too_many_angry_cows(self):
#         free_section = [1, 2, 8, 4, 9]
#         n = 5
#         c = 6
#         assert_result = -1
#         actual_result = angry_cows_location(n, c, free_section)
#         self.assertEquals(assert_result, actual_result)
#
#     def test_not_enough_angry_cows(self):
#         free_section = [1, 2, 8, 4, 9]
#         n = 5
#         c = 1
#         assert_result = -1
#         actual_result = angry_cows_location(n, c, free_section)
#         self.assertEquals(assert_result, actual_result)
#
#     def test_not_enough_cows(self):
#         free_section = [1, 2, 8, 4, 9]
#         n = 1
#         c = 3
#         assert_result = -1
#         actual_result = angry_cows_location(n, c, free_section)
#         self.assertEquals(assert_result, actual_result)
#
#     def test_too_many_cows(self):
#         free_section = [1, 2, 8, 4, 9]
#         n = 6
#         c = 3
#         assert_result = -1
#         actual_result = angry_cows_location(n, c, free_section)
#         self.assertEquals(assert_result, actual_result)
#
#     def test_two_angry_cows(self):
#         free_section = [1, 2, 8, 4, 9]
#         n = 5
#         c = 2
#         assert_result = 8
#         actual_result = angry_cows_location(n, c, free_section)
#         self.assertEquals(assert_result, actual_result)
#
#     def test_lesson(self):
#         free_section = [1,2,3,4,5,10,30,40,60,90]
#         n = 10
#         c = 4
#         assert_result = 29
#         actual_result = angry_cows_location(n,c,free_section)
#         self.assertEqual(assert_result,actual_result)
