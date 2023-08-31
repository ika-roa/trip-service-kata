# Trip Service Kata

> Each attempt can be found in its separate branch. The main branch contains the original code as a common starting point for further attempts.

The [Trip service kata](https://kata-log.rocks/trip-service-kata) provides an example of existing code that needs to be unit tested. 
The objective is to test and refactor the legacy TripService module. 
The end result should be well-crafted code that expresses the domain. 
We do not need tests for collaborators (right now), we want to test only the logic contained in the `getTripsByUser()` function.
Although this is a very small piece of code, it has a lot of the problems that we find in legacy code. 


## Business Rules

Imagine a social networking website for travellers:
- You need to be logged in to see the content
- You need to be a friend to see someone else's trips
- If you are not logged in, the code throws an exception

## Exercise Rules

- Our job is to write tests for the `getTripsByUser()` function until we have 100% coverage
- Once we have 100% coverage, we need to refactor and make the code better.
- At the end of the refactoring, both tests and production code should clearly describe the business rules

## Exercise Constraints

- We cannot manually change production code if not covered by tests
- If we need to change the `getTripsByUser()` function in order to test, you can do so using automated refactorings (via IDE)
- We CANNOT change the public interface of the function

## Source

The code from this Kata was created by https://github.com/sandromancuso/trip-service-kata. 
Only the Python part was used, and the Readme accordingly.
