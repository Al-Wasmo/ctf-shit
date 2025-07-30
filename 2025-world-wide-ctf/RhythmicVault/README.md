## Steps
- I kept trying random things until I wrote the parser and realized the input was the variables.
- I sorted the events using the formula `bar + beat` to get a `timestamp`.
- I wrote a parser to convert the sorted event-like format into readable pseudocode — check [`event_to_psudo_code.py`](./event_to_psudo_code.py) and its output `psudo_code`.
- I edited `task.rdlevel` to test a few things and better understand how the program works:
  - I removed some checks.
  - I only checked for part of the flag (`ww` and `f{`), and got `correct flag`.
- From there, I used the editor to guess how the game logic works.
- I used Python and some known fixed values to reverse-engineer the rest of the program.
- See [`flag.py`](./flag.py) for the full solution.


## Some Notes 
- The editor only shows the last 3 updated values. That helped a lot while guessing, but I really would’ve loved if it showed **all** the values.
- To fix that, I could’ve just added some visual text in the editor.


## Editor Tool
- I used the editor to solve this challenge, but it’s too large to upload to GitHub.
- You can check it out here: [https://rd-editor-docs.github.io/intro/](https://rd-editor-docs.github.io/intro/)