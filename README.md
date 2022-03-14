# Solution Write Up
## Autonomous Vehicle Routing Coding Challenge
Schedule your car to get people where they want to go as fast as possible.

## Installation 
### Requirements
- Python 3.9+
- [optional] coverage, unittest

### Running `python src/main.py`
### Testing
1. `python -m unittest` to run all tests
2. `python -m unittest test.test_passenger` to test an individual module
3. `coverage run -m unittest` and `coverage report -m` to run a coverage report

## Distilled Requirements & Constraints
1. [x] Get people to their destination as quickly as possible
2. [x] Print current position of vehicle and names of all passengers in vehicle each time unit
3. [x] Print anyone being dropped off or picked up at an intersection to the console
4. [x] At initialization your code should take as inputs the number of streets in both the x and y directions (ex. x=10, y=10)
5. [x] Car can move in any direction exactly 1 block at a time
6. [x] Car can fit 'infinite' passengers

# Overview of Solution
When approaching this problem, the algorithm seemed to be the most important swappable element. The rules of the system
can remain relatively static, i.e. will pick up a person/will drop off a person when on the start/end positions of a 
user. However, the path finding algorithm needs to be able to be adaptable. There is an interface for the algorithm to
allow for dependency inversion/swappable components. 

The biggest problem was to determine what is meant by '*fast as possible*'. What is the measurement of success here?
Could it be the average wait times of passengers, or the median? Is it acceptable to have someone remain in the car for
an extremely long time while maximizing the lowest time for the population? This problem statement does not address the
human element or practical situations. The current assumption is that the car would navigate to the nearest passenger, which would become the fastest time.

The existing algorithm is simple. It navigates to the nearest pick-up point upon initialization, and then proceeds to the
drop-off point. While in route, if the car visits an intersection where someone else is waiting, the vehicle will automatically 
pick them up. Once the drop-off has been completed, if any passengers were picked up along the way, it will find an appropriate
route to drop them off. The setup takes advantage of 'happy coincidences' along the path. When there are no more passengers, the
car will find the nearest pick-up point (if any) and navigate there, thus repeating the cycle.

A more advance solution I had thought of was to maximize route efficiency via brute-force. Instead of 1 loop always navigating first on
the X axis each time followed by a Y move, it would choose 3 potential routes. The first would be the original algorithm, the second would be the inverse of the first, and the third would be a 'zigzag' to the destination where it would alternate between x/y moves. The reason for these 3 routes is to compare each to see which route is most profitable. If any of these 3 routes would have a pick-up point along the way, then it would be the favored route. The more the pickup points, the better the route. A full-on brute force of every possible path to a destination might yield better results, but due to the infinite potential of the grid, 3 seemed appropriate to prove out the profit analysis.

Even beyond this 'advance' solution could be incorporating wait times, which was the ultimate goal of the system. When 2 routes have the same profit, the ones that have higher wait times might prove to be the winner. And then further, incorporating the potential new route length, and subsequent pick ups, would allow the system to build the absolute lowest cost system. This begins to be more akin to a chess board evaluating a position of all possible moves. In this sort of system, the car can only take advantage of what it sees in the current moment, rather than see into the future. Building on past experiences of the car, common locations for the car to cross to optimize potential future pick ups, etc, would allow for an improvement on wait times.

One particular point of interest would be on evaluating when the path-finding algorithm would be triggered. The current set-up is that
a route is determined, and then the path-finding algorithm is never invoked again until the car completes its route. It may be advantageous to implement a new method on the algorithm to 'check-in' to make sure if the existing route is still optimal, and then overriding the route if appropriate.

## Future improvements & Considerations
1. More validation of incoming data
2. Bounds checking
3. Leveraging keys rather than looping on arrays to discover items (efficiency tweaks)
4. Figuring out the 'duplicate' passenger problem (keys)
5. More tests, especially with running at higher grid dimensions
6. The car seems like it may have been better used with the Visitor pattern, but would need to evaluate
7. Would want to investigate some more similar problems here and how they were approached
8. Try out different algorithms
9. Testing for negative coordinates
10. Loading in JSON as its own function, or allowing command line arguments to stream in new positions, etc.