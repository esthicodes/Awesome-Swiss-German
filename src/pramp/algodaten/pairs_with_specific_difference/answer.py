def find_pairs_with_given_difference(arr, k):
  arr_set = set(arr) 
  ans = []
  for i in arr:
    if k + i in arr_set:
      ans.append([k+i, i])
  return ans
  
arr = [0, -1, -2, 2, 1]
k = 1
print(find_pairs_with_given_difference(arr, k))
