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
        if not duplicate:
            print("error adding", words[0], "because it was a duplicate")
    fin.close()
    t2 = time.time()
    print("Time to Insert:", str(t2-t1))


    # Traverse
    totalAge = 0
    for s in bagInstance:
        totalAge += int(s.getAge())
    # need to round to 4 seconds
    print("The average age of all students is", totalAge / bagInstance.Size())

    #Delete
    t1 = time.time()
    fin = open("DeleteNames.txt")
    for line in fin: # Includes all lines and return.., must strip returns.
        ssn = line.strip()
        s2 = student.Student("","",ssn,"","") #dummy student
        ok = bagInstance.Delete(s2)
        if ok:
            print("Error deleting. SSN not found: ", ssn)
    fin.close()
    t2 = time.time()
    print("Deleting time: ", str(t2-t1))




    #Retrieve
    t1 = time.time()
    totalAge=0
    count = 0
    fin = open("RetrieveNames.txt")
    for line in fin: # Includes all lines and return.., must strip returns.
        ssn = line.strip()
        s2 = student.Student("","",ssn,"","") #dummy student
        foundStudent = bagInstance.Retrieve(s2)
        if not foundStudent:
            print("Error retrieving. SSN not found: ", ssn)
        else:
            totalAge+= int(foundStudent.getAge())
            count +=1
    print("The average age of all retrieved students is: " + str(totalAge/count))
    fin.close()
    t2 = time.time()
    print("Retrieving time: ", str(t2-t1))
if __name__ == "__main__":
    main()

