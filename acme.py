import random
import time
import sys
start = time.clock()
input_array = list(map(int,"188930 194123 201345 154243 154243".split(" ")))
# input_array = random.sample(range(1,100),20)

def main():

    with open(sys.argv[1],"r") as f:
        N , K = list(map(int,f.readline().strip().split(" ")))
        input_array = f.readline().strip().split(" ")
        input_array = list(map(int,input_array))
    print(K)
    
    print("Input array: ",input_array)
#     print("First Window", input_array[:K])
#      
    print("First_reference",checkCount(K))      
    if K <= 2: return None
    new_index = 0   
    referencelist = checkCount(K)
    print(referencelist)
    sum_reference_list = sum(referencelist)
    if K<N:
        while new_index + K < N:
#             print(sum_reference_list)
            referencelist, sum_reference_list = newWindow(K, N, new_index, referencelist,sum_reference_list)
            new_index += 1
            print("New Input", input_array[new_index:new_index+K])
            print(referencelist)
#              
            
    print(sum_reference_list)      

#      

    
    
def newWindow(K,N,index, reference_list, sum_reference_list):
    if abs(reference_list[0]) == 1: 
        sum_reference_list = sum_reference_list - reference_list.pop(0)       
    else:
        n_value = find_n_value(reference_list[0])
        sum_reference_list -= reference_list[0]
        n_value = n_value-1
        if reference_list[0]<0 : reference_list[0] = -int((n_value*(n_value+1))/2)
        else: reference_list[0] = int((n_value*(n_value+1))/2)
        sum_reference_list += reference_list[0]
    new_n_value = find_n_Value(K, N, index, reference_list) 
    if new_n_value and abs(new_n_value) == 1:
        reference_list.append(new_n_value)
        sum_reference_list += reference_list[-1]
    elif new_n_value: 
        sum_reference_list -= reference_list[-1]
        reference_list[-1] = new_n_value
        sum_reference_list += reference_list[-1]
    return reference_list,sum_reference_list
      
#     if index+K < N-1: newWindow(K, N, index+1, reference_list)
    
def find_n_value(num):
    if num >0: num = -num
    return int((-1+(1-4*2*num)**0.5)/2)

def find_n_Value(K,N,index, reference_list):
    n_value = find_n_value(reference_list[-1]) 
    if input_array[index+K-1] < input_array[index+K]:
        if reference_list[-1] > 0:
            n_value = n_value + 1
            return int((n_value*(n_value+1)/2))
        return 1
        
    elif input_array[index+K-1] > input_array[index+K]:
        if reference_list[-1] <0:
            n_value = n_value + 1
            return -int((n_value*(n_value+1)/2))
        return -1
    
    return None
    
def checkCount(K):
    first_window = input_array[:K]
    index = 0
    K = len(first_window)
    reference_list = []
    while index < K-1:
        count = 0
        while index <= K-2:
            if first_window[index] < first_window[index+1]:
                index += 1
                count += 1
            else: break
        if count != 0:
            reference_list.append(int((count*(count+1))/2))
            
        count = 0
        while index <= K-2:
            if first_window[index] > first_window[index+1]:
                index += 1
                count += 1
            else: break
        if count != 0:
            reference_list.append(-int((count*(count+1))/2))
    
        if index < K-2 and first_window[index] == first_window[index+1] : index += 1
           
    return reference_list



if __name__ == "__main__":
    main()
    print(time.clock()-start)

