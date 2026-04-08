#!/usr/bin/env python3
"""
基于知识网络的智能练习生成系统
根据205个知识点的属性和掌握程度生成个性化练习
"""

import os
import json
import random
import logging
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('exercise_generation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ExerciseType(Enum):
    """练习类型枚举"""
    VOCABULARY = "vocabulary"      # 词汇练习
    GRAMMAR = "grammar"           # 语法练习
    PRONUNCIATION = "pronunciation" # 发音练习
    EXPRESSION = "expression"     # 表达练习
    COMPREHENSION = "comprehension" # 理解练习
    INTEGRATED = "integrated"     # 综合练习

class DifficultyLevel(Enum):
    """难度级别枚举"""
    BEGINNER = "A1"      # 初学者
    ELEMENTARY = "A2"    # 基础
    INTERMEDIATE = "B1"  # 中级
    ADVANCED = "B2"      # 高级
    EXPERT = "C1"        # 专家

@dataclass
class KnowledgePoint:
    """知识点数据类"""
    id: str
    text: str
    category: str
    unit: str
    section: Optional[str] = None
    difficulty: DifficultyLevel = DifficultyLevel.BEGINNER
    mastery_level: float = 0.0  # 0.0-1.0，掌握程度
    last_practiced: Optional[datetime.datetime] = None
    practice_count: int = 0
    error_rate: float = 0.0  # 错误率
    tags: List[str] = field(default_factory=list)

@dataclass
class Exercise:
    """练习数据类"""
    id: str
    type: ExerciseType
    difficulty: DifficultyLevel
    knowledge_points: List[KnowledgePoint]
    question: str
    options: List[str]
    correct_answer: str
    explanation: str
    hints: List[str] = field(default_factory=list)
    time_limit: Optional[int] = None  # 时间限制（秒）
    points: int = 10  # 分值

class ExerciseGenerator:
    """智能练习生成器"""
    
    def __init__(self, knowledge_network_path: str):
        self.knowledge_network_path = Path(knowledge_network_path)
        self.exercises_path = self.knowledge_network_path / "exercises"
        self.exercises_path.mkdir(exist_ok=True)
        
        # 加载知识网络数据
        self.knowledge_points = self._load_knowledge_points()
        
        # 练习模板库
        self.exercise_templates = self._load_exercise_templates()
        
        # 用户学习数据（模拟）
        self.user_data = self._load_user_data()
        
        logger.info(f"初始化练习生成器，知识点数: {len(self.knowledge_points)}")
    
    def _load_knowledge_points(self) -> List[KnowledgePoint]:
        """从知识网络加载知识点"""
        points = []
        
        # 模拟加载知识点数据
        # 在实际实现中，这里会解析知识网络文档
        units = ["L1", "L2", "L3"]
        categories = ["vocabulary", "grammar", "pronunciation", "expression", "exercise"]
        
        for unit in units:
            for category in categories:
                # 模拟生成知识点
                for i in range(1, 21):  # 每个单元每个分类20个知识点
                    point_id = f"{unit}_{category}_{i:03d}"
                    point = KnowledgePoint(
                        id=point_id,
                        text=f"{unit}单元{category}知识点{i}",
                        category=category,
                        unit=unit,
                        difficulty=DifficultyLevel.BEGINNER,
                        mastery_level=random.uniform(0.1, 0.9),
                        practice_count=random.randint(0, 10),
                        error_rate=random.uniform(0.0, 0.5),
                        tags=[unit, category]
                    )
                    points.append(point)
        
        logger.info(f"加载了 {len(points)} 个知识点")
        return points
    
    def _load_exercise_templates(self) -> Dict[str, List[Dict]]:
        """加载练习模板"""
        templates = {
            "vocabulary": [
                {
                    "type": "multiple_choice",
                    "template": "请选择 '{word}' 的正确中文意思：",
                    "options_count": 4
                },
                {
                    "type": "fill_blank",
                    "template": "请用德语单词填空：{sentence_with_blank}",
                    "options_count": 0
                },
                {
                    "type": "matching",
                    "template": "请将德语单词与正确的中文意思匹配：",
                    "options_count": 5
                }
            ],
            "grammar": [
                {
                    "type": "sentence_correction",
                    "template": "请改正以下句子中的语法错误：{incorrect_sentence}",
                    "options_count": 0
                },
                {
                    "type": "grammar_choice",
                    "template": "请选择正确的语法形式完成句子：{sentence_with_gap}",
                    "options_count": 4
                }
            ],
            "pronunciation": [
                {
                    "type": "pronunciation_choice",
                    "template": "请选择单词 '{word}' 的正确发音：",
                    "options_count": 3
                },
                {
                    "type": "minimal_pairs",
                    "template": "请分辨以下两个单词的发音差异：{word1} 和 {word2}",
                    "options_count": 2
                }
            ],
            "expression": [
                {
                    "type": "situation_response",
                    "template": "在以下情景中，应该说什么：{situation}",
                    "options_count": 4
                },
                {
                    "type": "dialogue_completion",
                    "template": "请完成以下对话：{dialogue_with_gap}",
                    "options_count": 3
                }
            ]
        }
        
        return templates
    
    def _load_user_data(self) -> Dict:
        """加载用户学习数据（模拟）"""
        return {
            "current_unit": "L3",
            "weak_categories": ["grammar", "pronunciation"],
            "preferred_exercise_types": ["multiple_choice", "fill_blank"],
            "average_score": 0.75,
            "learning_style": "visual"
        }
    
    def analyze_knowledge_gaps(self) -> List[KnowledgePoint]:
        """分析知识缺口，识别薄弱知识点"""
        weak_points = []
        
        for point in self.knowledge_points:
            # 基于掌握程度和错误率识别薄弱点
            if point.mastery_level < 0.6 or point.error_rate > 0.3:
                weak_points.append(point)
        
        # 按薄弱程度排序
        weak_points.sort(key=lambda x: (x.mastery_level, -x.error_rate))
        
        logger.info(f"识别出 {len(weak_points)} 个薄弱知识点")
        return weak_points
    
    def select_knowledge_points(self, 
                               count: int = 10,
                               focus_categories: Optional[List[str]] = None,
                               focus_units: Optional[List[str]] = None) -> List[KnowledgePoint]:
        """选择知识点用于生成练习"""
        selected_points = []
        
        # 1. 优先选择薄弱知识点
        weak_points = self.analyze_knowledge_gaps()
        
        # 2. 应用筛选条件
        filtered_points = []
        for point in weak_points:
            if focus_categories and point.category not in focus_categories:
                continue
            if focus_units and point.unit not in focus_units:
                continue
            filtered_points.append(point)
        
        # 3. 如果筛选后不够，补充其他知识点
        if len(filtered_points) < count:
            # 添加最近学习但掌握不够的知识点
            for point in self.knowledge_points:
                if point not in filtered_points:
                    if point.practice_count > 0 and point.mastery_level < 0.8:
                        filtered_points.append(point)
        
        # 4. 随机选择指定数量的知识点
        selected_points = random.sample(
            filtered_points, 
            min(count, len(filtered_points))
        )
        
        logger.info(f"选择了 {len(selected_points)} 个知识点用于练习生成")
        return selected_points
    
    def generate_vocabulary_exercise(self, point: KnowledgePoint) -> Exercise:
        """生成词汇练习"""
        exercise_id = f"vocab_{point.id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # 模拟生成词汇练习
        question = f"请选择 '{point.text}' 的正确中文意思："
        
        # 生成选项
        options = [
            "正确的意思",
            "错误的意思1",
            "错误的意思2", 
            "错误的意思3"
        ]
        random.shuffle(options)
        
        exercise = Exercise(
            id=exercise_id,
            type=ExerciseType.VOCABULARY,
            difficulty=point.difficulty,
            knowledge_points=[point],
            question=question,
            options=options,
            correct_answer="正确的意思",
            explanation=f"'{point.text}' 的正确中文意思是 '正确的意思'。",
            hints=["注意单词的词性和用法"],
            points=10
        )
        
        return exercise
    
    def generate_grammar_exercise(self, point: KnowledgePoint) -> Exercise:
        """生成语法练习"""
        exercise_id = f"grammar_{point.id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # 模拟生成语法练习
        question = f"请改正以下句子中的语法错误：\n\n{point.text}"
        
        options = [
            "改正后的句子1",
            "改正后的句子2",
            "改正后的句子3",
            "改正后的句子4"
        ]
        random.shuffle(options)
        
        exercise = Exercise(
            id=exercise_id,
            type=ExerciseType.GRAMMAR,
            difficulty=point.difficulty,
            knowledge_points=[point],
            question=question,
            options=options,
            correct_answer="改正后的句子1",
            explanation=f"原句中的语法错误是...，正确的应该是...",
            hints=["注意动词变位和词序"],
            points=15
        )
        
        return exercise
    
    def generate_pronunciation_exercise(self, point: KnowledgePoint) -> Exercise:
        """生成发音练习"""
        exercise_id = f"pron_{point.id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        question = f"请选择单词 '{point.text}' 的正确发音："
        
        options = [
            "发音描述1",
            "发音描述2", 
            "发音描述3"
        ]
        random.shuffle(options)
        
        exercise = Exercise(
            id=exercise_id,
            type=ExerciseType.PRONUNCIATION,
            difficulty=point.difficulty,
            knowledge_points=[point],
            question=question,
            options=options,
            correct_answer="发音描述1",
            explanation=f"'{point.text}' 的正确发音是...",
            hints=["注意元音长度和辅音清浊"],
            points=10
        )
        
        return exercise
    
    def generate_expression_exercise(self, point: KnowledgePoint) -> Exercise:
        """生成表达练习"""
        exercise_id = f"expr_{point.id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        question = f"在以下情景中，应该说什么：\n\n{point.text}"
        
        options = [
            "合适的表达1",
            "不合适的表达2",
            "不合适的表达3",
            "不合适的表达4"
        ]
        random.shuffle(options)
        
        exercise = Exercise(
            id=exercise_id,
            type=ExerciseType.EXPRESSION,
            difficulty=point.difficulty,
            knowledge_points=[point],
            question=question,
            options=options,
            correct_answer="合适的表达1",
            explanation=f"在这个情景中，合适的表达是...",
            hints=["注意礼貌程度和场合"],
            points=12
        )
        
        return exercise
    
    def generate_integrated_exercise(self, points: List[KnowledgePoint]) -> Exercise:
        """生成综合练习"""
        exercise_id = f"integrated_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # 基于多个知识点生成综合练习
        categories = list(set(p.category for p in points))
        question = f"请根据以下知识点完成综合练习：\n\n"
        for i, point in enumerate(points, 1):
            question += f"{i}. {point.text}\n"
        
        question += "\n请选择正确的选项："
        
        options = [
            "综合正确答案",
            "部分正确选项",
            "完全错误选项",
            "相关但不正确选项"
        ]
        
        exercise = Exercise(
            id=exercise_id,
            type=ExerciseType.INTEGRATED,
            difficulty=DifficultyLevel.INTERMEDIATE,
            knowledge_points=points,
            question=question,
            options=options,
            correct_answer="综合正确答案",
            explanation="这个综合练习考察了多个知识点的综合应用...",
            hints=["注意知识点之间的联系"],
            points=20,
            time_limit=120
        )
        
        return exercise
    
    def generate_exercise_set(self, 
                            exercise_count: int = 10,
                            focus_categories: Optional[List[str]] = None,
                            focus_units: Optional[List[str]] = None) -> List[Exercise]:
        """生成一组练习"""
        exercises = []
        
        # 1. 选择知识点
        knowledge_points = self.select_knowledge_points(
            count=exercise_count * 2,  # 多选一些，用于综合练习
            focus_categories=focus_categories,
            focus_units=focus_units
        )
        
        # 2. 按分类分组知识点
        points_by_category = {}
        for point in knowledge_points:
            if point.category not in points_by_category:
                points_by_category[point.category] = []
            points_by_category[point.category].append(point)
        
        # 3. 为每个分类生成练习
        exercises_generated = 0
        for category, points in points_by_category.items():
            if exercises_generated >= exercise_count:
                break
            
            for point in points[:3]:  # 每个分类最多3个练习
                if exercises_generated >= exercise_count:
                    break
                
                # 根据分类生成不同类型的练习
                if category == "vocabulary":
                    exercise = self.generate_vocabulary_exercise(point)
                elif category == "grammar":
                    exercise = self.generate_grammar_exercise(point)
                elif category == "pronunciation":
                    exercise = self.generate_pronunciation_exercise(point)
                elif category == "expression":
                    exercise = self.generate_expression_exercise(point)
                else:
                    # 默认生成词汇练习
                    exercise = self.generate_vocabulary_exercise(point)
                
                exercises.append(exercise)
                exercises_generated += 1
        
        # 4. 如果还不够，添加综合练习
        if exercises_generated < exercise_count:
            remaining_points = knowledge_points[exercises_generated:]
            if len(remaining_points) >= 3:
                integrated_exercise = self.generate_integrated_exercise(remaining_points[:3])
                exercises.append(integrated_exercise)
                exercises_generated += 1
        
        logger.info(f"生成了 {len(exercises)} 个练习")
        return exercises
    
    def save_exercises(self, exercises: List[Exercise], filename: Optional[str] = None):
        """保存练习到文件"""
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"exercises_{timestamp}.json"
        
        filepath = self.exercises_path / filename
        
        # 转换练习对象为字典
        exercises_data = []
        for exercise in exercises:
            exercise_dict = {
                "id": exercise.id,
                "type": exercise.type.value,
                "difficulty": exercise.difficulty.value,
                "knowledge_points": [
                    {
                        "id": point.id,
                        "text": point.text,
                        "category": point.category,
                        "unit": point.unit
                    }
                    for point in exercise.knowledge_points
                ],
                "question": exercise.question,
                "options": exercise.options,
                "correct_answer": exercise.correct_answer,
                "explanation": exercise.explanation,
                "hints": exercise.hints,
                "time_limit": exercise.time_limit,
                "points": exercise.points
            }
            exercises_data.append(exercise_dict)
        
        # 添加元数据
        data = {
            "metadata": {
                "generated_at": datetime.datetime.now().isoformat(),
                "exercise_count": len(exercises),
                "knowledge_points_covered": len(set(
                    point.id for exercise in exercises for point in exercise.knowledge_points
                )),
                "categories": list(set(
                    point.category for exercise in exercises for point in exercise.knowledge_points
                )),
                "units": list(set(
                    point.unit for exercise in exercises for point in exercise.knowledge_points
                ))
            },
            "exercises": exercises_data
        }
        
        # 保存到文件
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"练习已保存到: {filepath}")
        return filepath
    
    def generate_markdown_report(self, exercises: List[Exercise]) -> str:
        """生成 Markdown 格式的练习报告"""
        timestamp = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M")
        
        report = f"# 智能练习生成报告\n\n"
        report += f"**生成时间**: {timestamp}\n"
        report += f"**练习数量**: {len(exercises)} 个\n"
        report += f"**预计完成时间**: {len(exercises) * 2} 分钟\n\n"
        
        # 统计信息
        categories = {}
        units = {}
        difficulties = {}
        
        for exercise in exercises:
            # 分类统计
            for point in exercise.knowledge_points:
                categories[point.category] = categories.get(point.category, 0) + 1
                units[point.unit] = units.get(point.unit, 0) + 1
            
            # 难度统计
            diff = exercise.difficulty.value
            difficulties[diff] = difficulties.get(diff, 0) + 1
        
        report += "## 📊 练习统计\n\n"
        
        report += "### 分类分布\n"
        for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            report += f"- **{category}**: {count} 个练习\n"
        
        report += "\n### 单元分布\n"
        for unit, count in sorted(units.items(), key=lambda x: x[1], reverse=True):
            report += f"- **{unit}**: {count} 个练习\n"
        
        report += "\n### 难度分布\n"
        for diff, count in sorted(difficulties.items(), key=lambda x: x[1], reverse=True):
            report += f"- **{diff}**: {count} 个练习\n"
        
        # 练习列表
        report += "\n## 🧪 练习列表\n\n"
        
        for i, exercise in enumerate(exercises, 1):
            report += f"### 练习 {i}: {exercise.type.value}\n"
            report += f"**难度**: {exercise.difficulty.value}  |  **分值**: {exercise.points} 分\n"
            
            if exercise.time_limit:
                report += f"**时间限制**: {exercise.time_limit} 秒\n"
            
            report += f"\n**题目**:\n"
            report += f"> {exercise.question}\n\n"
            
            if exercise.options:
                report += "**选项**:\n"
                for j, option in enumerate(exercise.options, 1):
                    report += f"{j}. {option}\n"
                report += "\n"
            
            report += f"**提示**: {', '.join(exercise.hints)}\n"
            report += f"**知识点**: {', '.join([p.text[:20] + '...' for p in exercise.knowledge_points])}\n"
            
            report += "\n---\n\n"
        
        # 学习建议
        report += "## 💡 学习建议\n\n"
        
        # 基于薄弱环节的建议
        weak_categories = [cat for cat, count in categories.items() if count >= 3]
        if weak_categories:
            report += "### 重点关注\n"
            report += f"建议重点关注以下分类的练习：{', '.join(weak_categories)}\n\n"
        
        # 时间管理建议
        total_time = len(exercises) * 2
        report += "### 时间管理\n"
        report += f"1. **总时间**: 预计需要 {total_time} 分钟\n"
        report += f"2. **建议分段**: 每完成5个练习休息2分钟\n"
        report += f"3. **最佳时段**: 选择注意力集中的时间段完成\n\n"
        
        # 练习策略
        report += "### 练习策略\n"
        report += "1. **先易后难**: 从简单的练习开始，逐步增加难度\n"
        report += "2. **及时复习**: 完成练习后立即查看解释\n"
        report += "3. **错题记录**: 记录做错的题目，定期复习\n"
        report += "4. **主动思考**: 不仅选择答案，还要理解为什么\n"
        
        # 系统信息
        report += "\n---\n\n"
        report += "**🤖 生成系统**: 基于知识网络的智能练习生成器\n"
        report += f"**📅 报告版本**: v1.0\n"
        report += f"**🔗 知识网络**: 基于205个知识点分析\n"
        
        return report
    
    def save_markdown_report(self, report: str, filename: Optional[str] = None):
        """保存 Markdown 报告"""
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"exercise_report_{timestamp}.md"
        
        filepath = self.exercises_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Markdown 报告已保存到: {filepath}")
        return filepath

    def run_generation(self, 
                      exercise_count: int = 10,
                      focus_categories: Optional[List[str]] = None,
                      focus_units: Optional[List[str]] = None,
                      output_format: str = "both") -> Dict[str, Any]:
        """运行完整的练习生成流程"""
        logger.info("=" * 60)
        logger.info("开始智能练习生成流程")
        logger.info("=" * 60)
        
        try:
            # 1. 生成练习
            exercises = self.generate_exercise_set(
                exercise_count=exercise_count,
                focus_categories=focus_categories,
                focus_units=focus_units
            )
            
            # 2. 保存练习数据
            json_file = self.save_exercises(exercises)
            
            # 3. 生成并保存报告
            report = self.generate_markdown_report(exercises)
            md_file = self.save_markdown_report(report)
            
            # 4. 返回结果
            result = {
                "success": True,
                "exercises_generated": len(exercises),
                "json_file": str(json_file),
                "markdown_file": str(md_file),
                "categories_covered": list(set(
                    point.category for exercise in exercises for point in exercise.knowledge_points
                )),
                "units_covered": list(set(
                    point.unit for exercise in exercises for point in exercise.knowledge_points
                ))
            }
            
            logger.info(f"练习生成成功: {len(exercises)} 个练习")
            return result
            
        except Exception as e:
            logger.error(f"❌ 练习生成失败: {e}")
            return {
                "success": False,
                "error": str(e)
            }

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="基于知识网络的智能练习生成系统")
    parser.add_argument("--count", type=int, default=10, help="生成练习的数量")
    parser.add_argument("--categories", type=str, help="重点关注的分类，用逗号分隔")
    parser.add_argument("--units", type=str, help="重点关注的单元，用逗号分隔")
    parser.add_argument("--output", type=str, default="both", 
                       choices=["json", "markdown", "both"], 
                       help="输出格式")
    parser.add_argument("--test", action="store_true", help="测试模式")
    
    args = parser.parse_args()
    
    # 解析参数
    focus_categories = None
    if args.categories:
        focus_categories = [cat.strip() for cat in args.categories.split(",")]
    
    focus_units = None
    if args.units:
        focus_units = [unit.strip() for unit in args.units.split(",")]
    
    # 创建生成器
    knowledge_network_path = os.path.join(os.path.dirname(__file__), "docs", "knowledge-network")
    generator = ExerciseGenerator(knowledge_network_path)
    
    # 运行生成
    result = generator.run_generation(
        exercise_count=args.count,
        focus_categories=focus_categories,
        focus_units=focus_units,
        output_format=args.output
    )
    
    if result["success"]:
        print(f"\n练习生成成功！")
        print(f"生成数量: {result['exercises_generated']} 个练习")
        print(f"JSON文件: {result['json_file']}")
        print(f"Markdown报告: {result['markdown_file']}")
        print(f"覆盖分类: {', '.join(result['categories_covered'])}")
        print(f"覆盖单元: {', '.join(result['units_covered'])}")
        return 0
    else:
        print(f"\n❌ 练习生成失败: {result['error']}")
        return 1

if __name__ == "__main__":
    exit(main())