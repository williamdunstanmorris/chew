Getting Started
===============

Chew requires Python 3.5 or later to run. Once you’ve installed Python 3, install chew using pip:

.. code-block:: python

    python3 -m pip install chew

Once chew is installed, verify it is working by creating a `test.py` file and run this short script:

.. code-block:: python

    from chew.model import GitlabCIPipeline

    def test_generate_gitlab_script():
        s = GitlabCIPipeline('Test Script', 'Copyright (c) 2019 Chew')
        s.generate('.gitlab-ci.yml', s)


    test_generate_gitlab_script()


.. note::

   This should run absolutely fine, but if not, please raise an issue on Github!

The table of contents to the left of you has been divided into separate sections, each covering different tech and tools used in the DevOps world. Because each tool operates differently, with different syntax, there are obvious differences in the way that python classes have been designed. Have a look at the technology you are interested in, and follow the example given in each to get an understanding of how you can start your first script or config file with python. Have fun!



