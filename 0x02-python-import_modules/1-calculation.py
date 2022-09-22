#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as my_calculator
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, my_calculator.add(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, my_calculator.sub(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, my_calculator.mul(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, my_calculator.div(a, b)))
