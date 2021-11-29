#!/usr/bin/python 

class Problem():
    def __init__(self,filename):
        names = []
        with open(filename, "r") as file:
            for line in file:
                names.append(line)
        return

def main():
    p = Problem('names.txt')
    for name in p.names:
        print("Hello {}!\n".format(name))

if __name__ == "__main__":
    main()