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
from pybluedot.api import patent
from pybluedot.tests import base
import requests
from requests.exceptions import HTTPError


class PatentTestSuite(base.DietTestCase):
    """This test suite provides some common things relevant to the
       tests in this file. All tests should inherit from this class
    """

    def setUp(self):
        """Perform setup activities
        """
        self.testpatent = patent.Patent(query='plastic')

    @mock.patch('pybluedot.api.patent.requests.get', autospec=True)
    def test_get_response_ok(self, mock_get):
        mock_response = mock.Mock()
        expected_dict = {'key': 'value'}
        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response
        response_dict = self.testpatent.get()
        self.assertEqual(1, mock_response.json.call_count)
        self.assertEqual(response_dict, expected_dict)

    @mock.patch('pybluedot.api.patent.requests.get', autospec=True)
    def test_get_response_fail(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = HTTPError('NASA API DOWN')
        mock_get.return_value = mock_response
        response = self.testpatent.get()
        self.assertEqual(1, mock_response.raise_for_status.call_count)
