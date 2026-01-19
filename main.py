def hello_world(name: str = "World") -> None:
    """
    Print a hello world greeting message.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        None

    Examples:
        >>> hello_world()
        Hello, World!
        >>> hello_world("Alice")
        Hello, Alice!
    """
    print(f"Hello, {name}!")


def main() -> None:
    """Main entry point for the hello world program."""
    hello_world()


if __name__ == "__main__":
    main()
