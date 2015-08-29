class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        # for linked list
        self.next = None

class Solution(object):
    def MidTravel(self, root):
        rootVal = str(root.val)
        leftRes = None
        rightRes = None
        if root.left != None:
            leftRes = self.MidTravel(root.left)
            leftRes[1].next = root
        print rootVal
        if root.right != None:
            rightRes = self.MidTravel(root.right)
            root.next = rightRes[0]
        else:
            root.next = None
        leftest = leftRes[0] if leftRes != None else root
        rightest = rightRes[1] if rightRes != None else root

        return [leftest, rightest]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    root.left = node2
    node2.left = node4
    node2.right = node3
    node4.right = node5
    [left, right] = sol.MidTravel(root)
    x = left
    while x != None:
        print x.val,
        x = x.next
