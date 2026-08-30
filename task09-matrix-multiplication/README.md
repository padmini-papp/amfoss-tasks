Matrix Multiplication Showdown

This implements matrix multiplication three different ways and compares how fast each one runs.

Naive multiplication is the standard triple nested loop, going through every row and column combination directly, which runs in O(n cubed) time.

Divide and conquer splits each matrix into four quadrants recursively, multiplies the quadrants using eight recursive multiplications, then combines the results back together. Still O(n cubed) technically, just structured differently.

Strassen's algorithm uses the same divide and conquer idea but only needs seven recursive multiplications instead of eight, by using some extra additions and subtractions to make up the difference. This brings the time complexity down to about O(n to the power 2.81), which is theoretically better than naive for large enough matrices.

One thing to note is that divide and conquer and Strassen's only work correctly when the matrix size is a power of two, since they depend on splitting the matrix exactly in half each time.

Results and an interesting finding

Testing with a 16x16 matrix, naive multiplication actually finished fastest, even though Strassen's has better theoretical complexity. This is because in Python specifically, the overhead of all the recursive function calls and list slicing in divide and conquer and Strassen's outweighs their algorithmic advantage at this size. That advantage would probably only show up with much bigger matrices, or in a compiled language like C where function call overhead is much lower.

Challenges faced

Getting the quadrant splitting and recombining logic right took some care, especially for Strassen's algorithm, which has a lot of very similar looking addition and subtraction steps across its seven sub-multiplications, so it was easy to mix one up.

How to run

python3 matrix.py

Then enter a matrix size when prompted, it should be a power of two like 4, 8, or 16.
