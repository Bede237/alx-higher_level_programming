#!/usr/bin/python3
def main():
    import calculator_1 as math
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, math.add(a, b)))
    print("{} - {} = {}".format(a, b, math.sub(a, b)))
    print("{} * {} = {}".format(a, b, math.mul(a, b)))
    print("{} / {} = {}".format(a, b, math.div(a, b)))


if __name__ == "__main__":
    main()
