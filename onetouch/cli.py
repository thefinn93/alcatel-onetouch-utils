import argparse
from prettytable import PrettyTable
import json

from . import onetouch, __version__


def prettyprint(data, f):
    if f == "json":
        print(json.dumps(data))
    elif f == "table":
        first_row = data[0] if isinstance(data, list) else data
        fields = list(first_row.keys())
        fields.sort()
        t = PrettyTable()
        if isinstance(data, list):
            t.field_names = fields
            for row in data:
                t.add_row([row.get(x) for x in fields])
        else:
            for key in fields:
                t.add_row(key, data.get(key))
        print(t)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default="192.168.1.1", help="The hostname or IP of the Alcatel OneTouch device")
    parser.add_argument('-f', '--format', choices=["json", "table"], default="table")

    action = parser.add_subparsers(dest="action", help='The action to take')

    sms = action.add_parser("sms")
    sms_action = sms.add_subparsers(dest="sms_action")
    sms_send = sms_action.add_parser("send")
    sms_send.add_argument('to', type=int)
    sms_send.add_argument('message')
    sms_action.add_parser("list")
    sms_delete = sms_action.add_parser("delete")
    sms_delete_group = sms_delete.add_mutually_exclusive_group(required=True)
    sms_delete_group.add_argument("-m", "--message", nargs="+")
    sms_delete_group.add_argument("-a", "--all", action="store_true")

    status = action.add_parser("status")
    status.add_argument("fields", nargs="*")

    action.add_parser("version")

    args = parser.parse_args()
    if args.action == "status" or args.action is None:
        status = onetouch.get_status(args.host)
        if not hasattr(args, 'fields') or len(args.fields) == 0:
            prettyprint(status, args.format)
        elif len(args.fields) == 1:
            prettyprint(status[args.fields[0]], args.format)
        else:
            out = [(field, status[field]) for field in args.fields]
            prettyprint(out, args.format)
    elif args.action == "sms":
        if args.sms_action == "send":
            onetouch.send_sms(args.to, args.message, args.host)
        elif args.sms_action == "list":
            prettyprint(onetouch.get_sms(args.host), args.format)
        elif args.sms_action == "delete":
            if args.all:
                for message in onetouch.get_sms(args.host):
                    onetouch.delete_sms(args.host, message['sms_id'])
            else:
                for message in args.message:
                    onetouch.delete_sms(args.host, message)
    elif args.action == "version":
        print("Alcatel OneTouch Utils version {}".format(__version__))

if __name__ == "__main__":
    main()
