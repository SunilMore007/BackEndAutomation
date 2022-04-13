import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('APIAutomation/properties.ini')  # to read the config file
    config['API'] = {'endpoint': 'http://216.10.245.166'}

    return config


def getPassword():
    password = "Sayalikumari@123"
    return password


def getUsername():
    userName = "SunilMore007"
    return userName
