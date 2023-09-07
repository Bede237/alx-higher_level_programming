#!/usr/bin/python3
def main():
    import sys
    i = 1
    n = len(sys.argv) - 1
    print((n), "argument", end='')
    if n == 1:
        print(":")
    elif n > 1:
        print("s:")
    else:
        print("s.")
    if (n) > 0:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
