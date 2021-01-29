import sys
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover(".")
    testRunner = unittest.runner.TextTestRunner(verbosity=2)
    result = testRunner.run(tests)
    sys.exit(not result.wasSuccessful())
