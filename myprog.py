#!/usr/bin/env python

# system include files
#
import sys
import os
import numpy as np

# main: this is the main function of this Python
#
# int main(int argc, char** argv)
#
def main(argv):
    # check for file name
    #
    if len(sys.argv) != 2: 
        print("file name enter was not found")
        exit()
    # open text file
    #
    file = open(argv[1],"r")
    r1 = 0
    r2 = 0
    # get the firstdimesion of the array
    #
    row, col = [int(x) for x in file.readline().split()]
   
    # create for loop to read text file 
    # asign value by row than column
    m1 = []
    for i in range(row):

        # copy text into a list
        #
        m11 = [float(x) for x in file.readline().split()]
        # check the program cols to make sure it is right
        #
        if col != len(m11):

            # close program
            #
            print("The matrix chose are not able to be multiple")
            exit()

        # add list
        #
        m1.append(m11)
        r1 = r1 + 1
    # get the dimeison of the next matrix
    #
    row2, col2 = [int(x) for x in file.readline().split()]
    m2 = [] 

    # for loop to copy text file
    #
    for i in range(row2):

        #  read each value and split them into seperate value
        #
        m22 = [float(x) for x in file.readline().split()]
        if col2 != len(m22):
            
            # close program
            #
            print("The matrix chose are not able to be multiple")
            exit()

        # add list
        #
        m2.append(m22)
        r2 = r2 + 1
    
    # check row for matrix 1
    #
    if row != r1:
            
        # close program
        #
        print("The matrix chose are not able to be multiple")

    # check row for matrix 2
    #
    if row2 != r2:
            
        # close program
        #
        print("The matrix chose are not able to be multiple")

    # check that the two can be multiple
    #
    if col != row2:
            
        # close program
        #
        print("The matrix chose are not able to be multiple")
    
    # print out the list
    #
    print("matrix one")
    print(m1)
    print("matrix two")
    print(m2)
  
    # matrix multiplication
    #
    m3 = [[0 for x in range(col2)] for y in range(row)]
 
    # explicit for loops
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
 
                # resulted matrix
                #
                m3[i][j] += m1[i][k] * m2[k][j]
    print ("matrix 3")
    print (m3)
    # close file
    #
    file.close();
#
# end of main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end of file
