from pybluedot.tests import base
from pybluedot.api.patent import Patent


class PatentTestSuite(base.DietTestCase):
    """This test suite provides some common things relevant to the
       tests in this file. All tests should inherit from this class
    """

    def setUp(self):
        """Perform setup activities
        """
        self.patent = Patent()
        self.url = 'https://api.nasa.gov/patents/content'
        self.params_test = { 'query' : 'plasic',
                             'api_key' : 'DEMO_KEY',
                             'concept_tags' : False,
                             'limit' : None }

    @mock.patch('patent.requests.get')

    def test_get_response_ok(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        expected_dict = {'key':'value'}
        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response
        response_dict = self.patent.get(self.url, params = self.params_test)
        mock_get.assert_called_once_with(self.url, params = self.params_test)




    def test_get_response_NOT_ok(self):
        pass

    def test_json_response(self):
        pass

    def test_error_in_json_response(self):
        pass

if __name__ == "__main__":
    unittest.main()
