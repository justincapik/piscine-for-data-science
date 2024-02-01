import sys
from ft_filter import ft_filter


def main():
    """ main function """

    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        print("AssertionError: the arguments are bad")
        exit(1)

    gen = ft_filter(lambda x: len(x) > int(sys.argv[2]), sys.argv[1].split())
    print(list(gen))


if __name__ == '__main__':
    main()
