import argparse

from . import onetouch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default="192.168.1.1", help="The hostname or IP of the Alcatel OneTouch device")
    action = parser.add_subparsers(dest="action", help='The action to take')
    sms = action.add_parser("sms", help="send/receive SMSs")
    sms.add_argument('to', type=int)
    sms.add_argument('text')
    args = parser.parse_args()
    if args.action is None:
        parser.print_help()
    elif args.action == "sms":
        onetouch.send_sms(args.to, args.text, args.host)

if __name__ == "__main__":
    main()
