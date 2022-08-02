import requests
import time
from config import API_KEY


def solve_captcha(imageCode):
    '''
    Function to solve Image captcha through the 2captcha API
    '''
    
    submit_params = {
        "key": API_KEY,
        "method": "base64",
        "body": imageCode,
        "json": 1,
        "numeric": 0
    }
    reqestID = requests.get("http://2captcha.com/in.php", params=submit_params).json()["request"]
    get_params = {
        "key": API_KEY,
        "action": "get",
        "id": reqestID,
        "json": 1
    }
    r = requests.get("http://2captcha.com/res.php", params=get_params).json()
    while r["status"] == 0:
        r = requests.get("http://2captcha.com/res.php", params=get_params).json()
        time.sleep(2)
    return str(r["request"])
