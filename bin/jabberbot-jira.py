#!/usr/bin/env python

from jabberbot import JabberBot, botcmd
from configure import read_configuration
import SOAPpy
import os


class JiraJabberBot(JabberBot):

    def __init__(self, *args, **kwargs):
        ''' Initialize variables. '''

        # answer only direct messages or not?
        self.only_direct = False

        # initialize jabberbot
        super(JiraJabberBot, self).__init__(*args, **kwargs)


    def callback_message(self, conn, mess):
        ''' Changes the behaviour of the JabberBot in order to allow
        it to answer direct messages. This is used often when it is
        connected in MUCs (multiple users chatroom). '''

        message = mess.getBody()
        if not message:
            return
        else:
            return super(JiraJabberBot, self).callback_message(conn, mess)


    def _queryJira(self, jira_server=None, jira_username=None, jira_password=None):
        """
        Establish a connection to the jira server
        """

        soap = SOAPpy.WSDL.Proxy('%s/rpc/soal/jirasoapservice-v2?wsdl' % jira_server)
        auth = soap.login(jira_username, jira_password)

        try:
            result = soap.getIssue(auth, ticket)
            valid = True
        except:
            valid = False

        if not valid:
            # reply to jabber that the ticket is not valid
            pass
        else:
            tmp_statuses = soap.getStatuses(auth)
            tmp_priorities = soap.getPriorities(auth)

            status = {}
            for i in tmp_statuses:
                status[i['id']] = i['name']

            priorities = {}
            for i in tmp_priorities:
                priorities[i['id']] = i['name']

            url = '%s/browse/%s' % (server, result['key'])

            # return the data we care about from the ticket
            #return


    @botcmd
    def ticketinfo(self, message, args):
        """
        Follows along in chat and returns ticket details when ticket numbers
        are mentioned.
        """



def config():
    return read_configuration()

def main():
    """
    The main body of the bot, if started from CLI.
    """

    import argparse

    # read configurations from a config file
    conf = config()

    # get CLI options
    cmd_parser = argparse.ArgumentParser(
        description='A python jabber bot to notify details about tickets mentioned in chat')
    cmd_parser.add_argument('-u', '--username', dest='username', action='store',
        help='Jabber username for the bot', default=None)
    cmd_parser.add_argument('-p', '--password', dest='password', action='store',
        help='Jabber password for the bot', default=None)
    cmd_parser.add_argument('-c', '--channel', dest='channel', action='store',
        help='Jabber channel (MUC) for the bot to join', default=None)
    cmd_parser.add_argument('-n', '--nickname', dest='nickname', action='store',
        help='Jabber nickname (MUC) for the bot', default=None)
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
        conf['username'] = args.username
    if args.password:
        conf['password'] = args.password
    if args.channel:
        conf['channel'] = args.channel
    if args.nickname:
        conf['nickname'] = args.nickname
    if args.jira_server:
        conf['jira_server'] = args.jira_server
    if args.jira_username:
        conf['jira_username'] = args.jira_username
    if args.jira_password:
        conf['jira_password'] = args.jira_password
    if args.jira_regex:
        conf['jira_regex'] = args.jira_regex

    bot = JiraJabberBot(conf['username'], conf['password'])
    bot.join_room(conf['channel'])
    bot.serve_forever()

if __name__ == "__main__":
    main()
