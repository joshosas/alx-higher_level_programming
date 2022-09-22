#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    file = dir(hidden_4)
    length = len(file)
    for i in range(0, length):
        if file[i][0:2] != "__":
            print(file[i])

