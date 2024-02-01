from ft_filter import ft_filter


def check_even(number):
    """ check if a given number is even """

    return (number % 2 == 0)


def isdigit(c):
    """ isdigit copy """

    return (c in "1234567890")


def main():
    """ main function """

    print("Does the __doc__ match ? " +
          str(filter.__doc__ == ft_filter.__doc__) + "\n")

    string = "abcde123"
    print("Test: isdigit on string " + string)
    print("original filter => " + str(filter(isdigit, string))
          + ", " + str(list(filter(isdigit, string))))
    print("ft_filter => " + str(ft_filter(isdigit, string))
          + ", " + str(list(ft_filter(isdigit, string))) + "\n")

    print("Test: None function on string " + string)
    print("original filter => " + str(filter(None, string))
          + ", " + str(list(filter(None, string))))
    print("ft_filter => " + str(ft_filter(None, string))
          + ", " + str(list(ft_filter(None, string))) + "\n")

    lst = [1, 2, 3, 4, 5, 6, 7]
    print("Test: check_even on list " + str(lst))
    print("original filter => " + str(filter(check_even, lst))
          + ", " + str(list(filter(check_even, lst))))
    print("ft_filter => " + str(ft_filter(check_even, lst))
          + ", " + str(list(ft_filter(check_even, lst))) + "\n")

    print("Test: None function on list " + str(lst))
    print("original filter => " + str(filter(None, lst))
          + ", " + str(list(filter(None, lst))))
    print("ft_filter => " + str(ft_filter(None, lst))
          + ", " + str(list(ft_filter(None, lst))) + "\n")


if __name__ == '__main__':
    main()
