## Welcome to Hoo
#### A Playground Agent Based Model Repository

[Placeholder for a cute Owl (named Hoo?) who is the (so far, invisible) mascot for this project]

1. [Intro to `Hoo`](https://github.com/emmagras/hoo/blob/master/README.md#introduction)
2. [Intro to *Agent Based Modeling*](https://github.com/emmagras/hoo/blob/master/README.md#what-is-agent-based-modeling)
3. [Cases to Explore](https://github.com/emmagras/hoo/blob/master/README.md#cases)
3. [Dependencies](https://github.com/emmagras/hoo/blob/master/README.md#dependencies)

### Introduction
###### (Skip to [Into to Agent Based Modeling](https://github.com/emmagras/hoo/blob/master/README.md#what-is-agent-based-modeling),    [Back to top](https://github.com/emmagras/hoo/blob/master/README.md#welcome-to-hoo))
The motivation for this project came during a frustrating commute in my home town in Northern Virginia.
I like to imagine what the world will be like when cars can drive themselves, but we have a lot to explore as we create that reality. Autonomous and semi-autonomous cars are on the rise, but how we interact with them (and how they interact with each other) are still in their most basic exploratory phase. This project is a part of that exploration. 

### What is Agent Based Modeling?
###### (Skip to [Cases](https://github.com/emmagras/hoo/blob/master/README.md#cases),  [Back to top](https://github.com/emmagras/hoo/blob/master/README.md#welcome-to-hoo))
Agent based modeling is a simulation technique where the simulator creates a number of `agents` who interact with each other in various ways. Software developers may think of these `agents` simply as `objects` which have attributes and perform operations according to their circumstances.

In this project, the agents are, for the most part, cars on a road. Each car is an instance of an object which has a speed, a direction, and a location. We can then, for instance give each car a `following_distance` parameter and study the effects on traffic of increasing or decreasing. 

Without careful forethought, it's always possible to make ineffective policy decision in the name of good or progress. Agent Based Models help provide visible examples to counterintuitive tendencies, like [Braess' paradox](https://en.wikipedia.org/wiki/Braess%27_paradox) which explains that **adding a road to a congested road traffic network could increase overall journey time.** This project will use game theory and Python's Agent Based and statistical modelling capabilities to test hypotheses about how we can best construct our future roads.

### Cases
###### (Skip to [Dependencies](https://github.com/emmagras/hoo/blob/master/README.md#dependencies),  [Back to top](https://github.com/emmagras/hoo/blob/master/README.md#welcome-to-hoo))
These cases can be vague, and readers are invited to contribute. Exploring cases with a well reasoned theory behind it is important, but half of the point here is to have fun. 

Each of these case studies can be parameterized with varying agent population sizes and densities, ratios of autonomous to non-autonomous cars on the road, and the configuration of the roads. 

1. 
  - Question:
    - Can a minority of autonomous cars on the road respond to traffic patterns such that they break up traffic jams?

2. 
  - Question: 
    - What can we do about non-autonomous cars and pedestrians who abuse the overly cautious safety features of autonomous driving
  - Considerations:
    - Costly punishment (I spend `X` dollars to steal `p*X` (such that `0<p<1`) from you as punishment
    - Toll roads with increased costs for non-autonomous cars in certain lanes

3. 
  - Question: 
    - What are the various speed regulation rules on the road. What implications do they have on cars with smaller spending potentials, or even nearby real estate
  - Considerations:
    - Marginal cost of driving as a function of the lane a car is in, how fast, its size, etc
    - Cars bid for space on the road, pay other cars to move out of the way
    - What happens w/ accessibility to real estate in a busy area (for example if cars bid for traffic signals to change and homeowners can't costlessly get out of their neighborhood) 


[Back to top](https://github.com/emmagras/hoo/blob/master/README.md#welcome-to-hoo)
