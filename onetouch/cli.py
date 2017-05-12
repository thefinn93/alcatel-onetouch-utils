import argparse
import json

from . import onetouch, __version__


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default="192.168.1.1", help="The hostname or IP of the Alcatel OneTouch device")
    action = parser.add_subparsers(dest="action", help='The action to take')
    sms = action.add_parser("sms", help="send/receive SMSs")
    sms.add_argument('to', type=int)
    sms.add_argument('message')

    status = action.add_parser("status")
    status.add_argument("fields", nargs="*")

    action.add_parser("version")

    args = parser.parse_args()
    if args.action == "status" or args.action is None:
        status = onetouch.get_status(args.host)
        if not hasattr(args, 'fields') or len(args.fields) == 0:
            print(json.dumps(status))
        elif len(args.fields) == 1:
            print(status[args.fields[0]])
        else:
            out = [(field, status[field]) for field in args.fields]
            print(json.dumps(dict(out)))
    elif args.action == "sms":
        onetouch.send_sms(args.to, args.message, args.host)
    elif args.action == "version":
        print("Alcatel OneTouch Utils version {}".format(__version__))

if __name__ == "__main__":
    main()
