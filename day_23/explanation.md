```set b 84
set c b
jnz a 2
    jnz 1 5             # always skipped
mul b 100
sub b -100000
set c b
sub c -17000        # b = 108400 and c = 125400 and c never changes
set f 1             #
set d 2
set e 2
set g d             # g = d
mul g e             # g *= e
sub g b             # g -= b
jnz g 2             # g increases by d each time (g is -ve)
    set f 0         # => g == b which implies b is a multiple of d?
sub e -1            # e++
set g e             # g = e
sub g b             # g -= b
jnz g -8            # jmp to line 12 if e != b - basically e and g increase by 1 each time (note: g is -ve)
sub d -1            # d++ and g = 0 and e = b
set g d
sub g b
jnz g -13           # jmp to line 12 - exits when d = b
jnz f 2
    sub h -1        # h++ if f == 0
set g b
sub g c             # g = b - c
jnz g 2
    jnz 1 3         # finished when b == c => line 31 called 1000 times
sub b -17           # b += 17
jnz 1 -23           # jmp to line 9
```
## Explanation

- 'c' is a constant (125400).
- 'b' is set to an initial number (108400) and only incremented on line 31 (+17).
- the program exits when 'b == c' and the difference between 'b' and 'c' is initially 17,000 => line 31 runs 1000 times. 
This implies that the maximum 'h' could possibly be is 1001 as line 26 can only be called at most 1001 times (+1 for first
time through).
- 'h' is only ever incremented when 'f' is 0, for this to be true then at line 15 'g' must be equal to 'b' which implies that 'b'
must divisible by 'd', and as 'd' monotonically incremented (line 21) starting from 2 until it equals 'b' (line 24) then the
only time line 16 isn't called is when 'b' is prime!
- I then grabbed a list of primes between 'b' and 'c' off the web and counted the number of them that were 
`(p - 108400) % 17 == 0` which was 98.
- So the answer is 1001 - 98 = 903.
