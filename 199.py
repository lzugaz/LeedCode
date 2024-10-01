from typing import List
from typing import Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def rightSideView( root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    right_view = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        # Traverse the current level
        for i in range(level_size):
            node = queue.popleft()
            
            # If it's the last node in this level, add it to the right view
            if i == level_size - 1:
                right_view.append(node.val)
            
            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return right_view
 
