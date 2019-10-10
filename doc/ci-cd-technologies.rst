CI/CD Technologies
==================

Gitlab-CI
---------

With Gitlab, you mainly deal with stages, and within a stage, you have jobs that run in parallel. Therefore, when you create stages, you will be able to create jobs using them. You can then access more specific functions specific to jobs, stages or the entire pipeline itself. Let's take a look.

First, create an instance of our pipeline, and call generate. You can specify a filename if you want:

.. code-block:: python

    from chew import gitlab_ci

    def generate_gitlab_ci_script():

      # Instance
      s = GitlabCIPipeline('Script', 'Copyright (c) 2019 William Morris')

      # Generate our script.
      s.generate()

    generate_gitlab_ci_script()

This will create the simplest version - a hello world - version of the gitlab script. Lets add a stage, and then two jobs to our stage.

.. code-block:: python

    from chew import gitlab_ci

    def generate_gitlab_ci_script():

      # Instance
      s = GitlabCIPipeline('Script', 'Copyright (c) 2019 William Morris')

      # Add a new stage.
      s.add_stage('config')

      # Add two jobs to our new stage above, that run in parallel.
      s.stages['config'].new_job('echo_first', 'master', "echo Hello World!")
      s.stages['config'].new_job('echo_second', 'master', "echo Hello Mars!")

      # Generate our script.
      s.generate()

    generate_gitlab_ci_script()


With everything together, it looks like this:

.. code-block:: python

    from chew import gitlab_ci

    def generate_gitlab_ci_script():

      s = GitlabCIPipeline('Script', 'Copyright (c) 2019')
      # you can optionally flag all jobs to cover multiple OS systems at script level, but this is overridden at stage
      # instance level.
      s.multi_os({'linux', 'macos', 'windows'})

      s.add_stage('config')

      config_script = {'echo Hello World',
                       'echo This is Chew.',
                       'echo Hello You.'}

      # Define config jobs
      s.stages['config'].new_job('config_windows', 'master', config_script)
      # Append new attributes to a job:
      s.stages['config'].job('config_windows').create_var()
      # This will override the operating system for a specific job, flagging it to be ONLY be on linux.
      s.stages['config'].job('config_windows').set_os('linux')

      s.generate('.gitlab-ci.yml')

    generate_gitlab_ci_script()

Jenkins
-------
