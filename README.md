# Trip Service Kata

The [Trip service kata](https://kata-log.rocks/trip-service-kata) provides an example of existing code that needs to be unit tested. 
The objective is to test and refactor the legacy TripService module. 
The end result should be well-crafted code that expresses the domain. 
We do not need tests for collaborators (right now), we want to test only the logic contained in the `getTripsByUser()` function.

But there is one rule:

> We can't change any existing code if not covered by tests. The only exception is if we need to change the code to add unit tests, but in this case, just automated refactorings (via IDE) are allowed. 

Although this is a very small piece of code, it has a lot of the problems that we find in legacy code. 

