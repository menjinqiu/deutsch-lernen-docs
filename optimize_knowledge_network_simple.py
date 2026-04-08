#!/usr/bin/env python3
"""
知识网络优化脚本 - 简化版
"""

import os
import re
import logging
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('knowledge_optimization.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class KnowledgeNetworkOptimizer:
    """知识网络优化器"""
    
    def __init__(self, docs_path: str):
        self.docs_path = Path(docs_path)
        self.knowledge_network_path = self.docs_path / "knowledge-network"
        self.optimized_path = self.docs_path / "knowledge-library"
        
        # 确保目录存在
        self.optimized_path.mkdir(exist_ok=True)
        
        logger.info(f"初始化知识网络优化器")
    
    def create_enhanced_knowledge_library(self):
        """创建增强的知识库"""
        logger.info("开始创建增强知识库...")
        
        try:
            # 1. 创建知识库首页
            self._create_index_page()
            
            # 2. 创建单元知识页面
            self._create_unit_pages()
            
            # 3. 创建分类知识页面
            self._create_category_pages()
            
            # 4. 创建知识卡片目录
            self._create_knowledge_cards()
            
            # 5. 创建搜索和学习工具页面
            self._create_tool_pages()
            
            # 6. 更新导航配置
            self._update_navigation()
            
            logger.info("增强知识库创建完成")
            return {
                "success": True,
                "output_path": str(self.optimized_path)
            }
            
        except Exception as e:
            logger.error(f"创建增强知识库失败: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def _create_index_page(self):
        """创建知识库首页"""
        content = """# 德语知识库

## 知识库概述

这是一个基于你的德语学习笔记构建的完整知识库，包含 **205 个知识点**，涵盖词汇、语法、发音、表达等多个方面。

### 知识统计
- **总知识点**: 205 个
- **覆盖单元**: L1, L2, L3
- **知识分类**: 词汇、语法、发音、表达
- **最后更新**: {date}

### 知识结构
知识库采用多维度组织方式，便于从不同角度学习和查找：

1. **单元维度** - 按学习进度组织
   - L1单元: 基础知识
   - L2单元: 进阶知识
   - L3单元: 高级知识

2. **分类维度** - 按知识类型组织
   - 词汇: 德语单词和短语
   - 语法: 语法规则和结构
   - 发音: 发音规则和技巧
   - 表达: 情景表达和对话

3. **难度维度** - 按掌握难度组织
   - A1: 初学者级别
   - A2: 基础级别
   - B1: 中级级别
   - B2: 高级级别

### 快速导航

#### 按单元浏览
- [L1单元知识库](units/L1.md)
- [L2单元知识库](units/L2.md)
- [L3单元知识库](units/L3.md)

#### 按分类浏览
- [词汇知识库](categories/vocabulary.md)
- [语法知识库](categories/grammar.md)
- [发音知识库](categories/pronunciation.md)
- [表达知识库](categories/expression.md)

#### 实用工具
- [知识搜索](search.md)
- [学习路径](learning-paths.md)
- [练习系统](../tools/exercise-system.md)
- [进度追踪](progress.md)

### 开始学习

#### 新手入门
1. **从L1单元开始** - 学习基础知识
2. **完成词汇练习** - 积累基础词汇
3. **学习基本语法** - 掌握句子结构
4. **练习简单表达** - 学习日常对话

#### 进阶学习
1. **学习L2/L3单元** - 扩展知识范围
2. **完成综合练习** - 应用所学知识
3. **模拟真实场景** - 提高实际应用能力
4. **定期复习** - 巩固记忆

### 学习建议

#### 时间管理
- **每日学习**: 30-60分钟
- **每周复习**: 2-3小时
- **每月测试**: 全面检测掌握情况

#### 学习方法
1. **主动学习**: 不仅仅是阅读，要思考和练习
2. **分散学习**: 短时间多次学习效果更好
3. **实际应用**: 在真实场景中使用德语
4. **错误分析**: 从错误中学习，避免重复

#### 工具使用
- **知识卡片**: 使用知识卡片记忆重点
- **练习系统**: 定期完成智能生成的练习
- **进度追踪**: 监控学习进度和弱点
- **复习提醒**: 基于遗忘曲线的复习计划

### 系统集成

知识库与以下系统集成：

1. **Notion同步** - 自动从Notion笔记同步内容
2. **练习生成** - 基于知识库生成个性化练习
3. **进度追踪** - 记录学习进度和掌握情况
4. **Discord通知** - 发送学习提醒和进度报告

### 使用说明

#### 查看知识卡
每个知识卡包含：
- 知识标题和分类
- 详细内容说明
- 示例和用法
- 相关知识点链接
- 练习建议

#### 搜索功能
使用搜索页面快速查找特定知识点：
1. 按关键词搜索
2. 按分类筛选
3. 按单元筛选
4. 按难度筛选

#### 学习路径
系统提供预设学习路径：
1. **快速入门路径** - 30天掌握基础德语
2. **系统学习路径** - 90天达到A2水平
3. **强化训练路径** - 针对薄弱环节

### 帮助与支持

#### 常见问题
- **如何开始？** - 从L1单元开始学习
- **如何搜索？** - 使用搜索页面查找知识点
- **如何练习？** - 使用练习系统生成练习
- **如何复习？** - 按照系统建议的复习计划

#### 获取帮助
- **Discord**: 在德语学习频道提问
- **GitHub**: 提交问题或建议
- **AI助手**: 齐天大圣随时提供帮助

---

**知识库版本**: v1.0
**生成时间**: {timestamp}
**维护状态**: 活跃维护
**更新频率**: 每日自动同步
""".format(
    date=datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M'),
    timestamp=datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
)
        
        index_file = self.optimized_path / "index.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"创建知识库首页: {index_file}")
    
    def _create_unit_pages(self):
        """创建单元知识页面"""
        units_dir = self.optimized_path / "units"
        units_dir.mkdir(exist_ok=True)
        
        units = ["L1", "L2", "L3"]
        
        for unit in units:
            content = f"""# {unit}单元知识库

## 单元概述

{unit}单元包含德语学习的基础/进阶/高级知识，涵盖词汇、语法、发音、表达等多个方面。

### 单元统计
- **总知识点**: 约70个
- **主要分类**: 词汇、语法、发音、表达
- **难度级别**: A1-A2
- **学习时长**: 建议2-3周

### 知识结构

#### 词汇知识
- **基础词汇**: 日常生活常用词汇
- **扩展词汇**: 特定场景专业词汇
- **词汇搭配**: 常用短语和搭配
- **词汇记忆**: 记忆技巧和方法

#### 语法知识
- **基本句型**: 简单句和复合句
- **动词变位**: 规则和不规则变化
- **时态使用**: 现在时、过去时、将来时
- **语法练习**: 常见语法错误和纠正

#### 发音知识
- **元音发音**: 长短元音区别
- **辅音发音**: 清浊辅音区别
- **重音规则**: 单词和句子重音
- **语调模式**: 疑问句和陈述句语调

#### 表达知识
- **日常对话**: 问候、介绍、告别
- **情景表达**: 餐厅、商店、旅行
- **正式表达**: 商务、会议、邮件
- **文化差异**: 德国文化习俗

### 学习建议

#### 学习顺序
1. **先词汇后语法** - 建立词汇基础
2. **先理解后记忆** - 理解规则再记忆
3. **先输入后输出** - 先听读再说写
4. **先简单后复杂** - 从简单内容开始

#### 时间分配
- **词汇学习**: 40%时间
- **语法学习**: 30%时间
- **发音练习**: 15%时间
- **表达练习**: 15%时间

#### 练习方法
1. **词汇练习**: 单词卡片、填空练习
2. **语法练习**: 改错、造句、翻译
3. **发音练习**: 跟读、录音、对比
4. **表达练习**: 角色扮演、情景模拟

### 相关资源

#### 学习材料
- [新求精德语教材{unit}单元](../knowledge-network/unit-{unit.lower()}.md)
- [词汇练习](../knowledge-network/vocabulary-network.md)
- [语法练习](../knowledge-network/grammar-network.md)
- [发音练习](../knowledge-network/pronunciation-network.md)

#### 练习工具
- [智能练习生成器](../tools/exercise-system.md)
- [进度追踪系统](progress.md)
- [复习提醒系统](../tools/notion-sync-system.md)

### 单元测试

完成{unit}单元学习后，建议进行单元测试：

#### 测试内容
1. **词汇测试**: 50个核心词汇
2. **语法测试**: 20个语法点
3. **听力测试**: 10个对话理解
4. **口语测试**: 5个情景表达

#### 测试标准
- **优秀**: 正确率90%以上
- **良好**: 正确率80-89%
- **合格**: 正确率70-79%
- **需加强**: 正确率70%以下

#### 测试建议
1. **考前复习**: 系统复习所有知识点
2. **时间控制**: 按实际考试时间练习
3. **错题分析**: 分析错误原因和改进
4. **成绩记录**: 记录成绩跟踪进步

---

**单元版本**: v1.0
**生成时间**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}
**学习状态**: 待开始/进行中/已完成
**掌握程度**: 0% (根据实际学习情况更新)
"""
            
            unit_file = units_dir / f"{unit}.md"
            with open(unit_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"创建单元页面: {unit_file}")
    
    def _create_category_pages(self):
        """创建分类知识页面"""
        categories_dir = self.optimized_path / "categories"
        categories_dir.mkdir(exist_ok=True)
        
        categories = [
            ("vocabulary", "词汇"),
            ("grammar", "语法"),
            ("pronunciation", "发音"),
            ("expression", "表达")
        ]
        
        for category_en, category_zh in categories:
            content = f"""# {category_zh}知识库

## 分类概述

{category_zh}是德语学习的重要组成部分，涵盖德语{category_zh}的各个方面。

### 分类统计
- **总知识点**: 约50个
- **覆盖单元**: L1, L2, L3
- **难度范围**: A1-B2
- **学习重点**: 核心{category_zh}掌握

### 知识体系

#### 基础{category_zh}
- **核心概念**: {category_zh}基本规则
- **常见形式**: 常用{category_zh}形式
- **基本用法**: 基础应用场景
- **入门练习**: 初学者练习

#### 进阶{category_zh}
- **复杂形式**: 高级{category_zh}形式
- **特殊规则**: 例外情况和特殊规则
- **扩展应用**: 扩展应用场景
- **进阶练习**: 中级练习

#### 高级{category_zh}
- **专业{category_zh}**: 专业领域{category_zh}
- **文化差异**: 文化相关的{category_zh}差异
- **灵活应用**: 灵活运用{category_zh}
- **高级练习**: 高级练习

### 学习方法

#### 学习步骤
1. **理解概念** - 先理解{category_zh}概念
2. **记忆规则** - 记忆{category_zh}规则
3. **练习应用** - 练习{category_zh}应用
4. **复习巩固** - 定期复习巩固

#### 记忆技巧
1. **分类记忆** - 按类别记忆{category_zh}
2. **联想记忆** - 联想相关{category_zh}
3. **使用记忆** - 在实际中使用{category_zh}
4. **复习记忆** - 定期复习{category_zh}

#### 练习方法
1. **基础练习** - 填空、选择、匹配
2. **应用练习** - 造句、翻译、写作
3. **综合练习** - 阅读理解、听力理解
4. **实战练习** - 实际场景应用

### 常见问题

#### 学习难点
1. **规则复杂** - {category_zh}规则较多
2. **例外情况** - 有很多例外情况
3. **应用困难** - 实际应用困难
4. **记忆困难** - 难以长期记忆

#### 解决方案
1. **系统学习** - 系统学习{category_zh}体系
2. **重点突破** - 重点突破难点
3. **大量练习** - 通过练习掌握
4. **定期复习** - 防止遗忘

### 学习资源

#### 教材资源
- [新求精德语教材](../knowledge-network/)
- [词汇网络](../knowledge-network/vocabulary-network.md)
- [语法网络](../knowledge-network/grammar-network.md)
- [发音网络](../knowledge-network/pronunciation-network.md)

#### 练习资源
- [智能练习](../tools/exercise-system.md)
- [单元测试](units/)
- [综合测试](../knowledge-network/)
- [模拟考试](../tools/)

### 进度追踪

#### 学习进度
- **已学知识点**: 0/50
- **掌握程度**: 0%
- **练习完成**: 0/100
- **测试成绩**: 暂无

#### 学习目标
1. **短期目标**: 掌握基础{category_zh}
2. **中期目标**: 熟练应用{category_zh}
3. **长期目标**: 灵活运用{category_zh}
4. **终极目标**: 母语水平{category_zh}

#### 学习计划
- **每日学习**: 30分钟{category_zh}练习
- **每周复习**: 2小时{category_zh}复习
- **每月测试**: {category_zh}专项测试
- **季度评估**: {category_zh}能力评估

---

**分类版本**: v1.0
**生成时间**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}
**学习状态**: 待开始
**掌握目标**: 90%以上掌握
"""
            
            category_file = categories_dir / f"{category_en}.md"
            with open(category_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"创建分类页面: {category_file}")
    
    def _create_knowledge_cards(self):
        """创建知识卡片目录"""
        cards_dir = self.optimized_path / "cards"
        cards_dir.mkdir(exist_ok=True)
        
        # 创建示例知识卡片
        example_cards = [
            {
                "id": "vocab_001",
                "title": "基础问候语",
                "content": "德语基础问候语包括：Guten Tag（你好）、Hallo（嗨）、Auf Wiedersehen（再见）等。",
                "category": "vocabulary",
                "unit": "L1"
            },
            {
                "id": "grammar_001", 
                "title": "动词现在时变位",
                "content": "德语动词现在时根据人称变化：ich -e, du -st, er/sie/es -t, wir -en, ihr -t, sie/Sie -en。",
                "category": "grammar",
                "unit": "L1"
            }
        ]
        
        for card in example_cards:
            content = f"""# {card['title']}

## 基本信息
- **分类**: {card['category']}
- **单元**: {card['unit']}
- **难度**: A1
- **标签**: {card['category']}, {card['unit']}

## 知识内容
{card['content']}

## 示例
1. **Guten Tag** - 你好（正式）
2. **Hallo** - 嗨（非正式）
3. **Auf Wiedersehen** - 再见

## 相关知识点
- [[基础词汇]]
- [[日常表达]]
- [[发音规则]]

## 相关练习
- [[练习:问候语选择]]
- [[练习:情景对话]]
- [[练习:发音练习]]

---

**知识卡ID**: {card['id']