import yaml
class user():
    piUrlUI         = None
    piUserNotValid  = None
    piPassNotValid  = None
    piUserValid     = None
    piPassValid     = None

    def __init__(self, env):
        with open('config.yaml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        self.piUrlUI        =  str(config[env]['UI']['urlUI'])
        self.piUserNotValid =  str(config[env]['UI']['userNotValid'])
        self.piPassNotValid =  str(config[env]['UI']['passNotValid'])
        self.piUserValid    =  str(config[env]['UI']['userValid'])
        self.piPassValid    =  str(config[env]['UI']['passValid'])