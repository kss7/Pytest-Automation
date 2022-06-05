from Pytest_topics.utils.myconfigparser import *
from Pytest_topics.utils.ConfigFileParser import ConfigFileParser

config = ConfigFileParser('prod.ini')

def test_getgmailurl():
    print(getGmailUrl())

def test_getoutlookurl():
    print (config.getOutlookUrl())