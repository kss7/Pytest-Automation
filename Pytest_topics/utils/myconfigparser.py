import configparser
from pathlib import Path

cfgFile = 'qa.ini'
cfgFileDirectory = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)

config.read(CONFIG_FILE)

def getGmailUrl():
    return (config['gmail']['url'])

def getGmailUser():
    return (config['gmail']['user'])

def getGmailPass():
    return (config['gmail']['pass'])

print (getGmailUrl())