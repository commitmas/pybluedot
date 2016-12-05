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
