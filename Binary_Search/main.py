#BJC, Original Author
# 9/25/2023
# Conducts binary search algorithm
import bst
import student
import time
def main():
    total_fails =0
    total_Fails = 0
    total_fails_R =0
    # Works!
    t1 = time.time()
    treeInstance = bst.BST()
    fin = open("FakeNames.txt", "r")
    for line in fin:
        words = line.split()
        s = student.Student(words[0],words[1],words[2],words[3],words[4])
        duplicate = treeInstance.Insert(s)
        if not duplicate:
            print("error adding", words[0], "because it was a duplicate")
            total_fails += 1
    fin.close()
    t2 = time.time()
    print("Time to Insert:", str(t2-t1))
    print('Total fails in Insert Category: ', total_fails)

    # Traverse working correctly
    totalAge = 0
    for s in treeInstance:
        totalAge += int(s.getAge())
    if treeInstance.Size() >0:
        average_age = totalAge / treeInstance.Size()
    else:
        average_age = 0
    print("The average age of all students is", str(average_age))

    # Works!
    t1 = time.time()
    fin = open("DeleteNames.txt")
    for line in fin: # Includes all lines and return.., must strip returns.
        ssn = line.strip()
        s2 = student.Student("","",ssn,"","") #dummy student
        ok = treeInstance.Delete(s2)
        if ok:
            print("Error deleting. SSN not found: ", ssn)
            total_Fails += 1
    fin.close()
    t2 = time.time()
    print("Deleting time: ", str(t2-t1))

    print('Total fails in Delete Category: ', total_Fails)

    #Retrieve IS working Correctly
    t1 = time.time()
    totalAge=0
    count = 0
    fin = open("RetrieveNames.txt")
    for line in fin: # Includes all lines and return.., must strip returns.
        ssn = line.strip()
        s2 = student.Student("","",ssn,"","") #dummy student
        foundStudent = treeInstance.Retrieve(s2)
        if foundStudent is not None:
            totalAge+= int(foundStudent.getAge())
            count +=1
        else:
            print("Error retrieving. SSN not found: ", ssn)
            total_fails_R +=1
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

