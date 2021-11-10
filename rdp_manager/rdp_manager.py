"""rdp_manager.rdp_manager"""
import subprocess

import click

# Typing.
IPAddress = str


def connect(remote_address: IPAddress) -> None:
    """Invoke a connection to `remote_address` with powershells mstsc."""
    subprocess.run(["mstsc", "/v", remote_address], check=True)


@click.command(name="connect")
@click.argument("address", nargs=1, required=True)
def connect_command(address: IPAddress) -> None:
    """Connect to a remote address"""
    connect(address)
