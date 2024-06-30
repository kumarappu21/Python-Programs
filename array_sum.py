n = int(input("enter number of elements in the array: "))
arr=[];
for j in range(1,n+1):
    arr.append(j);
print(arr);
def sum_of_array(arr):
    sum = 0;
    for i in arr:
       sum = sum + i;
    return sum;
print("sum of array: ", sum_of_array(arr));
