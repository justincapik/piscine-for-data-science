import sys

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if len(sys.argv) == 1:
    print ("AssertionError: please provide one argument")
elif len(sys.argv) > 2:
    print ("AssertionError: more than one argument provided")
elif not (sys.argv[1].isdigit()
        or (len(sys.argv[1]) > 1 and sys.argv[1][0] == "-"
        and sys.argv[1][1:].isdigit())):
    print ("AssertionError: argument is not an integer")
else:
    if int(sys.argv[1]) % 2 == 0:
        print ("I'm Even.")
    else:
        print ("I'm Odd.")
    