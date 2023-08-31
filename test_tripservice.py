import pytest
from tripservice import User, getTripsByUser, UserNotLoggedInException

from unittest.mock import patch


class TestWithoutLoggedUser:

    @patch('tripservice._getLoggedUser', return_value="")
    def test_get_trips_raises_exception(self, patch_func):
        new_user = User()
        with pytest.raises(UserNotLoggedInException):
            getTripsByUser(new_user)


class TestWithLoggedUser:

    @patch('tripservice._getLoggedUser', return_value="Tom")
    def test_get_trips_returns_empty_if_user_not_friend(self, patch_func):
        new_user = User()
        assert getTripsByUser(new_user) == []



