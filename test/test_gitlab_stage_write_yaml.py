#  Copyright (c) 2019 William Morris. Don't Steal Me.

from chew.model import GitlabCIScript
from ruamel.yaml import YAML
import sys

def gitlab_stage_write_yaml():

    str_script = {'text': ['# script']}
    s = GitlabCIScript('GitlabTestScript', 'Copyright (c) 2019 Mister. Chew')
    # s.generate('.gitlab-ci.yml')

    s.add_stage('config')
    s.add_stage('build')
    s.add_stage('pages')
    s.remove_stage('config')
    s.remove_stage('build')
    # s.remove_stage('pagasdfes')
    vars = s.global_variables()

    # s.stages['config'].add_job(name='.config')

    # todo: how is an object being accessed?
    # print(yaml.dump({'stages': ['build', 'config', 'pages']}, default_flow_style=False))
    # print(yaml.dump(str_script, default_flow_style=False))

    # s.generate(s)
#
# yaml = YAML()
# yaml.register_class(TestGitlabWriter)
# yaml.register_class(TestGitlabWriterAgain)
#
# data = yaml.load("")
# data['abc'].yaml_add_eol_comment('comment 4', 1)  # takes column of comment 1
#
#
# print(yaml.dump([TestGitlabWriter(),TestGitlabWriterAgain()], sys.stdout))


gitlab_stage_write_yaml()
