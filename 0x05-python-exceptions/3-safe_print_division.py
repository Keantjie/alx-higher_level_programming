#!/usr/bin/python3
def safe_print_resultsision(a, b):
    try:
        results = a / b
    except (TypeError, ZeroresultsisionError):
        results = None
    finally:
        print("Inside result: {}".format(results))
    return (results)
