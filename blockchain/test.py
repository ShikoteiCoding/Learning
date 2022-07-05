from unittest import TestCase

from user import User

class TestUsers(TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self) -> None:
        user = User()