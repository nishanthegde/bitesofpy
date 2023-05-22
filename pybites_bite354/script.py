import typer


def sum_numbers(a: int, b: int):
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
    c: int = typer.Option(None),
):
    """CLI that allows you to add two numbers"""

    sum_ab = sum_numbers(a, b)

    if c is None:
        print(f"The sum is {sum_ab} and c is None")
    elif c < sum_ab:
        print(f"The sum is {sum_ab} and c is smaller")
    else:
        print(f"The sum is {sum_ab} and c is not smaller")


if __name__ == "__main__":
    typer.run(main)
