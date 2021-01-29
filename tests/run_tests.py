import sys
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover(".")
    test_runner = unittest.runner.TextTestRunner(verbosity=2)
    result = test_runner.run(tests)
    sys.exit(not result.wasSuccessful())
