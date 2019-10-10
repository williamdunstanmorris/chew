import fire
import yaml
import warnings
import os, sys

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Monster(tuple):
    yaml_tag = u'!Monster'

    def __new__(cls, name, hp):
        return tuple.__new__(cls, [name, hp])

    # def __init__(self, name, hp, ac, attacks):
    #     self.name = name
    #     self.hp = hp
    #     self.ac = ac
    #     self.attacks = attacks

    def __repr__(self):
        return "Dice(%s, %s)" % self

    # if called without filename, use a default name.
    # if called, and file does not exist in directory, create
    # if called, and file already exists in directory, raise warning to proceed within CLI
    # if called, and file is named differently, create
    @staticmethod
    def generate(name):

        if os.path.exists('.travis-ci.yml'):
            input(name + ' already exists. Would you like to overwrite it? [y/n] ')

            yes = {'yes', 'y', 'ye', ''}
            no = {'no', 'n'}

            choice = input().lower()
            if choice in no:
                fire.Fire(exit(1))
            elif choice in yes:
                pass
            else:
                sys.stdout.write("Please respond with 'yes' or 'no'")

        docker = open(name, "w+")

        try:
            with open(name, 'w') as writer:
                writer.write(
                    yaml.dump(Monster(3, 6), default_flow_style=False))
        finally:
            docker.close()

    # use this declarator to use the class as the first instance, rather than the instance.
    @classmethod
    def class_rep(cls, dumper, node):
        return dumper.represent_scalar(cls.yaml_tag, u'!dice', u'%sd%s' % node)

    def parse(self, filename):
        with open(filename, 'r') as stream:
            try:
                self.data = yaml.safe_load(stream)
                print(self.data)
            except yaml.YAMLError as YAMLException:
                print(YAMLException)


class Chew(object):
    """Main pipeline class"""

    def __init__(self):
        self.monster = Monster(name='Cave spider', hp=[2, 6])


if __name__ == '__main__':
    fire.Fire(Chew)
