import random
import time
start = time.clock()
input_array = list(map(int,"188930 194123 201345 154243 154243".split(" ")))
input_array = random.sample(range(1,100),10)
#     input_array = [74, 7, 15, 49, 77, 50, 40, 19, 54, 80]
#     input_array = [1,2,3,4,5,3,2,2,2,2,3,4]
#     print(input_arra)
def main():

    N = len(input_array)
    K = 8
    if K == 1: return None
    step_size = 3
    
    print("Input array: ",input_array)
    print("First Window",input_array[:K])
    print("Real Output", checkCount(input_array[:K]))
#     print(N,K)
    reference_list = []
    
    for i in range(0,K,step_size):
        if K < i+step_size : upper_bound = K
        else: upper_bound = i+step_size
        newinput = input_array[i:upper_bound]
        print(newinput)
        newlist = checkCount(newinput)
        reference_list = addList(reference_list, newlist)
        print("Reference in for loop",reference_list)
        
        
    print("Reference list {}".format(reference_list))    
        
    new_input = input_array[:K]
    
    index=0
    print("reference_list", reference_list)
#     for i in reference_list: print(find_n_value(i))
    return newWindow(K, N, index, reference_list)

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
    print(reference_list)
      
    if index+K < N-1: newWindow(K, N, index+1, reference_list)
    
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
    
def checkCount(first_window, index=0,reference_list=None):
    reference_list = []
    count = 0
    while index<=len(first_window)-2:
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
    
    if index > len(first_window)-2: return reference_list
    elif first_window[index] == first_window[index+1] and index<len(first_window)-2: index += 1
    
    reference_list = reference_list + checkCount(first_window, index, reference_list)
    return reference_list

def addList(list1,list2):         
    if list1 == [] or list2 ==[]:
        return list1+list2
    elif (list1[-1] < 0 and list2[0] > 0) or (list1[-1] > 0 and list2[0] < 0):
        return list1+list2
    else:
        list1_n_value = find_n_value(list1[-1])
        list2_n_value = find_n_value(list2[0])
        n_value = list1_n_value + list2_n_value
        if list1[-1] < 0: 
            newvalue = -int((n_value*(n_value+1))/2)
        else:
            newvalue = int((n_value*(n_value+1))/2)
        return list1[:-1] + [newvalue] + list2[1:]

if __name__ == "__main__":
#     print(main())
    print("n_value",main())
    print(time.clock()-start)
