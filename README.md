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
  Might use this problem as an example problem when teaching queues!

</details>
