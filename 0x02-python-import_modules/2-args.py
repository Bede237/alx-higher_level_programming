#!/usr/bin/python3
def main():
    import sys
    n = len(sys.argv)
    print((n - 1), "argument:")
    if (n - 1) > 0:
        for i in range(n):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))


if __name__ == "__main__":
    main()
