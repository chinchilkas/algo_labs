import unittest

def square_list(start_list: list):
    square = []
    for element in start_list:
        square.append(element ** 2)

    for i in range(len(square)):
        for j in range(0, len(square) - i - 1):
            if square[j] > square[j + 1]:
                square[j], square[j + 1] = square[j + 1], square[j]
            j += 1
        i += 1
    return square

class TestSquareList(unittest.TestCase):

    def test_pass(self):
        default_list = [-4,-2,0,1,3]
        assert_result = [0,1,4,9,16]
        actual_result = square_list(default_list)
        self.assertEquals(assert_result, actual_result)

    def test_fail(self):
        default_list = [1,2,3,4,5]
        assert_result = [1,4,9,16]
        actual_result = square_list(default_list)
        self.assertNotEqual(assert_result, actual_result)


if __name__ == '__main__':
    a = [1, 9, 4, 7]

    print(square_list(a))
