# test_bucketlist.py

import unittest
import json
from week2 import create_app, db

class DatabaseTestCase(unittest.TestCase):

    def test_api_can_print_all(self):
        """Test API can get a bucketlist (GET request)."""
        res = self.client().printall('/locations/')
        self.assertEqual(res.status_code, 201)

    def test_api_can_filter(self):
        res = self.client().filter('/locations/')
        self.assertEqual(res.status_code, 200)

    def test_bucketlist_can_be_edited(self):
        res = self.client().filter('/locations/')
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
