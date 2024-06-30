arr = [3,6,8,2,4,6,8,10,9,3,2];
def largest(arr):
    max = arr[0];
    for i in arr:
        if i > max:
            max = i;
    return max;
print("largest element = ",largest(arr));