from django.test import TestCase, Client

# Create your tests here.
class AppTest(TestCase):
    def test_app_html(self):
        response = Client().get('https://tugas2pbpfaris.herokuapp.com/mywatchlist/html', follow=True)
        self.assertEqual(response.status_code,200)

    def test_app_xml(self):
        response = Client().get('https://tugas2pbpfaris.herokuapp.com/mywatchlist/xml', follow=True)
        self.assertEqual(response.status_code,200)

    def test_app_json(self):
        response = Client().get('https://tugas2pbpfaris.herokuapp.com/mywatchlist/json', follow=True)
        self.assertEqual(response.status_code,200)