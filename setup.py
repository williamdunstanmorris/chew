from setuptools import setup

setup(
    name = 'chew',
    version = '0.1.0',
    packages = ['chew'],
    entry_points = {
        'console_scripts': [
            'chew = chew.__main__:main'
        ]
    }, install_requires=['PyYAML'])
