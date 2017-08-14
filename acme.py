import random
import time
start = time.clock()
input_array = list(map(int,"188930 194123 201345 154243 154243".split(" ")))
input_array = random.sample(range(1,1000000),100000)
# input_array = [74, 7, 15, 49, 77, 50, 40, 19, 54, 80]
#     input_array = [1,2,3,4,5,3,2,2,2,2,3,4]
#     print(input_arra)
def main():

    N = len(input_array)
    K = 100000
    if K == 1: return None
    
    print("Input array: ",input_array)
    print("First Window",input_array[:K])
#     print(N,K)
    reference_list = []
    referencelist = []
    new_input = input_array[:K]
    new_index = 0

    while new_index <= K-2:
        reference_list, new_index = checkCount(new_input, new_index)
        referencelist += reference_list
         
    print(referencelist)

    
    
def newWindow(K,N,index, reference_list):
    if abs(reference_list[0]) == 1: reference_list.pop(0)
    else:
        n_value = find_n_value(reference_list[0])
        n_value = n_value-1
        if reference_list[0]<0 : reference_list[0] = -int((n_value*(n_value+1))/2)
        else: reference_list[0] = int((n_value*(n_value+1))/2)
    new_n_value = find_n_Value(K, N, index, reference_list) 
    if new_n_value and abs(new_n_value) == 1:
        reference_list.append(new_n_value)
    elif new_n_value: reference_list[-1] = new_n_value
#     print(reference_list)
      
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
    
def checkCount(first_window, index,reference_list=None):
    count = 0
    reference_list = []
    while index <= len(first_window)-2:
        if first_window[index] < first_window[index+1]:
            index += 1
            count += 1
        else: break
    if count != 0:
        reference_list.append(int((count*(count+1))/2))
        
    count = 0
    while index <= len(first_window)-2:
        if first_window[index] > first_window[index+1]:
            index += 1
            count += 1
        else: break
    if count != 0:
        reference_list.append(-int((count*(count+1))/2))
    if index > len(first_window)-2: return reference_list, index
    elif first_window[index] == first_window[index+1] and index<len(first_window)-2: index += 1
       
    return (reference_list, index)



if __name__ == "__main__":
#     print(main())
    print("n_value",main())
    print(time.clock()-start)

