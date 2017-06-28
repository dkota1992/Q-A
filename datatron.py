"""
Input
1 2 3 4
4 5 6 5
7 8 9 6
0 0 0 0

1st Diagonal = 1
2nd Diagonal = 2, 4
3rd Diagonal = 3, 5, 7
4th Diagonal = 4, 6, 8
.
.
.

3 + 5 + 7 = 15/3 = 5

# of Rows < # of Cols

Output
1 3 5 6
3 5 6 7    
5 6 7 6
0 0 0 0"""


def skew_matrix(matrix,input_col):  
    new_matrix = matrix
    for i in xrange(input_col):
        sum_diagnol = 0
        count,k = 0,0
        try:
            for j in xrange(i,-1,-1):
            
                sum_diagnol = sum_diagnol + matrix[j][k]
                k += 1
                
                if matrix[j][k] != 0: count += 1
                if j == 0:
                    s = 0
                    for p in xrange(i,-1,-1):
                        if count != 0: 
                            new_matrix[p][s] = sum_diagnol*1.0/count
                        s += 1
        except IndexError: pass
    return new_matrix


    
def invert_matrix(matrix): 
    inverted_matrix = matrix[::-1]
    for i in xrange(len(matrix)):
        inverted_matrix[i] = inverted_matrix[i][::-1]
    new_matrix = inverted_matrix
    return inverted_matrix
    
def main():
    input_rows = 3
    input_col = 4
    
    input_matrix = [[1 , 2 , 3, 4], [3 , 5, 6, 7], [1, 8, 7, 9],[0, 0, 0, 0]]    
    
    _output = skew_matrix(input_matrix,input_col)
    Output = invert_matrix(skew_matrix(invert_matrix(_output),input_col))
    print(Output[:input_rows])
    
    
if __name__ == '__main__':
    main()
    
    
    
    

# 
# Your last C# code is saved below:
# using System;
# 
# public class Test
# {
#     public static void Main()
#     {
#         Console.WriteLine("Hello");
#     }
# }
