# Make text files smaller for resting.
from hashtablecopy import HashTable
import student
import time
def main():
    total_fails =0
    total_Fails = 0
    total_fails_R =0
    threshold = 10
    #
    t1 = time.time()
    tableInstance = HashTable(3000040)
    fin = open("FakeNamesBig.txt", "r")
    for line in fin:
        words = line.split()
        s = student.Student(words[0],words[1],words[2],words[3],words[4])
        duplicate = tableInstance.Insert(s)
        if not duplicate:
            #print("error adding", words[0], "because it was a duplicate")
            total_fails += 1
            #if total_fails > threshold:
            #   print("/n Lots of prints...stopping print")
            #else:

    fin.close()
    t2 = time.time()
    print("Time to Insert:", str(t2-t1))
    print('Total fails in Insert Category: ', total_fails)

    #
    totalAge = 0
    for s in tableInstance:
        totalAge += int(s.getAge())
    if tableInstance.Size() >0:
        average_age = totalAge / tableInstance.Size()
    else:
        average_age = 0
    print("The average age of all students is", str(average_age))

    # Works!
    t1 = time.time()
    fin = open("DeleteNamesBig.txt")
    for line in fin: # Includes all lines and return.., must strip returns.
        ssn = line.strip()
        s2 = student.Student("","",ssn,"","") #dummy student
        ok = tableInstance.Delete(s2)
        if not ok:
            total_Fails += 1
            #if total_Fails > threshold:
                #print("\nLots of deletes, stopping print...\n")

            #else:
               # print ("Error deleting. SSN Not found: ", ssn)
    fin.close()
    t2 = time.time()
    print("Deleting time: ", str(t2-t1))

    print('Total fails in Delete Category: ', total_Fails)

    # issues
    t1 = time.time()
    totalAge=0
    count = 0
    fin = open("RetrieveNamesBig.txt")
    for line in fin: # Includes all lines and return.., must strip returns.
        ssn = line.strip()
        s2 = student.Student("","",ssn,"","") #dummy student
        foundStudent = tableInstance.Retrieve(s2)
        if foundStudent is not None:
            totalAge+= int(foundStudent.getAge())
            count +=1
        else:
            #print("Error retrieving. SSN not found: ", ssn)
            total_fails_R +=1
            #if total_fails_R >threshold:
               # print ("\n Lots of retrieves. Stopping print...\n")
            #else:
                #print("Error retrieving. SSN not found: ", ssn)

    if count >0:
        average_age = totalAge / count
    else:
        average_age =0
    print("The average age of all retrieved students is: ",average_age)
    fin.close()
    t2 = time.time()
    print("Retrieving time: ", str(t2-t1))
    print('Total fails in Retrieve Category: ', total_fails_R)
main()

