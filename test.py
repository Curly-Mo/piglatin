#!/usr/bin/env python

import unittest


if __name__ == "__main__":
    """Run all unit tests in the tests directory"""
    all_tests = unittest.TestLoader().discover(
        'tests',
        pattern='*.py'
    )
    unittest.TextTestRunner().run(all_tests)
