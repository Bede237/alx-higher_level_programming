#!/usr/bin/python3
def main():
    import sys
    n = 0
    for i, arg in enumerate(sys.argv):
        if i > 0:
            n += int(arg)
    print(n)


if __name__ == "__main__":
    main()
