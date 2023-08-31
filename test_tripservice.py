import pytest
from tripservice import User, getTripsByUser, UserNotLoggedInException

from unittest.mock import patch


def find_trips_by_user(user):
    return user.trips


class TestWithoutLoggedUser:

    @patch('tripservice._getLoggedUser', return_value="")
    def test_get_trips_raises_exception(self, patch_getLoggedUser):
        new_user = User()
        with pytest.raises(UserNotLoggedInException):
            getTripsByUser(new_user)


class TestWithLoggedUser:

    @patch('tripservice._getLoggedUser', return_value="Tom")
    def test_get_trips_returns_empty_if_user_not_friend(self, patch_getLoggedUser):
        new_user = User()
        assert getTripsByUser(new_user) == []

    @patch('tripservice._getLoggedUser', return_value="Tom")
    @patch('tripservice._findTripsByUser', wraps=find_trips_by_user)
    def test_get_trips_returns_empty_for_friends_without_trips(self, patch_getLoggedUser, patch_findTripsByUser):
        new_user = User()
        new_user.addFriend("Tom")
        assert getTripsByUser(new_user) == []

    @patch('tripservice._getLoggedUser', return_value="Tom")
    @patch('tripservice._findTripsByUser', wraps=find_trips_by_user)
    def test_get_trips_returns_trips_for_friends(self, patch_getLoggedUser, patch_findTripsByUser):
        new_user = User()
        new_user.addFriend("Tom")
        new_user.addTrip("trip_1")
        assert "trip_1" in getTripsByUser(new_user)
