import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_add_two_numbers(self):
        response = self.client.get('/calculator/add?operands=7,-7')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['sum'], 0.0)

    def test_add_single_number(self):
        response = self.client.get('/calculator/add?operands=42')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['sum'], 42.0)

    def test_add_multiple_numbers(self):
        response = self.client.get('/calculator/add?operands=1,2,3.5,4')
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.get_json()['sum'], 10.5)

    def test_add_empty_input(self):
        response = self.client.get('/calculator/add?operands=')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['sum'], 0.0)

    def test_add_invalid_input(self):
        response = self.client.get('/calculator/add?operands=1,a,3')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_add_with_whitespace(self):
        response = self.client.get('/calculator/add?operands= 1 , 2 , 3 ')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['sum'], 6.0)

    def test_add_negative_and_float_mix(self):
        response = self.client.get('/calculator/add?operands=-5.5,2.5,1')
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.get_json()['sum'], -2.0)

    def test_missing_operands_param(self):
        response = self.client.get('/calculator/add')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['sum'], 0.0)

    def test_large_input_set(self):
        operands = ','.join(str(i) for i in range(1000))  # 0 + 1 + ... + 999 = 499500
        response = self.client.get(f'/calculator/add?operands={operands}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['sum'], 499500.0)

    def test_add_with_special_characters(self):
        response = self.client.get('/calculator/add?operands=1,2,@,3')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    
