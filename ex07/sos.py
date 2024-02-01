import sys


def main():
    """ main function """

    morse = {' ': '/', 'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-',
             'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..'}

    if len(sys.argv) != 2 or not sys.argv[1].isalpha():
        print("AssertionError: the arguments are bad")
        exit(1)

    string = ""

    for c in sys.argv[1]:
        string += morse[c.upper()] + " "

    print(string.strip())


if __name__ == '__main__':
    main()
