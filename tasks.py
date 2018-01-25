import os
import json
import shutil
import webbrowser

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'leicarentals.json'), 'r') as fp:
    APP_SETTINGS = json.load(fp)

APP = os.path.join(HERE, APP_SETTINGS['app_name'])
CREATE_APP= os.path.join(APP, 'leicarentals.py')
REQUIREMENTS = os.path.join(APP, 'requirements', 'dev.txt')


def _run_npm_command(ctx, command):
    os.chdir(APP)
    ctx.run('npm {0}'.format(command), echo=True)
    os.chdir(HERE)


@task
def build(ctx):
    ctx.run('leicarentals {0} --no-input'.format(HERE))
    _run_npm_command(ctx, 'install')
    _run_npm_command(ctx, 'run build')


@task
def clean(ctx):
    if os.path.exists(APP):
        shutil.rmtree(APP)
        print('Removed {0}'.format(APP))
    else:
        print('App directory does not exist. Skipping.')


def _run_flask_command(ctx, command):
    ctx.run('FLASK_APP={0} flask {1}'.format(CREATE_APP, command), echo=True)


@task(pre=[clean, build])
def test(ctx):
    ctx.run('pip install -r {0} --ignore-installed'.format(REQUIREMENTS),
            echo=True)
    _run_npm_command(ctx, 'run lint')
    os.chdir(APP)
    _run_flask_command(ctx, 'lint')
    _run_flask_command(ctx, 'test')

@task
def readme(ctx, browse=False):
    ctx.run("rst2html.py README.rst > README.html")
    if browse:
        webbrowser.open_new_tab('README.html')

