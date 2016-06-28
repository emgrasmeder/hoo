Goal: make a generic map pin move from 14th and R to 14th and T (or the other way around) in Washington, DC.

Iterations:
1. move pin linearly in 10 descrete steps from A - B and B - A
2. move multiple ordered pins A - B
3. nodes regulate their throughput.
  1. multiple pins move A - B - C, where C is regulated to 1 car per second.
4. nodes communicate backup to node before them when their capacity threshold is reached.
  - capacity threshold is a function of the node ahead
  - at freeflow, B can allow 1 car per second. but if C has 10 cars waiting in a queue, C will send a message to B that now B's throughput is identical to (or capped by?) C, which is at capacity.
