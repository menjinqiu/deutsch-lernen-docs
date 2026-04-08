#!/usr/bin/env python3
"""
知识网络优化脚本
将现有的知识网络优化为包含具体内容的丰富知识库
"""

import os
import json
import re
import logging
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field

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

@dataclass
class KnowledgeCard:
    """知识卡片数据类"""
    id: str
    title: str
    content: str
    category: str
    unit: str
    section: Optional[str] = None
    difficulty: str = "A1"
    tags: List[str] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)
    related_cards: List[str] = field(default_factory=list)
    practice_links: List[str] = field(default_factory=list)
    last_updated: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    
    def to_markdown(self) -> str:
        """转换为 Markdown 格式"""
        md = f"""# {self.title}

## 📋 基本信息
- **分类**: {self.category}
- **单元**: {self.unit}
- **难度**: {self.difficulty}
- **标签**: {', '.join(self.tags)}
- **最后更新**: {self.last_updated}

## 📚 知识内容
{self.content}

"""
        
        if self.examples:
            md += "## 💡 示例\n\n"
            for i, example in enumerate(self.examples, 1):
                md += f"{i}. {example}\n"
            md += "\n"
        
        if self.related_cards:
            md += "## 🔗 相关知识点\n\n"
            for card_id in self.related_cards:
                md += f"- [[{card_id}]]\n"
            md += "\n"
        
        if self.practice_links:
            md += "## 🧪 相关练习\n\n"
            for link in self.practice_links:
                md += f"- {link}\n"
            md += "\n"
        
        md += "---\n"
        md += f"**知识卡ID**: {self.id}\n"
        md += f"**生成时间**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}\n"
        
        return md

class KnowledgeNetworkOptimizer:
    """知识网络优化器"""
    
    def __init__(self, docs_path: str):
        self.docs_path = Path(docs_path)
        self.knowledge_network_path = self.docs_path / "knowledge-network"
        self.optimized_path = self.docs_path / "knowledge-library"
        
        # 确保目录存在
        self.optimized_path.mkdir(exist_ok=True)
        
        # 加载现有知识网络
        self.existing_knowledge = self._load_existing_knowledge()
        
        logger.info(f"初始化知识网络优化器，现有知识点: {len(self.existing_knowledge)}")
    
    def _load_existing_knowledge(self) -> Dict[str, Dict]:
        """加载现有知识网络数据"""
        knowledge = {}
        
        # 读取单元页面
        unit_files = ["unit-l1.md", "unit-l2.md", "unit-l3.md"]
        
        for unit_file in unit_files:
            filepath = self.knowledge_network_path / unit_file
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    unit_knowledge = self._parse_unit_content(content, unit_file)
                    knowledge.update(unit_knowledge)
        
        logger.info(f"加载了 {len(knowledge)} 个现有知识点")
        return knowledge
    
    def _parse_unit_content(self, content: str, filename: str) -> Dict[str, Dict]:
        """解析单元页面内容"""
        knowledge = {}
        
        # 提取单元信息
        unit = "L1" if "L1" in filename else "L2" if "L2" in filename else "L3"
        
        # 解析章节
        lines = content.split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            # 检测章节标题
            section_match = re.match(r'^## (.+)$', line.strip())
            if section_match:
                # 保存前一个章节的内容
                if current_section and current_content:
                    section_content = '\n'.join(current_content).strip()
                    if section_content:
                        # 创建知识卡
                        card_id = f"{unit}_{current_section}_{len(knowledge)+1:03d}"
                        knowledge[card_id] = {
                            "title": current_section,
                            "content": section_content,
                            "category": self._detect_category(current_section),
                            "unit": unit,
                            "section": current_section,
                            "difficulty": "A1",
                            "tags": [unit, current_section],
                            "examples": [],
                            "related_cards": [],
                            "practice_links": []
                        }
                
                # 开始新章节
                current_section = section_match.group(1)
                current_content = []
            elif current_section and line.strip():
                current_content.append(line)
        
        # 处理最后一个章节
        if current_section and current_content:
            section_content = '\n'.join(current_content).strip()
            if section_content:
                card_id = f"{unit}_{current_section}_{len(knowledge)+1:03d}"
                knowledge[card_id] = {
                    "title": current_section,
                    "content": section_content,
                    "category": self._detect_category(current_section),
                    "unit": unit,
                    "section": current_section,
                    "difficulty": "A1",
                    "tags": [unit, current_section],
                    "examples": [],
                    "related_cards": [],
                    "practice_links": []
                }
        
        return knowledge
    
    def _detect_category(self, text: str) -> str:
        """检测知识分类"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ["词汇", "单词", "wort", "vocab"]):
            return "vocabulary"
        elif any(word in text_lower for word in ["语法", "grammar", "satzbau"]):
            return "grammar"
        elif any(word in text_lower for word in ["发音", "pronunciation", "aussprache"]):
            return "pronunciation"
        elif any(word in text_lower for word in ["表达", "expression", "ausdruck"]):
            return "expression"
        else:
            return "general"
    
    def enrich_knowledge_content(self):
        """丰富知识内容"""
        logger.info("开始丰富知识内容...")
        
        enriched_cards = []
        
        for card_id, card_data in self.existing_knowledge.items():
            # 创建知识卡对象
            card = KnowledgeCard(
                id=card_id,
                title=card_data["title"],
                content=card_data["content"],
                category=card_data["category"],
                unit=card_data["unit"],
                section=card_data["section"],
                difficulty=card_data["difficulty"],
                tags=card_data["tags"],
                examples=card_data["examples"],
                related_cards=card_data["related_cards"],
                practice_links=card_data["practice_links"]
            )
            
            # 丰富内容
            enriched_card = self._enrich_card_content(card)
            enriched_cards.append(enriched_card)
            
            logger.info(f"丰富知识卡: {card.title}")
        
        logger.info(f"完成了 {len(enriched_cards)} 个知识卡的丰富")
        return enriched_cards
    
    def _enrich_card_content(self, card: KnowledgeCard) -> KnowledgeCard:
        """丰富单个知识卡的内容"""
        # 根据分类添加特定内容
        if card.category == "vocabulary":
            card = self._enrich_vocabulary_card(card)
        elif card.category == "grammar":
            card = self._enrich_grammar_card(card)
        elif card.category == "pronunciation":
            card = self._enrich_pronunciation_card(card)
        elif card.category == "expression":
            card = self._enrich_expression_card(card)
        
        # 添加通用内容
        card = self._add_general_content(card)
        
        return card
    
    def _enrich_vocabulary_card(self, card: KnowledgeCard) -> KnowledgeCard:
        """丰富词汇知识卡"""
        # 提取德语单词
        german_words = re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]+\b', card.content)
        
        if german_words:
            # 添加示例句子
            examples = []
            for word in german_words[:3]:  # 最多3个示例
                examples.append(f"**{word}** - 示例: Das {word} ist auf dem Tisch.")
            
            if examples:
                card.examples = examples
            
            # 添加相关练习链接
            for word in german_words[:2]:
                card.practice_links.append(f"[[练习:词汇_{word}]]")
        
        # 添加记忆技巧
        memory_tips = """
### 🧠 记忆技巧
1. **联想记忆**: 将德语单词与相似的中文发音或形象联想
2. **分类记忆**: 按主题分类记忆相关词汇
3. **词根记忆**: 学习常见词根和前缀后缀
4. **使用记忆**: 在实际句子中使用新学词汇
"""
        card.content += memory_tips
        
        return card
    
    def _enrich_grammar_card(self, card: KnowledgeCard) -> KnowledgeCard:
        """丰富语法知识卡"""
        # 添加语法规则说明
        grammar_rules = """
### 📖 语法规则
1. **基本结构**: 主语 + 动词 + 其他成分
2. **动词位置**: 在陈述句中，动词总是第二位
3. **词性变化**: 注意名词的性、数、格变化
4. **时态使用**: 根据时间关系选择正确时态
"""
        card.content += grammar_rules
        
        # 添加常见错误
        common_errors = """
### ⚠️ 常见错误
1. **动词变位错误**: 忘记根据人称变化动词
2. **词序错误**: 将动词放在错误位置
3. **冠词错误**: 使用错误的冠词（der/die/das）
4. **介词错误**: 使用错误的介词搭配
"""
        card.content += common_errors
        
        # 添加练习链接
        card.practice_links.append("[[练习:语法改错]]")
        card.practice_links.append("[[练习:句子构造]]")
        
        return card
    
    def _enrich_pronunciation_card(self, card: KnowledgeCard) -> KnowledgeCard:
        """丰富发音知识卡"""
        # 添加发音要点
        pronunciation_tips = """
### 🔊 发音要点
1. **元音长度**: 注意长短元音的区别
2. **辅音清浊**: 区分清辅音和浊辅音
3. **重音位置**: 注意单词的重音位置
4. **语调模式**: 学习德语句子的语调
"""
        card.content += pronunciation_tips
        
        # 添加练习建议
        practice_suggestions = """
### 🎤 练习建议
1. **跟读练习**: 跟着录音模仿发音
2. **录音对比**: 录音后与标准发音对比
3. **最小对练习**: 练习发音相似的单词对
4. **句子朗读**: 在完整句子中练习发音
"""
        card.content += practice_suggestions
        
        return card
    
    def _enrich_expression_card(self, card: KnowledgeCard) -> KnowledgeCard:
        """丰富表达知识卡"""
        # 添加使用场景
        usage_scenarios = """
### 🎭 使用场景
1. **正式场合**: 商务会议、官方场合
2. **日常交流**: 朋友间、家庭中的对话
3. **服务场合**: 餐厅、商店、银行等
4. **紧急情况**: 求助、报警、医疗等
"""
        card.content += usage_scenarios
        
        # 添加礼貌程度说明
        politeness_levels = """
### 🤝 礼貌程度
1. **正式表达**: Siezen（您）形式，用于陌生人或长辈
2. **非正式表达**: Duzen（你）形式，用于朋友和同龄人
3. **亲密表达**: 家人和非常熟悉的朋友之间
"""
        card.content += politeness_levels
        
        # 添加相关表达
        card.related_cards.append("[[表达:问候]]")
        card.related_cards.append("[[表达:告别]]")
        card.related_cards.append("[[表达:感谢]]")
        
        return card
    
    def _add_general_content(self, card: KnowledgeCard) -> KnowledgeCard:
        """添加通用内容"""
        # 添加学习建议
        learning_advice = """
### 📚 学习建议
1. **理解优先**: 先理解概念，再记忆细节
2. **多次复习**: 按照遗忘曲线定期复习
3. **实际应用**: 在真实场景中使用所学知识
4. **错误分析**: 分析错误原因，避免重复
"""
        card.content += learning_advice
        
        # 添加进度追踪
        progress_tracking = """
### 📊 进度追踪
- **首次学习**: 标记开始学习日期
- **掌握程度**: 定期评估掌握情况（0-100%）
- **复习记录**: 记录每次复习的时间和效果
- **错误统计**: 统计常见错误类型和频率
"""
        card.content += progress_tracking
        
        return card
    
    def generate_knowledge_library(self, cards: List[KnowledgeCard]):
        """生成知识库"""
        logger.info("开始生成知识库...")
        
        # 1. 生成索引页面
        self._generate_index_page(cards)
        
        # 2. 按单元组织
        self._organize_by_unit(cards)
        
        # 3. 按分类组织
        self._organize_by_category(cards)
        
        # 4. 生成搜索页面
        self._generate_search_page(cards)
        
        # 5. 生成学习路径
        self._generate_learning_paths(cards)
        
        logger.info("知识库生成完成")
    
    def _generate_index_page(self, cards: List[KnowledgeCard]):
        """生成索引页面"""
        index_content = f"""# 📚 德语知识库

## 🎯 知识库概述

这是一个基于你的德语学习笔记构建的完整知识库，包含 **{len(cards)} 个知识点**，涵盖词汇、语法、发音、表达等多个方面。

### 📊 知识统计
- **总知识点**: {len(cards)} 个
- **覆盖单元**: L1, L2, L3
- **知识分类**: 词汇、语法、发音、表达
- **最后更新**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}

### 🏗️ 知识结构
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

### 🔍 快速导航

#### 按单元浏览
- [[L1单元知识库|knowledge-library/units/L1]]
- [[L2单元知识库|knowledge-library/units/L2]]
- [[L3单元知识库|knowledge-library/units/L3]]

#### 按分类浏览
- [[词汇知识库|knowledge-library/categories/vocabulary]]
- [[语法知识库|knowledge-library/categories/grammar]]
- [[发音知识库|knowledge-library/categories/pronunciation]]
- [[表达知识库|knowledge-library/categories/expression]]

#### 实用工具
- [[知识搜索|knowledge-library/search]]
- [[学习路径|knowledge-library/learning-paths]]
- [[练习系统|../tools/exercise-system]]
- [[进度追踪|knowledge-library/progress]]

### 🚀 开始学习

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

### 📈 学习建议

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

### 🔄 系统集成

知识库与