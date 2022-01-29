#!/usr/bin/python3
#task0 voting 1024 times
""" Hodor Voting Contest """
import requests

url = "http://158.69.76.135/level0.php"
form = {
        "id": "3866",
        "holdthedoor": "Submit"
        }

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(url, data=form)
