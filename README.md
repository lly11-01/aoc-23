# Advent of Code 2023

Trying out Advent of Code this year, gonna be documenting my solutions to each day here! \
Also gonna be adding my thought processes for each day down below! \
All solutions are written in Python

## Day 1 (Spoilers!)
<details>
  <summary>First star</summary>

  Pretty straightforward, for each row in the given data just filter out all the non-digits. \
  Then for each row, just pick out the first and last digits, string them into a two-digit number. \
  Finally just add all the two-digit numbers together. \
  Overall really simple, not much more to say!
</details>
<details>
  <summary>Second star</summary>

  Now *this* is where the puzzle starts to get interesting. \
  My first thought was to replace the first instance of the word `one`, `two` etc. with the corresponding digit, and then recursively replace the next instance and so on. \
  \(You can see it as the commented out `convert_to_digit` function in `day1.py` \) \
  Once all the words were converted to their corresponding digits it was pretty much the same as the first star. \
  Surprisingly, this didn't work and I got the wrong answer \
  Turns out that overlapping letters are permitted, while I assumed each letter could only be a part of one digit \
  \(so `twone` would actually map to `21`, whereas I thought it would only map to `2` and the `ne` part would be garbage\) \
  In this case I just went through every non-digit letter and see if it corresponded to the start of a new word \
  Once I strung all the digits together it was the same as part 1, grabbing the first and last digits, putting them together, and finally summing all the two-digit numbers together! \
  Overall not too bad but certainly a problem that has room for interpretation

</details>

## Day 2 (Spoilers!)
<details>
  <summary>First star</summary>

  Not all that difficult today, probably the most difficult part was parsing the input string.\
  Would definitely be easier to just use regex to parse it but kinda too lazy and didn't bother.
</details>
<details>
  <summary>Second star</summary>

  Again, not too difficult, but I wonder if it would be worth the effort to use OOP and create classes for a game and a game state.\
  Probably not for a single AoC problem unless there's some continuation between days 

</details>

## Day 3 (Spoilers!)
<details>
  <summary>First star</summary>

  The problem was a little daunting at the start, but I felt like I was over-thinking a bit too much. \
  Was thinking too much about bitmasking \(even though I had no idea how to implement it\) when I probably should've just stuck to first principles.\
  That said, bitmasking is definitely on my reading list for the future
  
</details>
<details>
  <summary>Second star</summary>

  Maybe this star is where using bitmasking would be a bit of a red herring however.\
  Realized I couldn't reuse my solution to part 1 and had to almost completely rewrite my solution.\
  At least I could reuse the part where I gathered each of the numbers, but I probably should've started from there in the first star instead of going straight to bitmasking and shit.\
  Also I think writing an `isdigit` method for the `Gear` class to always return `False` instead of checking if `entry` is a string instead of a `Gear` is kinda funny

</details>

## Day 4 (Spoilers!)
<details>
  <summary>First star</summary>

  Really easy, just another exercise in text parsing.\
  `count_winners` could probably just use `filter` and `len` instead of a for loop and if check though
  
</details>
<details>
  <summary>Second star</summary>

  Fun use of a queue! \
  Basic idea is to use a queue to keep track of the number of duplicate cards there are. \
  Might use this problem as an example problem when teaching queues! \
  UPDATE: After reading the reddit megathread, seems like using a queue was a bit overkill and you only need a list. Still, a fun problem to give to any newbie programmer!

</details>

## Day 5 (Spoilers!)
<details>
  <summary>First star</summary>
  
  Supposed to be a pretty easy task but I kinda overcomplicated it a little in anticipation of what I thought the second star's problem would be. \
  Turns out you can assume that each seed will always have a 1-to-1 mapping to the soil type, and soil to the fertilizer type etc. \
  \(My incorrect assumption was that the different ranges could overlap, meaning one seed could possibly map to two or more different soil types. Or if not for the first star, that would be the twist for the second star!\)\
  What I did originally in `map_seed` was to originally convert the `input` seed into a list then repeatedly add a new output if the input was in the mapping range. \
  Then once the seed was mapped to the final location number\(s\), I would take the smallest location number from the list! \
  
</details>
<details>
  <summary>Second star</summary>

  Oh boy now this was rough. Not only was my earlier assumption not correct \(so I did all that extra complexity for nothing\), but my program was _super_ inefficient!\
  For this solution I just used a brute force method and calculated the mapped location number for each seed one by one. Took about 6 hours to finish processing the input seeds with their giant ranges!\
  I have an idea to use some sort of window so that it can map many seeds at once if they're all within the same mapping, but that'll be a task for another time.
</details>

## Day 6 (Spoilers!)
<details>
  <summary>First star</summary>

  Was out the entire day today so thankfully today's puzzle was really simple that could be banged out very quickly.\
  \(Though I did kinda cheat by looking at it while I was out, was a little tripped up at the start and thought I had to whip out the ol' accelerating displacement formula from physics class a long time ago!\)
  
</details>
<details>
  <summary>Second star</summary>

  My heart did sink a bit when the answer didn't print instaneously and thought I had to finally do some optimizations.\
  But thankfully Python is not _that_ slow and I got it after a couple seconds of waiting.\
  The unoptimized brute force method lives another day!
</details>

## Day 7 (Spoilers!)
<details>
  <summary>First star</summary>

  Thought I was being clever by converting each hand to a hexadecimal score but as I'm writing this I realized I could probably just use regular string comparisons instead.\
  Tbf though in classic fashion I misread the question again, and thought it was like classic poker where the order of the cards do not matter.\
  How my scoring would've worked in classic poker is that the hand with the _lowest_ score is the best hand, a five-of-a-kind would be a two digit hexadecimal number starting with a `1`, and the second digit is the score of the label \(i.e. an `A` has the smallest score of 1, a `K` the next smallest score of 2, all the way down to a `2` having the largest score of D\) \
  Then four-of-a-kind would be a three-digit hexadecimal number starting with a `1`, the second digit is the score of the four-of-a-kind label and the third digit the score of the single label;\
  a full house would be another three-digit hexadecimal number starting with a `2` instead, the second digit is the score of the three-of-a-kind label and the third digit the score of the pair label \
  And so on with the next types.\
  It would've been fun to implement this scoring system \(though it's not like this puzzle wasn't fun either, especially the second star!\)
</details>
<details>
  <summary>Second star</summary>

  Am kinda scared of greedy algorithms so I had to take some time to convince myself that a greedy algorithm will always give the right solution in this case.\
  Luckily the 3-of-a-kind is ranked higher than a two pair here, would be a lot more interesting \(and maybe quite a bit more difficult!\) if it was the other way round
</details>

## Day 8 (Spoilers!)
<details>
  <summary>First star</summary>

  Pretty simple graph traversal, just traverse through the graph according to the sequence that was given until you reach node `ZZZ`. \
  Nothing really much else to say
</details>
<details>
  <summary>Second star</summary>

  Now _this_ was me being an idiot for several hours.\
  What I did for my original solution \(you can see it is commented out in the .py file\) was traverse the starting nodes simultaneously one step at a time and check whether all the nodes ended with a `Z`.\
  Turns out, just like in day 5, that if you are doing things one step at a time your solution will be _hilariously_ slow.\
  But I thought I had some free time today so I just left it alone and let it run.\
  It wasn't until a couple hours later until I realized that I could just calculate the number of steps required for _each_ starting node to traverse to the end, then take the LCM of those to get the correct answer.\
  Hours of time wasted which did lead me to facepalm quite a bit
</details>

## Day 9 (Spoilers!)
<details>
  <summary>First star</summary>

  Really easy but really fun! \
  The only real trick \(if you really want to call it a trick\) is noticing that the next value in the original sequence is just the last values of each sequence summed together
</details>
<details>
  <summary>Second star</summary>
  
  Similar to the first part, but instead of adding the last values of each sequence together, the idea is to subtract the first value in the last sequence from the first value in the second-last sequence, then subtract that from the first value in the third-last sequence, etc.\
  Which means the `accumulate` function really comes in handy!
</details>

## Day 10 (Spoilers!)
<details>
  <summary>First star</summary>

  Graphs my mortal nemesis >:C \
  Anyways this ended up being a relatively simple BFS to visit all the pipes that are in the loop and assign their distances from the start pipe.\
  Tough part for me is just designing the graph itself, which is why my code looks _super_ atrocious \(Apologies for that! I hate graphs\)
</details>
<details>
  <summary>Second star</summary>
  
  Now that I had the entire pipe loop from the first part, I got the idea to do a flood fill on the outskirts until it reached a pipe within the loop.\
  That worked at removing _most_ of the points outside of the loop, but since "squeezing between pipes is also allowed", now I had to also remove those points that are fully enclosed with pipes but are still considered "outside the loop".\
  Was kinda stuck at how to continue, so I cheated a little and decided to look at the reddit megathread for some ideas.\
  Credit to [u/hi_im_new_to_this](https://www.reddit.com/r/adventofcode/comments/18evyu9/comment/kcqtow6/) for this fun fact, and with that I could figure out how to solve it! \
  Just needed to iron out a few quirks like `L7` or `FJ` only counting as one wall instead of two \(because the two walls are technically at different heights and you would only cross one of those walls but not both\) \
  Still not _super_ convinced that my solution is 100% correct and covers all the possible edge cases but hey iiwiw
</details>

## Day 11 (Spoilers!)
<details>
  <summary>First star</summary>

  Was slightly concerned that my old nemesis would make a return, but thankfully it wasn't all that bad.\
  Because of the grid like structure the shortest path between two galaxies is just the taxicab distance between them, which is really easy to calculate!\
  The expanding space is an interesting spanner thrown in the works, but it wasn't that difficult to account for\
</details>
<details>
  <summary>Second star</summary>
  
  Still not too bad, just instead of actually using more memory to make a bigger universe, you just need to keep track of the number of empty rows/columns between the two galaxies and add them to the distance.\
  Was tripped up by the math quite a bit but after taking some time to draw stuff out, I got the solution out pretty easily
</details>
