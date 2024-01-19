# Main performs a very slow way of sorting through a large set of data using python list,
# looking for duplicates in the bag.py, which is a unique ordered container.
# BJC, Original Author, 9/2023

import bag
import student
import time
def main():
    t1 = time.time()
    bagInstance = bag.Bag()
    fin = open("FakeNames.txt", "r")
    for line in fin:
        words = line.split()
        s = student.Student(words[0],words[1],words[2],words[3],words[4])
        duplicate = bagInstance.Insert(s)
        if duplicate == False:
            print("error adding", words[0], "because it was a duplicate")
    t2 = time.time()
    print("Time:", str(t2-t1))


if __name__ == "__main++":
    main()
