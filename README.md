# Receive and rotate problem

This project presents a solution to the receive and rotate problem.

## Requirements

### For Python

A python 3 version installed. Not sure which is the lowest needed. I am running `3.8` therefore I would say to try it with that one if the one installed is not working.

### For Javascript

A Node version installed. Not sure if any requirements on version. Mine - `v15.12.0`.

## Running

### For Python

- To trigger the program run `python receive_and_rotate.py`.

- To trigger tests run `python test_receive_and_rotate.py`

### For Javascript

- To trigger the program run `node slyp.js`.
- There were no test written for Javascript as I hoped my logic was well tested in Python as well as by running the JS script.

## Additional assumptions

In addition to the instruction some assumption were made to best fit the goal:

- Since the task was to receive words following groups were removed from the definition of 'word': Empty words (`''`), Words containing non-alphabet characters (`pap3r`/`sun_bath`)
- All input words are match to the same (lower) case.

## Learnings

List of learnings from this exercise:

- You can use native `venv` and `unittest` modules to set up an environment as well as set up unit tests. (no need to install `pytest`)

- You can check if a string is a rotation if you validate if it is contained in a double of the initial word. For `dog` you need to check if `gdo` is contained within "do`gdo`g"

## Final notes

The main reason why I posted two language version was to practice. After the first stage I felt a little bit rusty, so I decided I needed a bit of refreshment. Especially on the JavaScript side. It is nice to rediscover concepts like scopes, `this`, closures etc...

Also I have never done a side by side comparison of a problem using different languages and I must say this is an interesting conceptual play. A nice way of exploring what one language can offer is contrast to another.
