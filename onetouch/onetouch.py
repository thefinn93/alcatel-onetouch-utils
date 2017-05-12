import requests


HOST = "192.168.1.1"


def send_sms(to, text, host=HOST):
    data = {
        "sms_number": to,
        "sms_content": text,
        "sms_id": "NaN",
        "action_type": "new"
    }
    requests.post("http://{}/goform/sendSMS".format(HOST), data=data)
