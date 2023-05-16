import typer  # use typer.run and typer.Argument


def sum_numbers(a: int, b: int):
    """Sums two numbers"""
    return a + b


def main(
    a: int = typer.Argument(1, help="The value of the first summand"),
    b: int = typer.Argument(2, help="The value of the second summand"),
):
    """
    CLI that allows you to add two numbers
    """
    print(sum_numbers(a, b))


if __name__ == "__main__":
    typer.run(main)
