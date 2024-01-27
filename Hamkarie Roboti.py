import numpy as np

def read_matrices(file_path) :
    with open(file_path , 'r') as file :
        data = file.readline().split()
        n , m = map(int , data)

        matrices = [] 

        for i in range (n) :
            matrix = []
            for j in range (m) :
                row  = list(map(int , file.readline().split()))
                matrix.append(row)
            matrices.append(matrix)
    return matrices

file_path = '/Users/xxsmgxx/Desktop/code/Uni/Hamkarie Roboti/input2.txt'

input = read_matrices(file_path)
matrices = []
for inp in input :
    matrices.append(np.array(inp))
first_ans = matrices[0]
second_ans = matrices[1]
max_dot = np.linalg.det(np.dot(matrices[0],matrices[1]))
for i in range (len(matrices)-1) :
    for j in range(i+1 ,len(matrices) ) :
        temp_dot = np.linalg.det(np.dot(matrices[i], matrices [j]))
        if temp_dot > max_dot :
            first_ans = matrices[i]
            second_ans = matrices [j]
            max_dot = temp_dot

if np.linalg.det(first_ans) < np.linalg.det(second_ans) :
    new_matrix = np.dot(second_ans,first_ans)
else :
    new_matrix = np.dot(first_ans , second_ans)

inverse = np.linalg.inv(new_matrix)

for row in inverse:
    for element in row:
        formatted_element = "{:.3f}".format(round(element, 3))
        print(formatted_element, end=" ")
    print()