import java.io.*;
import java.lang.*;
import java.util.*;


class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println("tilingRectangleBT(2, 3): " + solution.tilingRectangleBT(2, 3));  // 3
        System.out.println("tilingRectangleBT(5, 8): " + solution.tilingRectangleBT(5, 8));  // 5
        System.out.println("tilingRectangleBT(11, 13): " + solution.tilingRectangleBT(11, 13));  // 6
    }
}

class Solution {

    // 1240. Tiling a Rectangle with the Fewest Squares
    // Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.
    // https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
    // http://int-e.eu/~bf3/squares/
    // http://int-e.eu/~bf3/squares/view.html
    // https://en.wikipedia.org/wiki/Squaring_the_square

    // Example #1:
    // Input: n = 2, m = 3
    // Output: 3
    // Explanation: 3 squares are necessary to cover the rectangle.
    // 2 (squares of 1x1)
    // 1 (square of 2x2)

    // Example #2:
    // Input: n = 5, m = 8
    // Output: 5
    // 1 5x5
    // 1 3x3
    // 1 2x2
    // 2 1x1

    // Example #3:
    // Input: n = 11, m = 13
    // Output: 6
    // 1 7x7
    // 1 6x6
    // 1 5x5
    // 2 4x4


    // Backtracking with n x m grid
    // Time Complexity: 
    // Space Complexity:
    private int bestAnswer = Integer.MAX_VALUE;
    public int tilingRectangleBT(int n, int m) 
    {
        dfs(0, 0, new boolean[n][m], 0);
        return 0;
    }

    // Base cases
    // 1. Current answer > best answer, return - done
    // 2. Filled up our rectangle - done

    // Considerations:
    // Use greedy algo to determine the largest available rectangle
    private void dfs(int row, int col, boolean[][] rect, int curAnswer) {
        int n = rect.length;  // rows
        int m = rect[0].length;  // columns


        // Current answer > best answer, return - done
        if (curAnswer >= bestAnswer) {
            return;
        }

        // if row >= n, we have traversed all rows available and are done
        if (row >= n) {
            bestAnswer = curAnswer;
            return;
        }

        // if col >= m, we've traversed that row and can move on to the next row (start from col 0)
        if (col >= m) {
            dfs(row + 1, 0, rect, curAnswer);
            return;
        }

        if (rect[row][col]) {
            dfs(row, col + 1, rect, curAnswer);
            return;
        }

        // 1. Start with the largest available square (k x k)
        // 2. Cover our square with 1's for the k x k square
        // 3. Traverse and cover again with the next largest available square
        // 4. Uncover our square and reset the 1s to 0s
        for (int k = Math.min(n - row, m - col); k >= 1 && isAvailable(rect, row, col, k); k--) {
            cover(rect, row, col, k);
            dfs(row, col + 1, rect, count + 1);
            uncover(rect, row, col, k);
        }
    }


    // Check if area is already covered
    private boolean isAvailable(boolean[][] rect, int row, int col, int k) {
        for(int i = 0; i < k; i++){
            for(int j = 0; j < k; j++){
                if (rect[row + i][col + j]) {
                    return false;
                }
            }
        }

        return true;
    }

    // Cover with a k * k square starting from (r, c)
    private void cover(boolean[][] rect, int row, int col, int k) {
        for(int i = 0; i < k; i++){
            for(int j = 0; j < k; j++){
                rect[row + i][col + j] = true;
            }
        }
    }

    // Uncover with a k * k square starting from (r, c)
    private void uncover(boolean[][] rect, int row, int col, int k) {
        for(int i = 0; i < k; i++){
            for(int j = 0; j < k; j++){
                rect[row + i][col + j] = false;
            }
        }
    }
}