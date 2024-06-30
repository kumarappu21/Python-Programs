def rotate(arr,d):
    n = len(arr);
    d=d%n;
    arr[:]=arr[d:]+arr[:d];
arr = [1,2,3,4,5,6,7,8];
d=4;
rotate(arr,d);
print("array after rotation is: ",arr);