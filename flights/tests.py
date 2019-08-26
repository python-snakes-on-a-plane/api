from django.test import TestCase

# Create your tests here.
class snakeTest(TestCase):
    def test_fail(self):
        self.assertEqual(True, False)
        self.assertEqual(True, True)