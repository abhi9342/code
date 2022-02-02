"""
Question: To find duplicates in array list. 
Time Complexity: O(n) Space Complexity: O(1)

Solution:
1. The list will not contain elements which is greater than size of array
2. Create and initialize the temp array of size n
3. Traverse through orignal list and append +1 in temp list at index = val of orignal list
4. Now, traverse through the temp list and return index where value greater than 1. 
"""

def duplicates(self, arr, n): 
        temp = [0 for i in range(n)]
        result = []
        
        for i in range(n):
            temp[arr[i]] += 1 
        
        for i in range(n):
            if temp[i] > 1:
                result.append(i)
        
        if result:
            return result
        else:
            result.append(-1)
            return result
