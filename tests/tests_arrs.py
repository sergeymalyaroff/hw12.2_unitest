import unittest
from utils.arrs import get, my_slice


class TestArrsFunctions(unittest.TestCase):
    def test_get_existing_index(self):
        # Тестирование получения значения по существующему индексу
        array = [1, 2, 3, 4, 5]
        index = 2
        default = "Not found"
        expected_result = array[index]

        result = get(array, index, default)

        self.assertEqual(result, expected_result)

    def test_get_non_existing_index(self):
        # Тестирование получения значения по несуществующему индексу
        array = [1, 2, 3, 4, 5]
        index = 10
        default = "Not found"
        expected_result = default

        result = get(array, index, default)

        self.assertEqual(result, expected_result)

    def test_get_negative_index(self):
        # Тестирование получения значения по отрицательному индексу
        array = [1, 2, 3, 4, 5]
        index = -2
        default = None
        expected_result = default

        result = get(array, index, default)

        self.assertEqual(result, expected_result)

    def test_my_slice_start(self):
        # Тестирование извлечения среза с указанием начального индекса
        coll = [1, 2, 3, 4, 5]
        start = 2
        expected_result = [3, 4, 5]

        result = my_slice(coll, start=start)

        self.assertEqual(result, expected_result)

    def test_my_slice_default_arguments(self):
        # Тестирование извлечения среза с использованием значений по умолчанию
        coll = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]

        result = my_slice(coll)

        self.assertEqual(result, expected_result)

    def test_my_slice_end(self):
        # Тестирование извлечения среза с указанием конечного индекса
        coll = [1, 2, 3, 4, 5]
        end = 4
        expected_result = [1, 2, 3, 4]

        result = my_slice(coll, end=end)

        self.assertEqual(result, expected_result)

    def test_my_slice_negative_indices(self):
        # Тестирование извлечения среза с использованием отрицательных индексов
        coll = [1, 2, 3, 4, 5]
        start = -3
        end = -1
        expected_result = [3, 4]

        result = my_slice(coll, start, end)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
