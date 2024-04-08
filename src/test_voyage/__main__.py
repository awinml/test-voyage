"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Test Voyage."""


if __name__ == "__main__":
    main(prog_name="test-voyage")  # pragma: no cover
