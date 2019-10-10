# todo: should be abstract?
import datetime

class Script(object):

    def __init__(self, name, copyright_):
        self.name = name
        self.copyright = copyright_
        self.datetime = datetime.datetime.now()


