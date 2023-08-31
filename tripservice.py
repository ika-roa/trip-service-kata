#!/usr/bin/env python


#
# Exceptions
#
class DependentClassCallDuringUnitTestException(Exception):
    pass


class UserNotLoggedInException(Exception):
    pass


#
# Classes
#
class Trip:
    pass


class User:
    def __init__(self):
        self.trips = []
        self.friends = []

    def add_friend(self, user):
        self.friends.append(user)

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_friends(self):
        return self.friends


#
# Functions
#
def _is_user_logged_in(user):
    raise DependentClassCallDuringUnitTestException(
        "UserSession.isUserLoggedIn() should not be called in an unit test"
    )


def _get_logged_user():
    raise DependentClassCallDuringUnitTestException(
        "UserSession.getLoggedUser() should not be called in an unit test"
    )


def _find_trips_by_user(user):
    raise DependentClassCallDuringUnitTestException(
        "TripDAO should not be invoked on an unit test."
    )


def get_trips_by_user(possible_friend):
    logged_user = _get_logged_user()

    if not logged_user:
        raise UserNotLoggedInException()

    if is_friend(logged_user, possible_friend):
        return _find_trips_by_user(possible_friend)
    else:
        return []


def is_friend(user, possible_friend):
    if user in possible_friend.get_friends():
        return True
    else:
        return False


if __name__ == "__main__":
    pass
