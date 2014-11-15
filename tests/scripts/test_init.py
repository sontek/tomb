import pytest
from click.testing import CliRunner


@pytest.mark.unit
def test_tomb_new_correct():
    from tomb.scripts import tomb

    runner = CliRunner()
    result = runner.invoke(tomb, ['new', 'test_package'])
    assert result.exit_code == 0


@pytest.mark.unit
def test_tomb_new_missing_package():
    from tomb.scripts import tomb

    runner = CliRunner()
    result = runner.invoke(tomb, ['new'])
    assert result.exit_code == 2


@pytest.mark.unit
def test_tomb_clean_tmp():
    from tomb.scripts import tomb
    import os

    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('hello.txt~', 'w') as f1:
            f1.write('Hello World!')

        with open('hello.pyc', 'w') as f2:
            f2.write('Hello World!')

        with open('hello.pyo', 'w') as f3:
            f3.write('Hello World!')

        assert len(os.listdir('.')) == 3

        result = runner.invoke(tomb, ['clean_tmp'])
        assert result.exit_code == 0
        assert len(os.listdir('.')) == 0