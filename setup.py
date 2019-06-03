from setuptools import setup

setup(
    name='helloworld-cli',
    version='1.0.0',
    packages=['helloworld'],
    entry_points={
        'console_scripts': [
            'helloworld = helloworld.__main__:main'
        ]
    }
)
