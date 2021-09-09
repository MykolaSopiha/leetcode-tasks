#144. Binary Tree Preorder Traversal

Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.

![Binary Tree Example](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

##Example 1:

```
Input: root = [1,null,2,3]
Output: [3,2,1]
```

##Example 2:

```
Input: root = []
Output: []
```

##Example 3:

```
Input: root = [1]
Output: [1]
```

##Example 4:

![Binary Tree Example](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)

```
Input: root = [1,2]
Output: [2,1]
```

##Example 5:

![Binary Tree Example](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

```
Input: root = [1,null,2]
Output: [2,1]
```

##Constraints:

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`
 

**Follow up:** Recursive solution is trivial, could you do it iteratively?