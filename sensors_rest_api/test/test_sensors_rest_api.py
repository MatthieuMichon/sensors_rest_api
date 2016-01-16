import sensors_rest_api
import unittest


"""
tests.test_sensors_rest_api
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main test file.
"""

class SensorsRestApiTestCases(unittest.TestCase):

    def setUp(self):
        # sensors_rest_api.app.testing = True
        self.app = sensors_rest_api.app.test_client()

    def test_dummy(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
