#  Copyright (c) 2019 William Morris. Don't Steal Me.
from .script import Script

from typing import Union

import sys
import yaml

class JenkinsNode(object):
    pass


class JenkinsStage(object):

    def __init__(self, name):
        self.name = name
        self.jobs = {}

    def define_job(self, job_name, job_tag, job_script):
        # logic for correct job name - append '.' to script too.
        # new_job = JenkinsStep(job_name, job_tag, job_script)
        # self.jobs.pop(self, new_job)
        pass


class JenkinsStep(object):
    pass


class JenkinsPipeline(Script):

    def __init__(self, name: str, copyright_: str):
        super().__init__(name, copyright_)
        self.name = name
        self.copyright = copyright_
        # todo, remove pipeline, it is only needed at _construct level.
        self.pipeline = {'pipeline': {'options': {}, 'stages': {}}}
        self.stages = {}

    def __repr__(self):
        return 'JenkinsPipeline({}, {}, {})'.format(self.name, self.copyright, self._construct(self.pipeline))

    @staticmethod
    def _construct():
        """Private in-house to merge all members into one dictionary"""
        # todo: merge all dictionaries
        pipeline = {'pipeline': {'options': {}, 'stages': {}}}
        pass

    def generate(self, name):

        file = open(name, "w+")

        try:
            with open(name, 'w') as writer:
                if self.name and self.copyright:
                    writer.write('/*\n' + self.name + ", " + self.copyright + "\n*/\n\n")
                if self.name and not self.copyright:
                    writer.write('/*\n' + self.name + "\n*/\n\n")
                if self.copyright and not self.name:
                    writer.write('/*\n' + self.copyright + "\n*/\n\n")

                # todo: remove for, it's useless.
                for key, value in self.pipeline.items():
                    if key == "pipeline":
                        writer.write(key)
                        writer.write(" {\n")
                        writer.write("\tagent any\n")
                        writer.write("\toptions {\n")
                        writer.write("\t\tskipStagesAfterUnstable()\n")


                        writer.write("}\n")

                    print(key, value)
        finally:
            file.close()

    """
    pipeline {
        agent any
        options {
            skipStagesAfterUnstable()
        }
        stages {
            stage('Build') {
                steps {
                    sh 'make'
                }
            }
            stage('Test'){
                steps {
                    sh 'make check'
                    junit 'reports/**/*.xml'
                }
            }
            stage('Deploy') {
                steps {
                    sh 'make publish'
                }
            }
        }
    }
    """

    def add_stage(self, stage: Union[JenkinsStage, str]):
        if type(str) is str or isinstance(str, basestring):
            new_stage = JenkinsStage(stage)
            self.pipeline['stages'].append(new_stage)
            print(self.pipeline)
        pass

    def remove_stage(self, stage):
        pass
