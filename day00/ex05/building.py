import sys


def print_string_info(string):
    """ print the string character, uppercase,
    lowercase, punction mark, spaces and digit count"""

    punc = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~\\"

    print("The text contains {:d} characters:".format(len(string)))
    print("{:d} upper letters".format(sum(1 for c in string if c.isupper())))
    print("{:d} lower letters".format(sum(1 for c in string if c.islower())))
    print("{:d} punctuation marks".format(sum(1 for c in string if c in punc)))
    print("{:d} spaces".format(sum(1 for c in string if c == ' ')))
    print("{:d} digits".format(sum(1 for c in string if c.isdigit())))


def main():
    """ main """

    if len(sys.argv) == 1:
        print("What is the text to count ?")
        string = input()
        print_string_info(string)
    elif len(sys.argv) == 2:
        print_string_info(sys.argv[1])
    else:
        print("AssertionError: too many arguments")
        exit(1)


if __name__ == "__main__":
    main()
