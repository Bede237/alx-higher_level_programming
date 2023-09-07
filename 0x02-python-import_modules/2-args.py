#!/usr/bin/python3
def main():
    import sys
    i = 1
    n = len(sys.argv) - 1
    print((n - 1), "argument", end='')
    if n == 1:
        print(":")
    elif n > 1:
        print("s:")
    else:
        print("s.")
    if (n) > 0:
        for i in range(n + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
