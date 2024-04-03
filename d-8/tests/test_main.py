import unittest

from main import (
    filter_number_list,
    get_intersection_lists,
    check_palindrom
)


class TestFilterNumberListFunc(unittest.TestCase):
    
    def test_succes(self):
        number_list = [1, 2, 43, 45, 212, 231, 21]
        self.assertEqual(filter_number_list(number_list), [2, 212])
        
    
    def test_with_string(self):
        string = 'hello world!'
        self.assertEqual(filter_number_list(string), 
                         'работает только со списком чисел')
        
        
    def test_with_int(self):
        number = 32
        self.assertEqual(filter_number_list(number), 
                         'работает только со списком чисел')
        
    def test_with_bool(self):
        number = True
        self.assertEqual(filter_number_list(number), 
                         'работает только со списком чисел')
        
        
        
class GetIntersectionList(unittest.TestCase):
    
    def test_success(self):
        numbers_one = [1, 2, 3, 4, 5, 6]
        numbers_two = [1, 2, 43, 5, 32132]
        numbers = get_intersection_lists(numbers_one, numbers_two)
        result = [2, 5 , 1]
        self.assertCountEqual(numbers, result)
        
        for number in numbers:
            self.assertIn(number, [2,5,1])
        
        
    def test_empty_list(self):
        numbers_one = []
        numbers_two = []
        numbers = get_intersection_lists(numbers_one, numbers_two)
        self.assertEqual(numbers, [])
    
    def test_list_string(self):
        numbers_one = 'hello world'
        numbers_two = 'hello'
        numbers = get_intersection_lists(numbers_one, numbers_two)
        self.assertEqual(numbers, 'работает только со списками')


class TestCheckPolindromFunc(unittest.TestCase):
    
    def test_result_true(self):
        name = 'aziza'
        self.assertTrue(check_palindrom(name))
        
    def test_result_false(self):
        name = 'iman'
        self.assertFalse(check_palindrom(name))
    
    def test_with_number_true(self):
        number = 1111
        self.assertTrue(check_palindrom(number))
    
    def test_with_number_false(self):
        number = 1234
        self.assertFalse(check_palindrom(number))