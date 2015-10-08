<h2>Two Types</h2>
**Depth-First**  
- Always go left before going right
- three types of visitation
- Pre-order
- In-order
- Post-order

```python
# PRE-ORDER DFS
def pre_order_dfs(node):
    if node is not None:
        visit(node)
        pre_order_dfs(node.left)
        pre_order_dfs(node.right)
```

```python
# IN-ORDER DFS
def in_order_dfs(node):
    if node is not None:
        in_order_dfs(node.left)
        visit(node)
        in_order_dfs(node.right)
```

```python
# POST-ORDER DFS
def post_order_dfs(node):
    if node is not None:
        post_order_dfs(node.left)
        post_order_dfs(node.right)
        visit(node)
```

**Breadth-first search**
- level-by-level

```python
from collections import deque

def bfs(root_node):
    queue = deque()
    queue.append(root_node)
    while len(queue) > 0:
        node = queue.popleft()
        visit(node)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
```            
