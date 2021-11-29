#!/usr/bin/python 

class Problem():
    def __init__(self,filename):
        names = []
        with open(filename, "r") as file:
            for line in file:
                names.append(line.rstrip())
        self.names = names
        return

def main():
    p = Problem('C:\\Users\\Ben\\Documents\\Coding Projects\\AoC2021\\helloworld\\names.txt')
    for name in p.names:
        print("Hello {}!\n".format(name))

if __name__ == "__main__":
    main()