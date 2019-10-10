# Copyright (c) 2019 William Morris. Don't Steal Me.
from .script import Script

# 3rd party
from ruamel.yaml import YAML
import sys
import json
import warnings
from os import path
from collections import defaultdict


class GitlabCIPipeline(Script):

    def __init__(self, name: str, copyright_: str):
        super().__init__(name, copyright_)

        # SequenceProcessorInterface.__init__(self, arguments)
        # objs = []
        # for objNode in arguments.iter( 'object' ):
        #     data = objNode.attrib['data'].replace( '\'', '\"' )
        #     obj = loads( data )
        #     objs.append( obj )
        # sortedObjs = sorted( objs, key=lambda k: int(k['id']) )
        # self.additionalObjects = sortedObjs
        # create blank template pipeline
        # sort jobs by declared stages
        # if OS's defined, sort jobs within stages by OS
        self.stages = defaultdict(dict)
        self.os = {}
        self.variables = {}

    @property
    def global_variables(self):
        if not self.variables:
            warnings.warn("You have not set any global variables. Have a look at set_global_variable(...) functions.")
            return
        for item, amount in self.variables:
            return "{} ({})".format(item, amount)

    # todo: implement format for dict
    def __repr__(self):
        return "GitlabCIScript('{}', '{}')".format(self.stages, self.os)

    def __str__(self):
        return '{} - {}'.format(self.stages, self.os)

    def stages(self, key):
        return self.stages[key]

    def generate(self, script):

        yaml = YAML()
        data = yaml.load(yaml_str)
        data.insert(1, 'last name', 'Vandelay', comment="new key")
        yaml.dump(data, sys.stdout)

        # representation in string format.
        self.name = '# ' + self.name
        docker = open(name, "w+")

        try:
            with open(name, 'w') as writer:
                writer.write(
                    yaml.dump(data, sys.stdout))
                print(yaml.dump(data, sys.stdout))
        finally:
            docker.close()

    def add_stage(self, name: str):
        # does the following stage name contain any of the following keywords
        keywords = json.loads(open(path.abspath(path.join(path.dirname(__file__), "..", "data", "reserved_gitlab_keywords.json"))).read())

        for keyword in keywords:
            if name == keyword:
                raise Exception("Stage name %s you have chosen is a reserved keyword in GitlabCI: [%s]", keyword, keywords)

        for current_stage in self.stages:
            if name == current_stage:
                raise Exception("This stage already exists. Your registered stages are: [%s]", self.stages['stages'])
        self.stages.
        # self.stages.append(GitlabStage(name))

    def remove_stage(self, name: str):
        if name not in self.stages['stages']:
            raise Exception("This stage name does not exist. Stages that are currently registered are: " + self.stages[
                'stages'].__str__())
        self.stages['stages'].remove(name)
        print(self.stages)

    def artifact_path(self):
        pass

    # todo: this should be defined at job level too, but this function could act as a flag, and fill.
    # todo: this should also be prepended to the beginning of every job, as = .os_stage_job_name
    def multi_os(self, os):
        self.os = os

    # append '&'
    def make_this_template(self):
        pass


class GitlabJob(object):

    def __init__(self, name, tags, script):
        self.name = name
        self.variable = {}
        # can be multi-indented
        self.only = {'only': ['master', 'develop']}
        self.tags = tags
        self.extends = {}
        # todo: call job.add_script('echo "Hello World"), but user MUST do it once.
        self.script = script
        self.artifact_path = {}
        self.isTemplate = False
        # todo: set an extends policy here.

        """
        .runner_linux18_python_36_template: &runner_linux18_python_36
          only:
            variables:
              - $RUNNER_LINUX18_PYTHON_36 == "ON"
          tags:
            - linux18-py36

        # Specifies the CI branches once and for all jobs
        .default_config:
          only:
            - master
            - develop
            - feature/experimental-ci

        #
        # Templates for CMake commands - Windows and Unix
        #

        # Config-and-generate stage template
        .config_and_generate_windows_template:
          extends: .default_config
          script:
            - SET  CMAKE_OPTIONS_ALL=-DCMAKE_BUILD_TYPE=Release
                                     -DBOOST_ROOT=%BOOST_ROOT%
                                     %CMAKE_OPTIONS%
            - cmake -E remove_directory %BUILD_FOLDER%
            # folllowing line is for debug purposes only
            - echo "%GENERATOR%" \n\n %CMAKE_OPTIONS% \n\n %CMAKE_OPTIONS_ALL%
            - cmake -E make_directory %BUILD_FOLDER%
            - cmake -E chdir %BUILD_FOLDER%/
              cmake -G "%GENERATOR%" %CMAKE_OPTIONS_ALL% ..
          artifacts:
            paths:
              - "%BUILD_FOLDER%/"

        """


# todo: inherit from GitlabCI script?
class GitlabStage(object):

    def __init__(self, name):
        self.name = name
        # array of GitlabJobs
        self.jobs = {}

    def define_job(self, job_name, job_tag, job_script):
        # logic for correct job name - append '.' to script too.
        new_job = GitlabJob(job_name, job_tag, job_script)
        self.jobs.pop(self, new_job)
