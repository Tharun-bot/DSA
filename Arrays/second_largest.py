from typing import List

def second_largest(arr:List[int]):
    largest, second_largest = -999, -1000
    for i in range(0, len(arr)):
        if(arr[i]>largest):
            second_largest=largest
            largest=arr[i]
        elif(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
        
    return second_largest

def second_smallest(arr:List[int]):
    smallest, second_smallest = 9999, 10000
    for i in range(0, len(arr)):
        if(arr[i]<smallest):
            second_smallest=smallest
            smallest=arr[i]
        elif(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest=arr[i]
    
    return second_smallest

if __name__ == "__main__":
    arr = [1,2,3,4,6]
    print(f'Second Largest Element is : {second_largest(arr)}')
    print(f'Second Smallest element is : {second_smallest(arr)}')
