// Maximum Depth of Binary Tree - Easy (used as extra/backup problem)
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        return max(leftDepth, rightDepth) + 1;
    }
};

// Approach: recursive. If a node doesn't exist its depth is 0. Otherwise the depth
// is 1 (for the current node) plus whichever of the left or right subtree is deeper.
