import loguru
from requests_html import HTMLSession
from generator import username_gen, password_gen
from loguru import logger
from requests_params import *
import base64
from captcha import solve_captcha


def register(email: str, username: str = username_gen(), password: str = password_gen()):
   
    '''
    Main function to create an account on https://gidonline.eu/
    '''
    
    logger.info("Creating new account...")
    
    session = HTMLSession()
    
    if len(password) < 6:
        password = password_gen()

    params = {"do": "register"}
    respForm = session.get('https://gidonline.eu/index.php', headers=form_headers, params=params)

    while True:
        usernameResponse = session.post("https://gidonline.eu/engine/ajax/registration.php", data={"name": username})
        if usernameResponse.html.find("font", first=True).attrs["color"] == 'green':
            break
        username = username_gen()
    
    imageBytes = session.get("https://gidonline.eu/engine/modules/antibot/antibot.php", headers=captcha_headers).content
    imageBase64 = base64.b64encode(imageBytes)
    captchaKey = solve_captcha(imageBase64)

    data = {
        'name': username,
        'password1': password,
        'password2': password,
        'email': email,
        'sec_code': captchaKey,
        'submit': '',
        'submit_reg': 'submit_reg',
        'do': 'register',
    }

    response = session.post("https://gidonline.eu/index.php", params=params, data=data, headers=submit_headers)

    elem = response.html.find("[name=fullname]", first=True)
    if bool(elem):
        logger.info(f"Account created successfully! Creadentials: {username}:{password}:{email}")
        return {
            'username': username,
            'password': password,
            'email': email
        }
    else:
        logger.error("ERROR OCCURED!")
        logger.error(response.html.find(".berrors ul", first=True).text)
        return None
