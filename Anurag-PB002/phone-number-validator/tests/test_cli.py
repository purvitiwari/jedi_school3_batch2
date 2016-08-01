import pytest
from click.testing import CliRunner
from phone_number_validator import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_with_input(runner):
    number = '+917405352413'
    result = runner.invoke(cli.main, input=number)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output == 'Phone Number: {0}\nValid\n'.format(number)


def test_cli_with_long_option(runner):
    number = '+917405352413'
    result = runner.invoke(cli.main, ['--phone-number', number])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output == 'Valid\n'


def test_cli_with_short_option(runner):
    number = '+917405352413'
    result = runner.invoke(cli.main, ['-p', number])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output == 'Valid\n'


def test_cli_with_number_starting_from_0():
    assert cli.is_number_valid('07405352413') == True


def test_cli_with_number_starting_from_plus():
    assert cli.is_number_valid('+917405352413') == True


def test_cli_with_10_digit_number():
    assert cli.is_number_valid('7405352413') == True


def test_cli_with_10_digit_invalid_number():
    assert cli.is_number_valid('6789281278') == False
