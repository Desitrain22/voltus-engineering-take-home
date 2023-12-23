# Voltus Take-Home Technical Challenge

Welcome to the take-home portion of the Voltus interview process!

## Expectations:
1. Coding portion of this work should take less than one hour.
1. To keep this challenge scoped, we'd like you to focus specifically on implementing a pattern for returning the data in
question. (We recognize the temptation to update the skeleton code in all kinds of ways!)
1. You may use outside libraries.  If so, please add them to `requirements.txt`.

## Completing the Assignment

1. You should pull this repo locally, make a branch, add your changes, and create a new PR against `main`.

1. After you open the PR, we'll schedule a 45-minute time for you to walk us through your solution, discuss alternative approaches, and consider ways that your work can be scaled and expanded into a larger ‘production’ system.

## Task

Complete the function `get_top5_peaks_for_market(market_name)`, found in `main.py`

Your service should use existing data (supplied in this repo) and develop an efficient way to prepare the data for use by your company’s Peak Usage dashboard, which needs to display the 5 highest usage measures for each energy market.

For instance, if the client requests data about the `spp` market, your app should return these 5 highest usage readings:

```
2022-07-26 13:48:00 ┆ 996
2022-07-02 10:19:54 ┆ 991
2022-07-27 23:44:24 ┆ 985
2022-07-06 00:43:37 ┆ 978
2022-07-04 15:09:40 ┆ 977   
```

## The code

All of the code for this challenge can be found in this repo in the `main.py` file.

## The data

All of the data for this challenge can be in this repo at `markets.csv` and `usage.csv`

## Running the app

Once you've pip installed the requirements in requirements.txt, you should be able to start the debug server with the
following command:

```
uvicorn main:app --port 8000 --reload
```

You should see output that looks like:

```
INFO:     Will watch for changes in these directories: ['<your working directory would be here>']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2165] using statreload
INFO:     Started server process [2182]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

You will then be able to view the auto-generated swagger docs and make test API requests by visiting the local url:

```
http://127.0.0.1:8000/docs

```

Good luck!


## (Optional) Useful Commands:

* `uvicorn main:app --port 8000 --reload` will serve the app.
* `pytest test` will run coverage and tests in the `test/` directory, and print output to the terminal, and to the `htmlcov/` directory.
* `mypy *.py` will run static analysis on all python files.