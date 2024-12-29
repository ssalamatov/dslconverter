from .generate import generate

from .parser import parse


if __name__ == "__main__":
    generate(parse().template)
