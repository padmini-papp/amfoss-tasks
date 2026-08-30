// Valid Parentheses - Easy
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else {
                if (st.empty()) return false;
                char top = st.top();
                st.pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        return st.empty();
    }
};

// Approach: used a stack. Every opening bracket gets pushed. Every closing bracket
// checks if it matches whatever's on top of the stack. If not, or if the stack is
// empty when a closing bracket shows up, it's invalid. At the end, valid only if
// the stack is completely empty.
