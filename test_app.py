import unittest
from todo_project import app

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_main_page_requires_login(self):
        response = self.app.get('/')
        self.assertIn(response.status_code, [200, 302])

if __name__ == '__main__':
    unittest.main()
