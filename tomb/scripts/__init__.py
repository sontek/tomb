import click
import os

from invoke import run
from tomb.scaffolds.base import BaseTombTemplate


@click.group()
@click.pass_context
def tomb(ctx):
    """
    CLI utility for managing tomb
    """
    pass


class DummyOptions(object):
    simulate = None
    interactive = True
    overwrite = False


class DummyCommand(object):
    options = DummyOptions()
    verbosity = None


@tomb.command()
@click.argument('project_name')
@click.option(
    '--output-dir',
    default='.',
    help='Location for the project to be created'
)
def new(project_name, output_dir):
    """
    Generates a new project from the default template
    """
    scaffold = BaseTombTemplate('BaseTombTemplate')

    if output_dir == '.':
        output_dir = os.getcwd()

    vars = {
        'package': project_name,
    }

    scaffold.run(DummyCommand(), output_dir, vars)


@tomb.command()
@click.argument('path', default='.')
def clean_tmp(path):
    """
    Deletes any .pyc, .pyo, or files ending with ~
    """
    patterns = (
        '*.pyc',
        '*.pyo',
        '*~',
        '__pycache__',
    )

    for pattern in patterns:
        tmpl = 'find %s -name %s -exec rm -rf {} +'
        cmd = tmpl % (path, pattern)
        run(cmd)
