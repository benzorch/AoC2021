#!/usr/bin/python

class Problem():
    def __init__(self,filename):
        integers = []
        with open(filename, "r") as file:
            for line in file:
                integers.append(int(line.rstrip()))
        self.integers = integers
        return


def main():
    p = Problem("C:\\Users\\Ben\\Documents\\Coding Projects\\AoC2021\\day01\\input.txt")
    print("The fourth value is {}".format(p.integers[3]))
    
    previous = -2345678
    increases = 0
    
    for current in p.integers:
        if previous == -2345678:
            print("{} (N/A No Previous Value)".format(current))
        elif current > previous:
            print("{} (Increase)".format(current))
            increases += 1
        else:
            print("{} (No Increase)".format(current))
        previous = current

    print("Depth increases {} times".format(increases))
    return


if __name__ == "__main__":
    main()
    