#!/usr/bin/env python3
"""
重构 L1 单元知识库 - 简化版
"""

import os
from pathlib import Path
import datetime

def redesign_l1_unit():
    """重构 L1 单元知识库"""
    
    l1_path = Path(__file__).parent / "docs" / "knowledge-library" / "units" / "L1.md"
    
    # 读取重构版内容
    redesigned_path = Path(__file__).parent / "docs" / "knowledge-library" / "units" / "L1-redesigned.md"
    
    if redesigned_path.exists():
        with open(redesigned_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换原来的 L1 页面
        with open(l1_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"L1 单元知识库重构完成: {l1_path}")
        
        # 删除临时文件
        os.remove(redesigned_path)
        print(f"删除临时文件: {redesigned_path}")
    else:
        print(f"重构版文件不存在: {redesigned_path}")

def main():
    """主函数"""
    print("开始重构知识库...")
    redesign_l1_unit()
    print("知识库重构完成！")

if __name__ == "__main__":
    main()