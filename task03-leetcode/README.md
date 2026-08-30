## Leetcode Challenge

I solved 5 problems on Leetcode for this task, three easy and two medium.

Two Sum, easy. Given an array and a target, find the two numbers that add up to it. I used a hash map to store each number and its index as I went through the array, checking each time whether the complement, meaning target minus the current number, was already in the map. This gets the answer in a single pass instead of checking every pair.

Valid Parentheses, easy. Given a string of brackets, check if they're properly matched and nested. I used a stack, pushing every opening bracket, and whenever a closing bracket showed up, checking whether it matched whatever was on top of the stack. If the stack was empty or the brackets didn't match, the string is invalid.

Palindrome Number, easy. Check if a number reads the same forwards and backwards without converting it to a string. Negative numbers can never be palindromes because of the minus sign. I built the reversed version of the number one digit at a time using modulo and integer division, then compared it to the original, using a long instead of an int to avoid overflow on larger numbers.

Container With Most Water, medium. Given a list of heights, find the two lines that hold the most water together with the x axis. I used two pointers starting at each end of the array, calculating the water held as width times the shorter of the two heights, then moving whichever pointer had the smaller height inward, since that's the one limiting how much water could be held.

Maximum Subarray, medium. Find the contiguous subarray with the largest sum. This is known as Kadane's algorithm. I walked through the array once keeping a running sum, and at each number decided whether to keep extending the current subarray or start over from that number alone, whichever gave a bigger total.

Each cpp file in this folder has the code with a short explanation as a comment underneath.

Concepts learned: hash maps for constant time lookups instead of nested loops, using a stack for matching or balanced pairs, the two pointer technique for array problems, Kadane's algorithm for subarray sum problems, and avoiding integer overflow by using a wider data type where needed.
