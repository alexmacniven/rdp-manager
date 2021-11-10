"""test_rdp_manager"""
import subprocess


from click.testing import CliRunner
from pytest_mock import MockFixture

from rdp_manager import __version__
from rdp_manager.rdp_manager import connect, connect_command


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_connect(mocker: MockFixture) -> None:
    """Test connect."""
    mocker.patch("subprocess.run")
    connect("1.1.1.1")
    subprocess.run.assert_called_with(  # pylint: disable=no-member
        ["mstsc", "/v", "1.1.1.1"], check=True
    )
    # subprocess.run is mocked so assert_called_with is valid


def test_connect_command(mocker: MockFixture):
    """Test connect_command."""
    _connect = mocker.patch("rdp_manager.rdp_manager.connect")

    runner = CliRunner()
    runner.invoke(connect_command, "1.1.1.1")

    _connect.assert_called_with("1.1.1.1")
