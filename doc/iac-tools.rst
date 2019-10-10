IaC Management Tools
====================

Terraform
---------

With Terraform, you are spinning up and provisioning instances of machines - like an EC2 instance for AWS. The benefit of Terraform is that it's reproducible, and you can share modules for common infrastructure. The leading files you are concerned with in Terraform use ".tf" extensions, but can be segregated into multiple ".tf" files.

Let's take a look at how you could create these files with chew.

.. note::

  To work with terraform, you will need to download Terraform from the official *Hashicorp* website. You will also need an AWS account from the official *Amazon Web Services (AWS)* website.

.. code-block:: python

    from chew import terraform

    def generate_gitlab_ci_script():

      # Instance
      s = Terraform()

      # Generate our script.
      s.generate()

    generate_gitlab_ci_script()

This will create the simplest version - of a terraform script, but this would not work. Lets add a stage, and then two jobs to our stage.

.. code-block:: python

    from chew import terraform

    def generate_gitlab_ci_script():

      # Instance
      s = Terraform('Script', 'Copyright (c) 2019 William Morris')

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

    from chew import terraform
