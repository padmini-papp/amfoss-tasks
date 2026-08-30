// Palindrome Number - Easy
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        long original = x;
        long reversed = 0;
        while (x > 0) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        return original == reversed;
    }
};

// Approach: negative numbers can never be palindromes because of the minus sign.
// Built the reversed version of the number one digit at a time using modulo and
// division, then compared it to the original. Used long instead of int for the
// reversed number to avoid overflow on large numbers.
