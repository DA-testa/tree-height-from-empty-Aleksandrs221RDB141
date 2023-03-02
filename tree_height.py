# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    tree = numpy.zeros(n)
    def element_height(i):
        if tree[i]!=0:
            return tree[i]
        if parents[i]!=-1:
            tree[i]=element_height(parents[i])+1
        else:
            tree[i]=1
        return tree[i]
    for i in range(n):       
        element_height(i)
    max_height = int(max(tree))
    # Your code here
    return max_height

def main():
 # implement input form keyboard and from files
    text = input()
    if "F" in text :
        file=input()
        if "a" not in file :
            with open(f"test/{file}") as f:
                num = int(f.readline().strip())
                tree = f.readline().split()
                treehight = compute_height(num,list(map(int,tree)))
                print(treehight)
    elif "I" in text:
        num = int(input())
        tree = input().split()
        treehight = compute_height(num,list(map(int,tree)))
        print(treehight)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))