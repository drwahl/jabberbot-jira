#!/usr/bin/env python

from ConfigParser import SafeConfigParser
import os

def read_configuration():
    """
    Read configurations options from a config file.
    """

    # init our config dict
    configuration = dict(
        username = None,
        password = None,
        channel = None,
        nickname = None,
        jira_server = None,
        jira_username = None,
        jira_password = None,
        jira_regex = None,
    )

    # search in some known places for our config file
    parser = SafeConfigParser()
    if os.path.isfile('/etc/jabberbot-jira/jabberbot-jira.conf'):
        config = '/etc/jabberbot-jira/jabberbot-jira.conf'
    elif os.path.isfile('./jabberbot-jira.conf'):
        config = './jabberbot-jira.conf'
    elif os.path.isfile('../conf/jabberbot-jira.conf'):
        config = '../conf/jabberbot-jira.conf'
    else:
        print 'Config file not found.  Assuming params were pass from CLI...'
        return configuration

    # load the config file and try to find values
    parser.read(config)
    try:
        configuration['username'] = parser.get('default', 'username')
    except ConfigParser.NoOptionError:
        pass
    try:
        configuration['password'] = parser.get('default', 'password')
    except ConfigParser.NoOptionError:
        pass
    try:
        configuration['channel'] = parser.get('default', 'channel')
    except ConfigParser.NoOptionError:
        pass
    try:
        configuration['nickname'] = parser.get('default', 'nickname')
    except ConfigParser.NoOptionError:
        pass
    try:
        configuration['jira_server'] = parser.get('default', 'jira_server')
    except ConfigParser.NoOptionError:
        pass
    try:
        configuration['jira_username'] = parser.get('default', 'jira_username')
    except ConfigParser.NoOptionError:
        pass
    try:
        configuration['jira_password'] = parser.get('default', 'jira_password')
    except ConfigParser.NoOptionError:
        pass
    try:
        configuration['jira_regex'] = parser.get('default', 'jira_regex')
    except ConfigParser.NoOptionError:
        pass

    # provide our results to the boss
    return configuration
