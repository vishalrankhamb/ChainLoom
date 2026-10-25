# test_chainloom.py
"""
Tests for ChainLoom module.
"""

import unittest
from chainloom import ChainLoom

class TestChainLoom(unittest.TestCase):
    """Test cases for ChainLoom class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainLoom()
        self.assertIsInstance(instance, ChainLoom)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
