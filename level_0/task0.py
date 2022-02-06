#!/usr/bin/python3
#task0 voting 1024 times
""" Hodor Voting Contest """
import requests

url = "http://158.69.76.135/level0.php"
form = {
        "id": "80",
        "holdthedoor": "Submit"
        }
crash = 0

if __name__ == "__main__":
    for i in range(0, 1024):
        result = requests.post(url, data=form)
        if result.status_code != 200:
            print("Failed to post {} the request".format(i))
            crash += 1
    print("Failed {} number or requests".format(crash))
