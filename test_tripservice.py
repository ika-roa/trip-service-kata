import pytest
from tripservice import User, getTripsByUser, _getLoggedUser


def test_get_trips_from_new_user_returns_empty():
    new_user = User()
    getTripsByUser(new_user)
