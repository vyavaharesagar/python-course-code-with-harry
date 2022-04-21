
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
from re import I


def diagonalDifference(arr):
    # Write your code here
    sum1 = []
    sum2 = []
    j = 0
    for subarr in arr:
        for i in range(len(subarr)):
            i = j
            sum1.append(subarr[i])
            j+=1
            break
    # print(sum1)

    for subarr in arr:
        print(subarr)
    
        
            

        
        
        
        
            
                
                
                

        
        
    
        
            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 3

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
