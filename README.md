# advent_of_code_16
https://adventofcode.com/2016

## Day 1
- Part 1: looping but don't forget to check the last value.
- Part 2: modulo to find the element halfway round.

## Day 2
- Part 1: find the max and min for each row of data.
- Part 2: for each value in a row, look for when modulo is zero with any other value in the row.

## Day 3
- Part 1: simple to brute force, but did it with maths for a bit of fun.
- Part 2: brute force.

## Day 4
- Part 1: put the list of words in a set and see if both are the same length.
- Part 2: first sort the letters of each word and then create the set.

## Day 5
- Part 1: simple looping.
- Part 2: similar but with decrement for >= 3. Takes ~10 secs with Python, < 1 second with PyPy.

## Day 6
- Part 1: simple looping.
- Part 2: essentially the same code with some extra book-keeping to keep track of the target.

## Day 7
- Part 1: construct the graph and find the root. The root will be the node that doesn't appear in any other nodes list.
- Part 2: recurse until we find a mismatch, calculate the difference and add it to the base node. Used an exception to
terminate recursion :(

## Day 8
- Part 1: parse the commands, run them and find the highest value in the registers.
- Part 2: minor modification to max the updated register against the max so far.

## Day 9
- Part 1: move through the input and if it is a valid '{' increase the depth and on a valid '}' increase the score and
decrease the depth.
- Part 2: add a variable to count the garbage.

## Day 10
- Part 1: copy the "selected" values, reverse them and then overwrite. A little % magic to handle going past the end.
- Part 2: follow the recipe basically. I was getting a wrong answer because I forgot to strip the newline from the input.

## Day 11
- Part 1: hexagons => going directly north or south is y += 2.
- Part 2: to get the maximum calculate the total distance after each move. Takes a couple of seconds - it should be
possible to only calculate the relative distance change, so that would be quicker.
Massive speed up after looking at https://www.redblobgames.com/grids/hexagons/.
If we define q as the distance along the SW to NE axis and r as the distance along the NW to SE axis then:
```
n => r -= 1
s => r += 1
ne => q += 1 and r -= 1
se => q += 1
sw => q -= 1 and r += 1
nw => q -= 1
```
And the distance from the origin is just max(abs(q), abs(r)!


## Day 12:
- Part 1: pretty simple - BFS from '0' node and collect nodes seen in a set.
- Part 2: start from each node that hasn't already been seen and repeat part 1 but starting from that node.

## Day 13:
- Part 1: can be done by brute force by using a loop to work out where the sensor is for the current position.
- Part 2: brute force looping would take a very long time, so it was necessary to use maths to find the sensor positions.

## Day 14:
- Part 1: using knot hash algorithm from day 10, apply it for each row and count the number of ones.
- Part 2: for each non-empty cell, use a BFS to work out which non-empty cells are connected to it. Store the connected
cells  in a set, so anytime we find a non-empty cell we haven't seen before we know it is a new region.

## Day 15:
- Part 1: bitmasks FTW! Python takes ~40 seconds, PyPy < 1 second!
- Part 2: slight modification.

## Day 16:
- Part 1: step through the instructions.
- Part 2: 1,000,000,000 is a big number, so run the algorithm until we get the original data back as this gives us the
"repeat interval". "big number" % "repeat interval" gives us the number of times we need to perform the algorithm to get
the answer.

Note: because of the "Partner" command swaps based on letter not index, I don't think we can short-cut the algorithm.

## Day 17:
- Part 1: construct a linked list and run the algorithm.
- Part 2: big number! As we are only interested in the value after the zeroth entry, we only need to track the current
index, the buffer size and the "first" value. When the index is zero we update the "first" value.

## Day 18:
- Part 1: implement instruction set and exit when "recv" receives a value.
- Part 2: on "snd" command add to queue, on "recv" read from queue. Took me a while to realise there was `jgz 1 3`
command and because I was using defaultdict "1" was a treated as a valid key rather than a value - d'oh!

## Day 19:
- Part 1: work out an algorith for following the path and accumulate the letters.
- Part 2: add a variable to count the steps.

## Day 20:
- Part 1: find the particle(s) with the lowest acceleration. Turned out to be only one!
- Part 2: run the algorithm and handle the collisions; run until there are no more collisions.
Would be nice to exit the loop based on logic but seems overkill for AoC.

## Day 21:
- Part 1: put all the translations of an input into a dict, so we do all the rotating and flipping once at the beginning.
Then it is just working through the algorithm, hopefully, without any indexing bugs...
- Part 2: same as part 1 but run more iterations (takes ~5 seconds). I suspect if one doesn't do the rotations and
flips upfront and instead does them for each "square" then it takes a very long time.

## Day 22:
- Part 1: cellular automata-ish. Using a set because the grid is infinite.
- Part 2: handling more complex transitions so changed set to dict. Reasonably quick to run (~5 seconds in PyPy).

## Day 23:
- Part 1: modified the ASM runner from day 18.
- Part 2: see the explanation file in the directory.

## Day 24:
- Part 1: fill a dict of the connections (don't forget they can be used either way round!) and recurse.
- Part 2: add global variables to track the longest and it's strength.

Unexpectedly simple for day 24. Takes ~25 seconds with Python and ~4 seconds with PyPy.

## Day 25:
- Part 1: relatively simple algorithm to end the year.
- Part 2: no part 2.
