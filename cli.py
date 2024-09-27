import argparse

import api

"""
sagsa generate --doc="notification_conge.pdf" --mode="leave" --params="recipients.xlsx"
sagsa send --doc="notification_conge" --params="recipients.xlsx"
sagsa delete --doc="notification_conge"
"""

parser = argparse.ArgumentParser()

parser.add_argument('command', choices=['generate', 'send', 'delete'])
parser.add_argument('--pdf')
parser.add_argument('--excel')


args = parser.parse_args()


if args.command == 'generate':
    api.generate(args.pdf, args.excel)