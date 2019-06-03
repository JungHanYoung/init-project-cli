
from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from selenium import webdriver
import os
import sys
import click
from .generate_function import node_cli, python_cli, create_new_remote_repo

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'confirm',
        'name': 'isNew',
        'message': 'Is new project?',
        'default': False
    },
    {
        'type': 'list',
        'message': 'choose language',
        'name': 'language',
        'choices': [
            Separator('=== language ==='),
            {
                'name': 'nodejs (javascript)',
                'value': 'node'
            },
            {
                'name': 'C lang',
                'value': 'c'
            },
            {
                'name': 'python',
                'value': 'python'
            }
        ]
    },
    {
        'type': 'confirm',
        'message': 'Do you want to initialize remote project?',
        'name': 'isRemoteRepo',
        'default': False
    }
]


@click.command()
@click.argument('name')
# @click.option('--greeting', '-g')
def main(name):
    answers = prompt(questions, style=style)

    # if answers['isNew']:
    #     os.system('mkdir {}'.format(name))
    #     click.echo("프로젝트 폴더를 생성하였습니다.")

    # answers -> language, CLI
    if answers['language'] == 'node':
        node_cli(name)
    elif answers['language'] == 'python':
        python_cli(name)

    if answers['isRemoteRepo']:
        create_new_remote_repo(name)
    # click.echo("{}, {}".format(greeting, name))
    click.echo("프로젝트 초기화가 완료되었습니다.")

# def main():
#     print('in main')
#     args = sys.argv[1:]
#     print('count of args :: {}'.format(len(args)))

#     driver = webdriver.Chrome(
#         '/Users/hanyoungjeong/Documents/workspace_example/inflearn_crawling/chromedriver')

#     # 웹 자원을 로드하기 위해 3초까지 기다린다.
#     driver.implicitly_wait(3)

#     driver.get('https://github.com/login')

#     driver.find_element_by_name('login').send_keys('8735132@naver.com')
#     driver.find_element_by_name('password').send_keys('Jhy5968!@#')

#     driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[4]').click()

#     driver.find_element_by_xpath(
#         '/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a').click()

#     driver.find_element_by_name('repository[name]').send_keys('hello_world~')
#     driver.find_element_by_name(
#         'repository[description]').send_keys('Hello~ Description')

#     # print(driver.find_element_by_css_selector('button[type="submit"]'))
#     # print(driver.find_element_by_selector('button[type="submit"]'))
#     driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button').click()

#     driver.quit()

#     print('GitHub Project setup')

    # for arg in args:
    #     print('passed argument :: {}'.format(arg))


if __name__ == 'main':
    main()
