#!/usr/bin/python3
def main():
    import sys
    import calculator_1 as cal

    if (len(sys.argv) - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} {} {} = {}".format(n, sys.argv[2], m, cal.add(n, m)))
    elif sys.argv[2] == "-":
        print("{} {} {} = {}".format(n, sys.argv[2], m, cal.sub(n, m)))
    elif sys.argv[2] == "*":
        print("{} {} {} = {}".format(n, sys.argv[2], m, cal.mul(n, m)))
    elif sys.argv[2] == "/":
        print("{} {} {} = {}".format(n, sys.argv[2], m, cal.div(n, m)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    main()
