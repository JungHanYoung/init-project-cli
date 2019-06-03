import os
import sys

from PyInquirer import prompt, Separator
from .util_function import create_and_cli, github_init_project
import click

node_questions = [
    {
        'type': 'list',
        'message': 'choose nodejs CLI',
                'name': 'CLI',
                'choices': [
                        Separator('++++ Node CLI ++++'),
                        {
                            'name': 'Create React App',
                            'value': 'cra'
                        },
                    {
                            'name': 'general init (Yarn)',
                            'value': 'yarn'
                            }
                ]
    }
]

python_questions = [
    {
        'type': 'list',
        'message': 'choose python CLI',
                'name': 'CLI',
                'choices': [
                        Separator('++++ Python CLI ++++'),
                        {
                            'name': 'django',
                            'value': 'django'
                        }
                ]
    }
]

node_cli_dict = {
    'cra': 'npx create-react-app .',
    'yarn': 'yarn init -y'
}

python_cli_dict = {
    'django': 'django-admin startproject {}'
}


def node_cli(name):
    answer = prompt(node_questions)
    os.system(create_and_cli(name, node_cli_dict[answer['CLI']]))


def python_cli(name):
    answer = prompt(python_questions)
    # Django
    if answer['CLI'] == 'django':
        os.system('django-admin startproject {}'.format(name))


def create_new_remote_repo(name):
    answer = prompt([
        {
                    'type': 'list',
                    'message': 'choose remote repo',
                    'name': 'remote_repo',
                    'choices': [
                            Separator('---- remote repository ----'),
                            {
                                'name': 'github',
                                'value': 'github'
                            },
                        {
                                'name': 'bitbucket',
                                'value': 'bitbucket'
                        }
                    ]
                    }
    ])
    if answer['remote_repo'] == 'github':
        if github_init_project(name):
            click.echo('github project init success')
        else:
            click.echo('something broken..')
