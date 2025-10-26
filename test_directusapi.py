# test_directusapi.py
"""
Tests for DirectusAPI module.
"""

import unittest
from directusapi import DirectusAPI

class TestDirectusAPI(unittest.TestCase):
    """Test cases for DirectusAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DirectusAPI()
        self.assertIsInstance(instance, DirectusAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DirectusAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
