import click


@click.command()
@click.option('--name', prompt='What is the project name?',
              help='The name of the project you want to create.')
def tomb(project_name):
    """
    CLI utility for managing tomb
    """
    for x in range(3):
        click.echo('Hello %s!' % project_name)
