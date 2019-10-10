#  Copyright (c) 2019 William Morris. Don't Steal Me.

import yaml
import json


class Monster(yaml.YAMLObject):

    yaml_tag = u'!Monster'

    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)


# yaml.safe_load("""
# --- !Monster
# name: Cave spider
# hp: [2,6]    # 2d6
# ac: 16
# attacks: [BITE, HURT]
# """
# )

# print(yaml.dump(instance.name))


class Dice(tuple):
    def __new__(cls, a, b):
        return tuple.__new__(cls, [a, b])

    def __repr__(self):
        return "Dice(%s,%s)" % self


print(yaml.dump(Dice(3,6)))


def dice_representer(dumper, data):
    return dumper.represent_scalar(u'!dice', u'%sd%s' % data)


yaml.add_representer(Dice, dice_representer)

print(yaml.dump(Dice(3,6)))


def dice_constructor(loader, node):
    value = loader.construct_scalar(node)
    a, b = map(int, value.split('d'))
    return Dice(a, b)


yaml.add_constructor(u'!dice', dice_constructor)

