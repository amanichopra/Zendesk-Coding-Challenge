from ticket_viewer import *
import unittest
from random import randint


class TestTicketViewer(unittest.TestCase):
    true_access_token = 'VNShXh0CtsAEU9z0v47cTKmSSSU8jnCHaSAxKmgn'

    def test_get_request_valid_response(self):
        self.assertEqual(get_request(self.true_access_token).status_code, 200)

    def test_get_request_invalid_response(self):
        self.assertNotEqual(get_request(''), 200)

    def test_data_format(self):
        data = get_data(get_request(self.true_access_token))
        true_keys = ['tickets', 'next_page', 'previous_page', 'count']
        self.assertEqual(list(data.keys()), true_keys)


if __name__ == '__main__':
    unittest.main()