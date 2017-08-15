#!/usr/bin/python3

"""Assumptions:
1. The input data is given in a text file, first line representing N,K(seperated by " " where 1<=K<=N)
2. The Second line consists of the original data seperated by " "

Brief Explanation:
A continuous stream of incremental or decremental subranges have a total value of (n*(n-1)/2) where n is the highest 
value of incremental/decremetal steps in a stream.

Let the input be [1,2,5,4,4,6,3] and the window size be 6
The first window will be [1,2,5,4,4,6]
The first reference list or stream of different subranges will be [3,-1,1].
The complete solution depends on the basic reference list created above.

The next step will be modifying first and last elements of the list. If the first element of the list is -1/1,
it can be discarded until the previous window and first element in current window are different.

If it is a value other than -1/1 then this value obey the principle of (n*(n+1))/2.

Thus we find the n value and decrease the value of n and update the reference list.

Same holds true for the final element. If the current new element in the window is a continuity for incremental/decremental stream,
the n value is updated and the last value in the reference list is updated or simply add -1/1 to the list if it is not a stream.

The sum of reference list is calculated in the first and is passed along everytime we transfer to a new window.
Everytime the reference list gets updated, this sum is also updated using the same principle explained above.
This helps is reduced load of calculating the list over and over again.

At any given point if the reference list is an empty list it means all the elements are same in that window. So, when moving to next window,
just compare the new element of the window with its previous index.

Performance:
O(n) where n is the number of inputs given.

Space Complexity:
Worst case - O(K) where K is the window size.

"""
import random #For generating random input values
import time # For performance testing
import sys #In order to read a file from arguments
start = time.clock()
# input_values = list(map(int,"188930 194123 201345 154243 154243".split(" ")))
# input_values = random.sample(range(1,100),20)
if len(sys.argv) < 2:
    raise FileNotFoundError("Please enter in the following format : 'python3 filename.py input.txt > output.txt'")
 
with open(sys.argv[1],"r") as f:                        # Opens the file and reads the first line as N,K
    N , K = list(map(int,f.readline().strip().split(" ")))
    input_values = f.readline().strip().split(" ")
    input_values = tuple(map(int,input_values))              #The input values are stored in a tuple(immutable sets) as we do
                                                        # not change the input data at any given time
def main():    
    if K <= 1 or K>N: return None
    elif K == 2:        # If K == 2, life is easy. Just compare the 2 adjacent values and return 1 and -1  for increment and decrement respectively
        index = 0
        while index < N-1:
            if input_values[index] < input_values[index+1]: print(1)
            elif input_values[index] > input_values[index+1]: print(-1)
            else: print(0)
            index += 1
    else:        
        new_index = 0  
#         print("First Window", input_values[:K]) 
        referencelist = getFirstWindow() #This gets the basic reference list from the first window afer which we will modify the corresponding references
        print(sum(referencelist))
        sum_reference_list = sum(referencelist)
        if K<N:
            while new_index + K < N:    #Print the sum values of the consecutive windows
                referencelist, sum_reference_list = newWindow(new_index, referencelist,sum_reference_list)
                new_index += 1
#                 print("Current Window", input_values[new_index:new_index+K])
#                 print("Reference List", referencelist)
                print(sum_reference_list)
           
def newWindow(index, reference_list, sum_reference_list):
    if not reference_list: reference_list.append(0)
    
    if abs(reference_list[0]) == 1:
        if input_values[index] != input_values[index+1]: 
            sum_reference_list = sum_reference_list - reference_list.pop(0)       
    elif input_values[index] != input_values[index+1]:
        n_value = find_n_value(reference_list[0])
        sum_reference_list -= reference_list[0]
        n_value = n_value-1
        if reference_list[0]<0 : reference_list[0] = -int((n_value*(n_value+1))/2)
        else: reference_list[0] = int((n_value*(n_value+1))/2)
        sum_reference_list += reference_list[0]
        
    new_n_value = find_n_Value(K, N, index, reference_list[:5]+reference_list[-5:]) #We dont have to pass the whole reference list as it is waste of memory
    if new_n_value and abs(new_n_value) == 1:
        reference_list.append(new_n_value)
        sum_reference_list += reference_list[-1]
    elif new_n_value: 
        sum_reference_list -= reference_list[-1]
        reference_list[-1] = new_n_value
        sum_reference_list += reference_list[-1]
        
    if not reference_list: return [],0
    elif reference_list[0] == 0: reference_list.pop(0)
    return reference_list,sum_reference_list
    
def find_n_value(num):              #Find the root value from the index as every value in reference list is (n*(n-1)/2)
    if num >0: num = -num
    return int((-1+(1-4*2*num)**0.5)/2) #We discard the negative root of the solution

def find_n_Value(K,N,index, reference_list):
    if reference_list == []:
        if input_values[index+K-1] < input_values[index+K]: return 1
        elif input_values[index+K-1] > input_values[index+K]: return -1
        return None
    
    n_value = find_n_value(reference_list[-1]) 
    if input_values[index+K-1] < input_values[index+K]:
        if input_values[index+K-2] != input_values[index+K-1]:
            if reference_list[-1] > 0:  #Update the value if it is a continuous stream
                n_value = n_value + 1
                return int((n_value*(n_value+1)/2))
        return 1    # Return 1 if it is not a continuous stream
        
    elif input_values[index+K-1] > input_values[index+K]:
        if input_values[index+K-1] != input_values[index+K-2]:
            if reference_list[-1] <0:
                n_value = n_value + 1
                return -int((n_value*(n_value+1)/2))
        return -1   
    
    return None     #Return None if it is neither incremental nor decremental
    
def getFirstWindow():
    first_window = input_values[:K]
    index = 0
    reference_list = []
    while index < K-1:
        count = 0
        while index <= K-2:             #Find the continuous stream of incremental subranges
            if first_window[index] < first_window[index+1]:
                index += 1
                count += 1
            else: break
        if count != 0:
            reference_list.append(int((count*(count+1))/2)) #Add to reference list the total values of continuous subranges
            
        count = 0
        while index <= K-2:             #Find the continuous stream of incremental subranges
            if first_window[index] > first_window[index+1]:
                index += 1
                count += 1
            else: break
        if count != 0:
            reference_list.append(-int((count*(count+1))/2))
    
        if index < K-1 and first_window[index] == first_window[index+1] : index += 1 #Index is skipped if the values are same
           
    return reference_list   #Returns reference list once the window is completely iterated

if __name__ == "__main__":
    main()
#     print(time.clock()-start)
