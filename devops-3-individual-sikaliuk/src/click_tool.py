import click


@click.group()
def cli() -> None:
    "набір CLI-команд"
    pass


@cli.command()
@click.option("--name", required=True, help="ім'я")
def say(name: str) -> None:
    "друкує ім'я, якщо воно не починається з p/P."
    if name and name[0].lower() == "p":
        click.echo("Ім’я не підходить")
        return

    click.echo(name)


if __name__ == "__main__":
    cli()
