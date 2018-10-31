import pytest
from pgbackup import cli

url = "postgres://bob@example.com:5432/db_one"

def test_parser_without_driver():
    """
    Without a driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])


def test_parser_with_driver():
    """
    the parser will exit if it receives a driver without a destination
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver","local"])


def test_parser_with_driver_and_destination():
    """
    the parser will not exit if it receives a driver and a destination
    """
    parser = cli.create_parser()

    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.url == url
    assert args.drvier == 'local'
    assert args.destination == '/some/path'
