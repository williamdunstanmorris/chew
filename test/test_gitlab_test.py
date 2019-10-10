#  Copyright (c) 2019 William Morris. Don't Steal Me.
from chew.model import GitlabCIPipeline


def generate_gitlab_script():
    s = GitlabCIPipeline('Script', 'Copyright (c) 2019 William Morris')
    # you can optionally flag all jobs to cover multiple OS systems at script level, but this is overridden at stage
    # instance level.
    s.multi_os({'linux', 'macos', 'windows'})
    # todo: alternative, dirty way to add jobs quickly.
    # s.add_stage({s.add_job('this'), s.add_job('that')})

    # Define stages
    # more references.
    # config = GitlabStage('config')
    # config.define_job('config_windows', 'master', config_script)

    s.add_stage('config')
    s.add_stage('build')
    s.add_stage('pages')

    config_script = {'echo Hello World',
                     'echo This is Chew.',
                     'echo Hello You.'}

    # Define config jobs
    s.stages['config'].new_job('config_windows', 'master', config_script)
    # Append new attributes to a job:
    s.stages['config'].job('config_windows').create_var()
    # This will override the operating system for a specific job, flagging it to be ONLY be on linux.
    s.stages['config'].job('config_windows').set_os('linux')

    s.generate('.gitlab-ci.yml', s)


generate_gitlab_script()

