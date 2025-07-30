# Bad Apple Challenge Writeup

## Steps

- I did random stuff until things started making sense.
- First, I noticed the static method that initializes everything and sets up some global strings used for printing later. Honestly, it feels like the author put it there just to waste our time — not sure.
  - Anyway, I wrote the decoders — see `decoder.py`.
  - One of the functions uses the filename to extract *hidden info*, but the file name was `BadApple.java`, so it had clearly been modified.  
    I got the real filename **by luck** when I exported the `jadx` data into a file named `BadApplePlayer-jadx-readable.java`. Turned out to be pretty useful.
- After that waste of time, I moved on to the other functions:
  - One does `huffman-19` encoding.
  - The other does `huffman-20`.
  - **Only `19` is used**, though!!!
- Next, I jumped to the main function. It sets up some binary data — `compressed frames` and a `music file`.  
  These are the files that were breaking my editors. 😅
- I wrote a script to extract the `compressed frames`:  
  See `extract_frames.py`, which outputs `data2-extract`.
- At this point, I understood the code and how everything works.  
  But I still didn’t know how to solve the challenge.  

So I thought — maybe it’s intentionally setting some *wrong info* in the frames, which corrupts the flow and messes up the rendering.

- I recreated the same logic in Python — check `runner.py` (a replica of the Java code).
- After printing and debugging the data:  
  Nothing. The data wasn’t corrupted. Everything looked the same.

And then the CTF event ended — so I wasn’t able to finish in time.

- Turns out, the solution was just to **use `huffman-20`** instead of the `huffman-19` being used.  
  Maybe if I had just one or two more hours, I would’ve guessed it. Unfortunately, I didn’t.

---

## Final Thoughts

- This challenge got **0 solves** (would’ve been 1 if I had a bit more time).
- The idea was actually simple — I think most people just got discouraged because their tools kept crashing.
- **Welp**, at least I got a cool Bad Apple tool out of it. 😄

---

## Files

- `BadApplePlayer.java`: Original file, decompiled using some Java decompiler.
- `BadApplePlayer-clean.java`: Same as original, but with the huge string removed to avoid crashes.
- `BadApplePlayer-jadx-readable.java`: Decompiled via JADX — the most readable version.
- `data2-extract`: Extracted compressed frame data.
- `extract_frames.py`: Reads `BadApplePlayer.java` and extracts frame data.
- `runner.py`: Python replica of the original Java program logic.
- `frames_data`: Debug output to verify frame integrity (turns out, nothing was corrupted).

---

![meme](meme.jpg)
