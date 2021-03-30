# Receive and rotate problem

This project presents a solution to the receive and rotate problem.

## Requirements

### For Python

A python 3 version, but I am not sure which is the lowest. I am running `3.8` therefore I would say that is the version needed.

## Installation

## Running

### For Python

    To trigger the program run `python receive_and_rotate.py`.

    To trigger tests run `python test_receive_and_rotate.py`

## Additional assumptions

In addition to the instruction some assumption were made to best fit the goal:

- Since the task was to receive words following groups were removed from the definition of 'word': Empty words (`''`), Words containing non-alphabet characters (`pap3r`/`sun_bath`)
- All input words are match to the same (lower) case.

## Learnings

List of learnings from this exercise:

- You can use native `venv` and `unittest` modules to set up an environment as well as set up unit tests. (no need to install `pytest`)

- You can check if a string is a rotation if you validate if it is contained in a double of the initial word. For `dog` you need to check if `gdo` is contained within "do`gdo`g"
