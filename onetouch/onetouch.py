import requests


HOST = "192.168.1.1"


def send_sms(to, message, host=HOST):
    data = {
        "sms_number": to,
        "sms_content": message,
        "sms_id": "NaN",
        "action_type": "new"
    }
    requests.post("http://{}/goform/sendSMS".format(host), data=data)
