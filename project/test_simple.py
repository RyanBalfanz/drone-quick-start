from django.test import TestCase


class SimpleTestCase(TestCase):
	def test_should_pass(self):
		self.assertEqual(True, True)
