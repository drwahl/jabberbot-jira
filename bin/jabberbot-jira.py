#!/usr/bin/env python

from jabberbot import JabberBot, botcmd
from configure import read_configuration
import os

class JiraJabberBot(JabberBot):
    @botcmd
    def ticketinfo(self, message, args):
        """
        Follows along in chat and returns ticket details when ticket numbers
        are mentioned.
        """


def main():
    """
    The main body of the bot, if started from CLI.
    """

    import argparse

    # read configurations from a config file
    config = read_configuration()

    # get CLI options
    cmd_parser = argparse.ArgumentParser(
        description='A python jabber bot to notify details about tickets mentioned in chat')
    cmd_parser.add_argument('-u', '--username', dest='username', action='store',
        help='Jabber username for the bot', default=None)
    cmd_parser.add_argument('-p', '--password', dest='password', action='store',
        help='Jabber password for the bot', default=None)
    cmd_parser.add_argument('-s', '--jira_server', dest='jira_server', action='store',
        help='Jira server to connect to', default=None)
    cmd_parser.add_argument('-U', '--jira_username', dest='jira_username', action='store',
        help='Username used to authenticate with Jira', default=None)
    cmd_parser.add_argument('-P', '--jira_password', dest='jira_password', action='store',
        help='Password used to authenticate with Jira', default=None)
    cmd_parser.add_argument('-r', '--jira_regex', dest='jira_regex', action='store',
        help='Regex used when watching for tickets to be mentioned in chat', default=None)
    args = cmd_parser.parse_args()

    if args.username:
        config['username'] = args.username
    if args.password:
        config['password'] = args.password
    if args.jira_server:
        config['jira_server'] = args.jira_server
    if args.jira_username:
        config['jira_username'] = args.jira_username
    if args.jira_password:
        config['jira_password'] = args.jira_password
    if args.jira_regex:
        config['jira_regex'] = args.jira_regex

    print config
    #bot = JiraJabberBot(config)
    #bot.server_forever()

if __name__ == "__main__":
    main()
