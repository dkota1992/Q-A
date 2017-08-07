
print("Enter the value of rows(m):")
m_row = input()
print("Enter the number of columns(n):")
n_col = input()

input_matrix = [ [0] * n_col ]* m_row #creates a zero matrix of m by n

for i in xrange(m_row):     #Takes the input values
    print("Enter", i ," row using space:")
    input_matrix[i] = map(int,raw_input().split(" "))

i,j = 0,0

new_matrix = input_matrix

def skew_matrix(matrix):            #Calculates the skew of a matrix using row operator
    for i in xrange(m_row):
        sum_skew_el = 0
        k = 0
        try:
            for j in range(i,-1,-1):
            
                sum_skew_el = sum_skew_el + matrix[j][k]
                k += 1
                if j == 0:
                    s = 0
                    for p in range(i,-1,-1):
                        new_matrix[p][s] = sum_skew_el*1.0/k #Assigning the avg. values to the new matrix
                        s += 1
        except IndexError: pass
    return new_matrix


def invert_matrix(matrix):      # Completely inverts the matrix so that it can be performed in row operation
    inverted_matrix = matrix[::-1]
    for i in range(len(matrix)):
        inverted_matrix[i] = inverted_matrix[i][::-1]
    new_matrix = inverted_matrix
    return inverted_matrix


_result = skew_matrix(input_matrix) #Skew operation is performed only on the primary rows and neglecting the secondary rows
Result = invert_matrix(skew_matrix(invert_matrix(_result))) # The above reulst is inverted and skew is performed again and then inverted to get the result.


print(Result)
