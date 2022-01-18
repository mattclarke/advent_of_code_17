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
- Part 1:
- Part 2:

## Day 14:
- Part 1:
- Part 2:

## Day 15:
- Part 1:
- Part 2:

## Day 16:
- Part 1:
- Part 2:

## Day 17:
- Part 1:
- Part 2:

## Day 18:
- Part 1:
- Part 2:

## Day 19:
- Part 1:
- Part 2:

## Day 20:
- Part 1:
- Part 2:

## Day 21:
- Part 1:
- Part 2:

## Day 22:
- Part 1:
- Part 2:

## Day 23:
- Part 1:
- Part 2:

## Day 24:
- Part 1:
- Part 2:

## Day 25:
- Part 1:
- Part 2:
