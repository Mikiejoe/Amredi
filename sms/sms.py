import requests
import logging
from decouple import config
from urllib.parse import urlencode
import json


""" This is a function for sending a verification code to the new user """
def send_authentication_code(phone_number: str, verification_code: str)->str:
    headers = {
        "apikey": config("api_key"),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    payload = urlencode({
        "username": "sandbox",
        "to": phone_number,
        "message": f"Your Amredi verification code is: {verification_code}",
        "from": config("alphanumeric")
    })
    print(config("username"))

    url = "https://api.sandbox.africastalking.com/version1/messaging"

    try:
        request = requests.post(url=url, headers=headers, data=payload)
        print(request.content)
        if request.status_code == 201:
            response = json.dumps(request.json(), sort_keys=True, indent=4, ensure_ascii=False)
            print(response)
            return response
        
        else:
            logging.error(f"Failed to send with status code: {request.status_code}")

    except Exception as e:
        logging.error(f"Opps! an error has occuured: {str(e)}")

# if __name__ == "__main__":
#     # send_authentication_code("254743596183","12345")



