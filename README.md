## Welcome to Hoo
### A Playground Agent Based Model Repository

My main desire in this project is to give my frustrated Northern Virginia commuter thoughts some outlet.
I like to imagine what the world will be like when cars can drive themselves, but there are quite a number of roadway institutions to chosoe from regarding how traffic flows in a more automated world. While we can't be certain we'll ever find the global maximum, we can use agent based modeling to explore a number of the imaginable frameworks and seek to understand the set of local maxima possible within each.

### What is Agent Based Modeling?
Agent based modeling is a simulation technique where the simulator creates a number of autonomous `agents` who can interact with each other in various ways. Typically the agents have a number of parameters that can be altered to study the impact of different variables in the system. 

In this project, the agents are, for the most part, cars on a road. Each car is an instance of an object which has a speed, a direction, and a location. We can then, for instance give each car a `following_distance` parameter and study the effects on traffic of increasing or decreasing. 
