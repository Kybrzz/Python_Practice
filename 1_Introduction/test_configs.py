import os, sys  # unused on purpose for Ruff to flag


def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(2, 3) == 5  # pytest will collect this in this file


def main():
    # Intentional type bug for Pyright
    total = add(2, "3")
    print("Total:", total)  # sloppy spacing for Black to fix


if __name__ == "__main__":
    main()
