from typing import List

import pytest
import typer
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_app(runner: CliRunner):
    result = runner.invoke(app, ["Nishant"])
    assert result.exit_code == 0
    assert "Hello Nishant!" in result.stdout


@pytest.mark.parametrize(
    "expected_descriptions",
    [
        (
            [
                "CLI that allows you to greet a person.",
                "The name of the person to greet.",
            ]
        ),
    ],
)
def test_app_help(expected_descriptions: List[str], runner: CliRunner) -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for description in expected_descriptions:
        assert description in result.stdout
