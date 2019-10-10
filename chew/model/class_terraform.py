#  Copyright (c) 2019 William Morris. Don't Steal Me.

class _Resource(object):

    def __init__(self, resource_name: str, ami: str):
        self.resource_name = name


class _Provider(object):

    def __init__(self, provider_name: str):
        self.provider_name = provider_name


class _Region(object):
    pass


class Terraform(object):

    def __init__(self, provider: _Provider, profile: str, region: _Region):
        self.provider = provider
        self.profile = profile
        self.region = region

    @staticmethod
    def region_lookup():
        # todo: lookup table to return regions as constants
        provider_name = "aws"
        return _Provider(provider_name)

    def generate(self):
        """"""

        """
        provider "aws" {
          profile    = "default"
          region     = "us-east-1"
        }

        resource "aws_instance" "example" {
          ami           = "ami-2757f631"
          instance_type = "t2.micro"
        }
        """
        pass
