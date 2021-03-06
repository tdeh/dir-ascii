# Copyright 2017 Taylor DeHaan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module is the entry point for running unittests.

Example:
    In order to run this module and the unittests, use this command::

        $ python -m py_tree.tests
"""

import unittest


def load_tests(loader, standard_tests, pattern):
    """ Test loader function.

    This function is called by the unittest framework when running the
    unittests and loads all tests in files matching the pattern.
    """
    pattern = pattern or "test*.py"
    package_tests = loader.discover(start_dir=".", pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests


if __name__ == "__main__":
    unittest.main(verbosity=2)
