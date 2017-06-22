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

import mock
from pybluedot.api import apod
from pybluedot.tests import base
from requests.exceptions import HTTPError


@mock.patch('pybluedot.api.apod.requests.get', autospec=True)
class ApodTestSuite(base.DietTestCase):
    """This test suite provides some common things relevant to the
       tests in this file. All tests should inherit from this class
    """

def setUp(self):
    """Perform setup activities
    """
    self.testapod = apod.Apod()

    def test_get_response_ok(self, mock_get):
        mock_response = mock.MagicMock()
        expected_dict = {'key': 'value'}
        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response
        response_dict = self.testapod.get()
        self.assertEqual(1, mock_response.json.call_count)
        self.assertEqual(response_dict, expected_dict)

    def test_get_response_raises_HTTPError(self, mock_get):
        
