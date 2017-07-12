# Copyright 2016 Jeorry Balasabas
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

from pybluedot.tests import base


class SampleTestSuite(base.DietTestCase):
    """This test suite provides some common things relevant to the
       tests in this file. All tests should inherit from this class
    """

    def setUp(self):
        """Perform setup activities
        """

        super(SampleTestSuite, self).setUp()

    def tearDown(self):
        """Perform teardown activities
        """

        super(SampleTestSuite, self).tearDown()


class test_sample_foo(SampleTestSuite):
    """This is a sample unit test. Implement the testing here
    """

    def runTest(self):
        """Runs the unit test
        """

        self.assertTrue(True)
