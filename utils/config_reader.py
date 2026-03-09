import configparser

config = configparser.ConfigParser()
config.read("config/qa.ini")

def get_base_url():
    return config.get("environment", "base_url")

def get_browser():
    return config.get("environment", "browser")