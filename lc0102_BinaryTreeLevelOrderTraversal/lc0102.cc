// LeetCode #102: Binary Tree Level Order Traversal

#include <iostream>
#include <vector>

using namespace std;

typedef struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
} TreeNode;


vector<vector<int> > levelOrder (TreeNode *root) {
    vector<vector<int> > ret;
    if (!root) { return ret; }  // Empty tree
    
    vector<TreeNode *> curr_level;
    vector<TreeNode *> next_level;
    curr_level.push_back (root);
    
    while (!curr_level.empty ()) {
        vector<int> curr_level_nums;
        for (int i = 0 ; i < curr_level.size () ; i++) {
            TreeNode *temp = curr_level[i];
            curr_level_nums.push_back (temp->val);
            if (temp->left) {
                next_level.push_back (temp->left);
            }
            if (temp->right) {
                next_level.push_back (temp->right);
            }
        }
        
        curr_level = next_level;    // Copy next_level to curr_level
        next_level.clear ();        // Empty next_level
        ret.push_back (curr_level_nums);
    }
    
    return ret;
}

int main () {
    
}