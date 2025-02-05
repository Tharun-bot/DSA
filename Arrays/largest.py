from typing import List
def largest_element(arr:List[int]):
    largest=-999
    for i in range(0, len(arr)):
        if(arr[i]>largest):
            largest=arr[i]

    return largest

if __name__=="__main__":
    arr = [1,6,5,4,0,-1]
    print(f'Largest element of the given array is : {largest_element(arr)}')