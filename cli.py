import argparse

import api

"""
sagsa generate --doc="notification_conge.pdf" --mode="leave" --params="recipients.xlsx"
sagsa send --doc="notification_conge" --params="recipients.xlsx"
sagsa delete --doc="notification_conge"
"""

def run():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', choices=['generate_folder', 'send_folder', 'delete_folder', 'send'])
    parser.add_argument('--pdf')
    parser.add_argument('--folder')
    parser.add_argument('--excel')
    parser.add_argument('--generate', type=int, default=1)
    parser.add_argument('--delete', type=int, default=1)


    args = parser.parse_args()


    if args.command == 'generate_folder':
        api.generate_folder(args.pdf, args.excel)
    elif args.command == 'send_folder':
        api.send_folder(args.folder, args.excel)
    elif args.command == 'delete_folder':
        api.delete_folder(args.folder)
    elif args.command == 'send':
        api.send(args.pdf, args.excel, args.generate, args.delete)



if __name__ == '__main__':
    run()