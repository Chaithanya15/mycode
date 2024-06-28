# Find largest number in array
def finding_largest_num(arr):
    if len(arr)==0:
        return None
    largest=arr[0]
    for num in arr:
        if num>largest:
            largest=num
    return largest

numbers=[1,3,6,11,4]
largestNumber=finding_largest_num(numbers)
print("Largest number in series is :",largestNumber)
