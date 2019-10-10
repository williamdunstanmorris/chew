#  Copyright (c) 2019 William Morris. Don't Steal Me.
from chew.model import JenkinsPipeline


def jenkins_stage_write_yaml():
    # internal test scripts
    pipeline = JenkinsPipeline('JenkinsTestScript', 'Copyright (c) 2019 Mister. Chew')
    # print(pipeline.__repr__())
    pipeline.generate('Jenkinsfile')


jenkins_stage_write_yaml()
