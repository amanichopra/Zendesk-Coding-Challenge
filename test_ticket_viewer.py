from ticket_viewer import *
import unittest


class TestTicketViewer(unittest.TestCase):
    def test_get_request_valid_response(self):
        true_access_token = 'VNShXh0CtsAEU9z0v47cTKmSSSU8jnCHaSAxKmgn'
        self.assertEqual(get_request(true_access_token).status_code, 200)

    def test_get_request_invalid_response(self):
        self.assertNotEqual(get_request(''), 200)






if __name__ == '__main__':
    unittest.main()