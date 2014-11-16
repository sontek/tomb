import pytest
import logging
import os

from click.testing import CliRunner
logging.basicConfig()
logger = logging.getLogger(__name__)


@pytest.mark.unit
def test_tomb_new_correct():
    from tomb.scripts import tomb

    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(tomb, ['new', 'test_package'])
        files = os.listdir('.')

        assert result.exit_code == 0
        assert 'test_package' in files
        assert 'tox.ini' in files


@pytest.mark.unit
def test_tomb_new_missing_package():
    from tomb.scripts import tomb

    runner = CliRunner()
    result = runner.invoke(tomb, ['new'])
    assert result.exit_code == 2


@pytest.mark.unit
def test_tomb_clean_tmp():
    from tomb.scripts import tomb

    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('hello.txt~', 'w') as f1:
            f1.write('Hello World!')

        with open('hello.pyc', 'w') as f2:
            f2.write('Hello World!')

        with open('hello.pyo', 'w') as f3:
            f3.write('Hello World!')

        os.makedirs('__pycache__')

        with open('__pycache__/hello.txt', 'w') as f4:
            f4.write('Hello World!')

        assert len(os.listdir('.')) == 4
        result = runner.invoke(tomb, ['clean_tmp'])

        assert result.exit_code == 0
        assert len(os.listdir('.')) == 0
