#!/usr/bin/python3
def main():
    import sys
    i = 1
    n = len(sys.argv)
    print((n - 1), "argument:")
    if (n - 1) > 0:
        for i in range(n):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()