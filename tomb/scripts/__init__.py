import click
from invoke import run


@click.group()
@click.pass_context
def tomb(ctx):
    """
    CLI utility for managing tomb
    """
    pass


@tomb.command()
@click.argument('project_name')
def new(project_name):
    """
    Generates a new project from the default template
    """
    for x in range(3):
        click.echo('Hello %s!' % project_name)


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
