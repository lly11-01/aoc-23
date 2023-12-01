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
  My first thought was to replace the first instance of the word `one`, `two` etc. with the corresponding digit, \
  and then recursively replace the next instance and so on. \
  \(You can see it as the commented out `convert_to_digit` function in `day1.py` \) \
  Once all the words were converted to their corresponding digits it was pretty much the same as the first star. \
  Surprisingly, this didn't work and I got the wrong answer \
  Turns out that overlapping letters are permitted, while I assumed each letter could only be a part of one digit \
  \(so `twone` would actually map to `21`, whereas I thought it would only map to `2` and the `ne` part would be garbage\) \
  In this case I just went through every non-digit letter and see if it corresponded to the start of a new word \
  Once I strung all the digits together it was the same as part 1, \
  Grabbing the first and last digits, putting them together, and finally summing all the two-digit numbers together! \
  Overall not too bad but certainly a problem that has room for interpretation

</details>
