import requests


# Stolen from the top of http://192.168.1.1/js/main.js
SIM_STATES = [
    "ABSENT",
    "PRESENT",
    "NOT_INIT",
    "CHV_BLOCKED",
    "NOT_READY",
    "VALID",
    "REINIT",
    "ILLEGAL_CARD",
    "INVALID",
    "ERROR",
    "LOCK_CHECK"
]

SMS_STATES = [
    "DISENABLE",
    "FULL",
    "NOREAD",
    "READ"
]

WAN_STATES = [
    "DISCONNECTED",
    "CONNECTING",
    "CONNECTED",
    "DISCONNECTING"
]

NETWORK_TYPES = [
    "NO_SERVICE",
    "GPRS",
    "EDGE",
    "HSDPA",
    "HSUPA",
    "UMTS",
    "CDMA",
    "EV_DO_A",
    "EV_DO_B",
    "GSM",
    "EV_DO_C",
    "LTE",
    "HSPA_PLUS",
    "DC_HSDPA_PLUS"
]


def send_sms(to, message, host):
    data = {
        "sms_number": to,
        "sms_content": message,
        "sms_id": "NaN",
        "action_type": "new"
    }
    requests.post("http://{}/goform/sendSMS".format(host), data=data)


def get_status(host):
    response = {
        "sim_state": None,
        "signal": None,
        "sms": None,
        "wan_state": None,
        "wan_ip": None,
        "network_type": None,
        "network_name": None,
        "roaming": None,
        "wan_ip6": None
    }
    img_info = requests.get("http://{}/goform/getImgInfo".format(host)).json()
    wan_info = requests.get("http://{}/goform/getWanInfo".format(host)).json()

    response['sim_state'] = SIM_STATES[img_info['sim_state']]
    response['signal'] = img_info['signal']
    response['sms'] = SMS_STATES[img_info['sms']]
    response['wan_state'] = WAN_STATES[wan_info['wan_state']]
    response['wan_ip'] = wan_info["wan_ip"]
    response['network_type'] = NETWORK_TYPES[wan_info['network_type']]
    response['network_name'] = wan_info['network_name']
    response['roaming'] = wan_info['roam'] == 1
    response['wan_ip6'] = wan_info['wan_ip6']
    return response
