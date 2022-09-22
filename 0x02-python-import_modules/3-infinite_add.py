#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    inf_add = 0
    for i in argv:
        inf_add += int(i)
    print("{:d}".format(inf_add))
