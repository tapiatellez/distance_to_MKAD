from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        """Ensure that flask was set up correctly."""
        tester = app.test_client(self)
        response = tester.get('/', content_type = 'html_text')
        self.assertEqual(response.status_code, 200)

    def test_address_page(self):
        """Ensure index page loads the correct html."""
        tester = app.test_client(self)
        response = tester.get('/', content_type = "html_text")
        self.assertTrue(b'Address Locator' in response.data)

    def test_address_correct(self):
        """Testing page with a retrievable address"""
        tester = app.test_client(self)
        response = tester.post("/result",
                             data = dict(location="Chennai"),
                             follow_redirects=True)
        self.assertIn(b"Chennai, Chennai District, Tamil Nadu, 600001, India", response.data)

    def test_address_incorrect(self):
        """Testing page for an unretrievable address."""
        tester = app.test_client(self)
        response = tester.post("/result",
                             data = dict(location = "@1i451p4i1u3"),
                             follow_redirects = True)
        self.assertIn(b"Null address", response.data)

    def test_address_empty(self):
        """Test for a null address."""
        tester = app.test_client(self)
        response = tester.post("/result",
                               data = dict(location =""),
                               follow_redirects = True)
        self.assertIn(b"Null input", response.data)

    def test_address_inside_mkad(self):
        """Test for an address inside of MKAD location."""
        tester = app.test_client(self)
        response = tester.post("/result",
                               data = dict(location="Moscow Ring Road"),
                               follow_redirects = True)
        self.assertIn(b"Address is inside of MKAD", response.data)



if __name__ == '__main__':
    unittest.main()
