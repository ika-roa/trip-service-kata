import pytest
from tripservice import User, get_trips_by_user, UserNotLoggedInException

from unittest.mock import patch


def find_trips_by_user(user):
    return user.trips


@pytest.fixture
def new_user():
    return User()


class TestWithoutLoggedUser:

    @patch('tripservice._get_logged_user', return_value="")
    def test_get_trips_raises_exception(self, patch_getLoggedUser, new_user):
        with pytest.raises(UserNotLoggedInException):
            get_trips_by_user(new_user)


@patch('tripservice._get_logged_user', return_value="Tom")
@patch('tripservice._find_trips_by_user', wraps=find_trips_by_user)
class TestWithLoggedUser:

    def test_get_trips_returns_empty_if_user_not_friend(self, patch_getLoggedUser, patch_findTripsByUser, new_user):
        assert get_trips_by_user(new_user) == []

    def test_get_trips_returns_empty_for_friends_without_trips(self, patch_getLoggedUser, patch_findTripsByUser,
                                                               new_user):
        new_user.add_friend("Tom")
        assert get_trips_by_user(new_user) == []

    def test_get_trips_returns_trips_for_friends(self, patch_getLoggedUser, patch_findTripsByUser, new_user):
        new_user.add_friend("Tom")
        new_user.add_trip("trip_1")
        assert "trip_1" in get_trips_by_user(new_user)
