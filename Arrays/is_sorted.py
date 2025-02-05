from typing import List

def isSorted(arr:List[int]):
    for i in range(1, len(arr)-1):
        if((arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (arr[i]<arr[i] and arr[i]<arr[i+1])):
            return False
    return True


if __name__ == "__main__":
    arr=[1,2,3,10,5]
    print(f'Is this array increasing : {isSorted(arr)}')