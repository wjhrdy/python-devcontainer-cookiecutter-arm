import click.testing
import pytest
from {{cookiecutter.etl_package_name}} import {{cookiecutter.etl_package_name}}

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_main_succeeds(runner):
    result = runner.invoke({{cookiecutter.etl_package_name}}.main,["2023-01-01"])
    assert result.exit_code == 0
    