def num_of_paths_to_dest_v2(n):
  paths = [[0 for col in range(n)] for row in range(n)]
  
  for row in range(n):
    for col in range(row, n):
      if row == 0 and col == 0:
        paths[row][col] = 1
      if row > 0:
        paths[row][col] += paths[row-1][col]
      if col > 0:
        paths[row][col] += paths[row][col -1]
  return paths[-1][-1]
