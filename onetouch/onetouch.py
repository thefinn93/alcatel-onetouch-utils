import requests

from . import constants


def send_sms(to, message, host):
    data = {
        "sms_number": to,
        "sms_content": message,
        "sms_id": "NaN",
        "action_type": "new"
    }
    requests.post("http://{}/goform/sendSMS".format(host), data=data)


def get_sms(host):
    inbox = requests.post("http://{}/goform/getSMSlist".format(host), data={"key": "inbox", "pageNum": 1}).json()
    return inbox['data'][:-1]


def delete_sms(host, id):
    requests.post("http://{}/goform/deleteSMS".format(host), data={"sms_id": id})


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

    response['sim_state'] = constants.SIM_STATES[img_info['sim_state']]
    response['signal'] = img_info['signal']
    response['sms'] = constants.SMS_STATES[img_info['sms']]
    response['wan_state'] = constants.WAN_STATES[wan_info['wan_state']]
    response['wan_ip'] = wan_info["wan_ip"]
    response['network_type'] = constants.NETWORK_TYPES[wan_info['network_type']]
    response['network_name'] = wan_info['network_name']
    response['roaming'] = wan_info['roam'] == 1
    response['wan_ip6'] = wan_info['wan_ip6']
    return response
