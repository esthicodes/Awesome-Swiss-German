#include <stdio.h>
#include <stdlib.h>

int r_size;
int c_size;

//void mark_island(int (*mat)[c_size], int r, int c) {
void mark_island(int mat[][c_size], int r, int c) {
  if (r < 0 || r >= r_size || c < 0 || c >= c_size)
    return;
  if (mat[r][c] == 0)
    return;
  
  mat[r][c] = 0; // marked
  mark_island(mat, r - 1, c);
  mark_island(mat, r, c - 1);
  mark_island(mat, r + 1, c);
  mark_island(mat, r, c + 1);
}

int getNumberOfIslands(size_t numRows, size_t numCols, int binaryMatrix[numRows][numCols]) 
{
  int islands = 0;
  r_size = numRows;
  c_size = numCols;

  for (int r = 0; r < numRows; r++) {
    for (int c = 0; c < numCols; c++) {
      if (binaryMatrix[r][c] == 1) {
        islands++;
        mark_island(binaryMatrix, r, c);
      }
    }
  }
  return islands;
}

int main() {
  int m[2][2] = {{1, 0}, {0, 1}};
  int result = getNumberOfIslands(2,2,m);
  printf("%d", result);  
  return 0;
}

