import sys
from secgpt.cli import parse_arguments

def test_parse_arguments():
    test_args = ["prog", "-t", "example.com", "-p", "22,80,443", "--verbose"]
    sys.argv = test_args
    args = parse_arguments()
    assert args.target == "example.com"
    assert args.ports == "22,80,443"
    assert args.verbose is True

if __name__ == "__main__":
    test_parse_arguments()
    print("All tests passed!")
