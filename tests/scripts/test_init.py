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

    runner = CliRunner()
    result = runner.invoke(tomb, ['clean_tmp', '/tmp'])
    assert result.exit_code == 0
