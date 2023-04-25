def diffBetweenTwoStrings(source, target):
  m, n = len(target), len(source) 
  dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
  
  # Build dp
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0:
        dp[i][j] = j
      elif j == 0:
        dp[i][j] = i
      else:
        if target[i - 1] == source[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
  
  # Reconstruct path
  path = []
  i, j = m, n

  while i > 0 and j > 0:
    if target[i - 1] == source[j - 1]:
      # Write char with no edits
      path.append(source[j - 1])
      i -= 1
      j -= 1
    else:
      # We must either subtract source[j - 1] or add target[i - 1]
      if dp[i][j - 1] < dp[i - 1][j]:
        path.append("-" + source[j - 1])   
        j -= 1
      else:
        path.append("+" + target[i - 1])
        i -= 1
        
  while i > 0:
    path.append("+" + target[i - 1])
    i -= 1
  
  while j > 0:
    path.append("-" + source[j - 1])   
    j -= 1
    
  path.reverse()
  return path
