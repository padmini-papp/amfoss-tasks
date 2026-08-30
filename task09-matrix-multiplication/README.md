# Matrix Multiplication Showdown

Task 09 for amFOSS. Implements matrix multiplication three different ways and compares their runtime.

## Algorithms used

1. Naive Matrix Multiplication - the standard triple nested loop approach, O(n^3) time complexity. For every cell in the result, loop through and sum up the products of the corresponding row and column.

2. Divide and Conquer - splits each matrix into 4 quadrants recursively, multiplies the quadrants (8 recursive multiplications), and combines them back together. Still technically O(n^3) in terms of complexity, but structured differently.

3. Strassen's Algorithm - similar divide and conquer idea, but uses a clever trick to only need 7 recursive multiplications instead of 8, using addition/subtraction to make up for it. This brings the complexity down to about O(n^2.81), which is better than naive for very large matrices.

Note: Divide and Conquer and Strassen's only work correctly when the matrix size is a power of 2 (2, 4, 8, 16...), since they rely on splitting the matrix exactly in half each time.

## Benchmarking approach

The program generates two random matrices of the same size, runs all three multiplication methods on them, and times each one using Python's time.time(). It also checks that all three methods produce the exact same result matrix, to verify correctness.

## Results

Tested with a 16x16 matrix:

Naive Matrix Multiplication: 0.44 ms
Divide and Conquer: 5.48 ms
Strassen's Algorithm: 5.82 ms

Verification Status: PASSED
Fastest Method: Naive

Interesting finding: naive multiplication was actually the fastest at this size, even though Strassen's has better theoretical time complexity. This is because in Python specifically, the recursive function calls and list slicing used in Divide and Conquer and Strassen's have a lot of overhead, which outweighs their algorithmic advantage until you get to much bigger matrix sizes, or use a lower level language.

## Challenges faced

Getting the indices right for combining matrix quadrants back together after splitting was tricky, and Strassen's algorithm specifically has a lot of very similar looking add/subtract steps for the 7 sub-multiplications, so it was easy to swap something by mistake and had to be careful to match it exactly against the standard formula.

## How to run

python3 matrix.py

Then enter a matrix size when prompted (should be a power of 2 like 4, 8, or 16).

## Resources used and concepts learned

- Learned how Strassen's algorithm reduces the number of multiplications needed using addition and subtraction tricks
- Learned about recursive matrix splitting for divide and conquer approaches
- Learned that theoretical time complexity doesn't always translate directly into real world speed, especially in interpreted languages like Python where overhead matters a lot at smaller scales
