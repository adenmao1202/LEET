def pretty_print_tree(root, val="data", left="left", right="right"):
    """
    打印一个更美观的ASCII树形结构
    
    参数:
    - root: 树的根节点
    - val: 节点值的属性名 (默认: "data")
    - left: 左子节点的属性名 (默认: "left")
    - right: 右子节点的属性名 (默认: "right")
    """
    def display(root, val=val, left=left, right=right):
        """返回用于打印的字符串列表"""
        
        # 没有节点
        if getattr(root, val) is None:
            return [], 0, 0
        
        # 没有子节点
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, middle
        
        # 获取左子树的行、宽度和中间位置
        if getattr(root, left) is not None:
            left_lines, left_width, left_middle = display(getattr(root, left))
        else:
            left_lines, left_width, left_middle = [], 0, 0
        
        # 获取右子树的行、宽度和中间位置
        if getattr(root, right) is not None:
            right_lines, right_width, right_middle = display(getattr(root, right))
        else:
            right_lines, right_width, right_middle = [], 0, 0
        
        # 当前节点的值
        root_val = '%s' % getattr(root, val)
        root_width = len(root_val)
        
        # 计算新的宽度和中间位置
        new_root_width = left_width + right_width + root_width
        if new_root_width < 2:
            new_root_width = 2
        
        new_root_middle = left_width + root_width // 2
        if new_root_middle < 1:
            new_root_middle = 1
        
        # 计算根节点的位置
        root_position = new_root_middle - root_width // 2
        
        # 创建根节点行
        new_root_line = ' ' * root_position + root_val
        
        # 填充根节点行到完整宽度
        new_root_line = new_root_line + ' ' * (new_root_width - len(new_root_line))
        
        # 创建连接线
        if left_width > 0:
            left_connection = ' ' * (left_middle + 1) + '_' * (left_width - left_middle - 1)
        else:
            left_connection = ''
        
        if right_width > 0:
            right_connection = '_' * right_middle + ' ' * (right_width - right_middle)
        else:
            right_connection = ''
        
        connection_line = left_connection + ' ' * root_width + right_connection
        
        # 创建左右子树的连接线
        if left_width > 0:
            left_connector = ' ' * left_middle + '/' + ' ' * (left_width - left_middle - 1)
        else:
            left_connector = ' ' * left_width
        
        if right_width > 0:
            right_connector = ' ' * right_middle + '\\' + ' ' * (right_width - right_middle - 1)
        else:
            right_connector = ' ' * right_width
        
        connector_line = left_connector + ' ' * root_width + right_connector
        
        # 合并左右子树的行
        if len(left_lines) < len(right_lines):
            left_lines.extend([' ' * left_width] * (len(right_lines) - len(left_lines)))
        elif len(right_lines) < len(left_lines):
            right_lines.extend([' ' * right_width] * (len(left_lines) - len(right_lines)))
        
        # 合并所有行
        merged_lines = []
        for i in range(max(len(left_lines), len(right_lines))):
            merged_lines.append(left_lines[i] + ' ' * root_width + right_lines[i])
        
        # 返回结果
        return [new_root_line, connection_line, connector_line] + merged_lines, new_root_width, new_root_middle
    
    lines, _, _ = display(root, val, left, right)
    for line in lines:
        print(line)

# 使用示例
if __name__ == "__main__":
    from BinaryTreeNode import BinaryTreeNode
    
    # 创建一个二叉搜索树
    root = BinaryTreeNode(10)
    nodes = [5, 15, 3, 7, 12, 20]
    for value in nodes:
        root.insert_tree(BinaryTreeNode(value))
    
    # 打印树形状
    pretty_print_tree(root) 