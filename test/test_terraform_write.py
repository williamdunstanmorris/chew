#  Copyright (c) 2019 William Morris. Don't Steal Me.
from chew.model import Terraform


def terraform_file():
    tf = Terraform()
    tf.generate()


terraform_file()
