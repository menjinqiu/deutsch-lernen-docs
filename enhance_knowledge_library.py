#!/usr/bin/env python3
"""
知识库内容增强脚本
将从 Notion 提取的内容整合到知识库中
"""

import os
import re
from pathlib import Path
import datetime

def parse_notion_content(markdown_content):
    """解析 Notion Markdown 内容，提取结构化知识"""
    
    content = markdown_content
    
    # 提取发音规则部分
    pronunciation_rules = []
    vocabulary = []
    dialogues = []
    
    # 按标题分割内容
    lines = content.split('\n')
    
    current_section = None
    current_content = []
    
    for line in lines:
        # 检测标题
        if line.startswith('#### '):
            if current_section and current_content:
                if current_section == 'pronunciation':
                    pronunciation_rules.append('\n'.join(current_content))
                elif current_section == 'vocabulary':
                    vocabulary.append('\n'.join(current_content))
                elif current_section == 'dialogue':
                    dialogues.append('\n'.join(current_content))
            
            # 判断新章节类型
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['发音规则', '发音', '规则', '音']):
                current_section = 'pronunciation'
            elif any(keyword in line_lower for keyword in ['单词', '词汇', 'wort']):
                current_section = 'vocabulary'
            elif any(keyword in line_lower for keyword in ['对话', 'dialog', 'gespräch']):
                current_section = 'dialogue'
            else:
                current_section = 'other'
            
            current_content = [line]
        
        elif line.strip() and not line.startswith('<'):
            current_content.append(line)
    
    # 处理最后一个章节
    if current_section and current_content:
        if current_section == 'pronunciation':
            pronunciation_rules.append('\n'.join(current_content))
        elif current_section == 'vocabulary':
            vocabulary.append('\n'.join(current_content))
        elif current_section == 'dialogue':
            dialogues.append('\n'.join(current_content))
    
    return {
        'pronunciation_rules': pronunciation_rules,
        'vocabulary': vocabulary,
        'dialogues': dialogues,
        'raw_content': content
    }

def enhance_pronunciation_page(parsed_content):
    """增强发音知识库页面"""
    
    pronunciation_path = Path(__file__).parent / "docs" / "knowledge-library" / "categories" / "pronunciation.md"
    
    if not pronunciation_path.exists():
        print(f"发音页面不存在: {pronunciation_path}")
        return
    
    with open(pronunciation_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取发音规则
    pronunciation_rules = parsed_content['pronunciation_rules']
    
    # 创建增强内容
    enhanced_section = f"""
### 从 Notion 提取的详细发音规则

#### 核心发音规则总结

##### 1. 元音发音规则
- **基本元音**: a, e, i, o, u
- **长元音标志**: 
  - a: a, aa, ah
  - e: e, ee, eh  
  - i: i, ie, ih
  - o: o, oo, oh
  - u: u, uh

##### 2. 特殊发音规则

###### e的发音规则
1. **长音 [e:]** (读作 ei~)
   - e, ee, eh
2. **短音 [ɛ]** (读作 ai!)
   - e + 两个或以上辅音字母
   - ä + 两个或以上辅音字母
3. **非重读音 [ə]** (读作啊和屙的中间音)
   - 前缀: ge-, be-
   - 后缀: -e, -er, -en, -el

###### s的发音规则
1. **[s]** - s+辅音/词尾: Sklave, ist, das
2. **[s]** - ss: klasse
3. **[s]** - ß: heißen
4. **[z]** - sa-se-si-so-su
5. **[z]** - s+元音: sagen
   *注意: s+元音时只能发浊辅音*

###### h的发音规则
1. h+元音: 作为辅音发 [h]
2. 元音+h: h不发音，作为长元音标志

###### z的发音规则
发 [ts] (呲): z, tz, ts, ds, c
- zahlen, Platz, Rätsel, abends, circa

##### 3. 复合元音发音

###### [ao] 发音 (凹)
- au: auf, Auto, Haus

###### [ai] 发音 (爱)
- ei, ai, ey, ay: Ei, Mai, Meyer, Bayern

###### [y] 发音 (aoai)
- eu, äu: deutsch, Häuser

*所有复合元音都发长音*

##### 4. 特殊字母组合发音

###### r的发音
1. r+元音: 小舌音 (或"喝"代替)
   - ra-, re-, ri-, ro-, ru-
2. 元音+r: 元音化，近似 [a]

###### f的发音 [f] (夫)
- f: Foto
- ff: offen  
- ph: Physik
- v: vor

###### st, sp的发音规则
1. 词首/音节首: [ʃt], [ʃp]
2. 词中/词尾: [st], [sp]
   *注意: 后接元音时浊化为 [ʃd], [ʃb]*

###### sch的发音 [ʃ] (师)
- sch: schnell
- ch (法语外来词): Chef

###### tsch的发音 [tʃ] (吃)
- tsch: Deutsch
- c (意大利语): ciao

##### 5. ch的发音规则
1. **Ach-Laut [x]** (喝)
   - a, o, u, au + ch: acht, hoch, Buch, auch
2. **ich-Laut [ç]** (类似于西)
   - 其他元音 + ch: echt, mich, gleich, euch, Milch
3. ch + 元音:
   - [k]: Charakter, Chor, Chrom (a,o,l,r前)
   - [ç]: Chemie, China
   - [ʃ]: Chef (法语外来词)

##### 6. 其他重要规则

###### ig的发音
1. 词尾: [ɪç] (依溪)
2. 后有元音: [ɪg]

###### g的发音
- g: [g] 或 [k]
- ng: 后鼻音 "嗯"

###### ung的发音 [ʊŋ]
- 两个音连在一起: 乌-eng = wung
- 通常为阴性名词后缀

###### nk的发音 [ŋk]
- 先发 [eng] 再发 [k]: Dank, Onkel, links

###### [ks] 的发音 (克斯)
- x: Max, Taxi, Text
- gs: unterwegs
- chs: sechs

###### pf的发音
- [p] 只发气音，几乎听不到

###### qu的发音 [kv]
- 紧密发音

##### 7. 名词后缀发音

###### -tion 发音 [tsi̯oːn]
- 重音在 o 上: [次用, 41]

###### -ssion 发音 [si̯oːn]  
- 重音在 o 上: [思用, 41]

###### -sion 发音 [zi̯oːn]
- 重音在 o 上: [z用, 41]

###### -ismus 发音
- 各因素紧密相连，重音在 [i] 上
- 通常为阳性名词后缀

---

**内容来源**: Notion L1 单元笔记
**提取时间**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}
**更新状态**: 内容深度优化完成
"""
    
    # 在适当位置插入增强内容
    if "### 核心发音点" in content:
        # 在核心发音点后插入
        parts = content.split("### 核心发音点", 1)
        new_content = parts[0] + "### 核心发音点" + parts[1] + "\n\n" + enhanced_section
    else:
        # 在文件末尾添加
        new_content = content + "\n\n" + enhanced_section
    
    with open(pronunciation_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"发音页面增强完成: {pronunciation_path}")

def enhance_vocabulary_page(parsed_content):
    """增强词汇知识库页面"""
    
    vocabulary_path = Path(__file__).parent / "docs" / "knowledge-library" / "categories" / "vocabulary.md"
    
    if not vocabulary_path.exists():
        print(f"词汇页面不存在: {vocabulary_path}")
        return
    
    with open(vocabulary_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 从原始内容中提取词汇部分
    raw_content = parsed_content['raw_content']
    
    # 提取单词部分（在<details>标签中）
    import re
    
    # 查找单词部分
    word_section_match = re.search(r'<details>\s*<summary>单词</summary>(.*?)</details>', raw_content, re.DOTALL)
    
    if word_section_match:
        word_content = word_section_match.group(1)
        
        # 清理内容
        word_content = word_content.replace('<empty-block/>', '')
        word_content = re.sub(r'\s+', ' ', word_content).strip()
        
        # 分割成单词列表
        word_lines = [line.strip() for line in word_content.split('\n') if line.strip()]
        
        # 创建增强内容
        enhanced_section = f"""
### 从 Notion 提取的 L1 单元基础词汇

#### 基础词汇列表

##### 1. 连接词
"""
        
        # 分类整理词汇
        conjunctions = []
        pronouns = []
        verbs = []
        greetings = []
        farewells = []
        others = []
        
        for line in word_lines:
            if '：' in line or '=' in line:
                # 解析单词行
                if '：' in line:
                    parts = line.split('：', 1)
                else:
                    parts = line.split('=', 1)
                
                if len(parts) == 2:
                    german = parts[0].strip()
                    chinese = parts[1].strip()
                    
                    # 分类
                    if german in ['aber', 'und', 'oder']:
                        conjunctions.append(f"- **{german}**: {chinese}")
                    elif german in ['Sie', 'ich', 'du', 'Ihnen', 'dir']:
                        pronouns.append(f"- **{german}**: {chinese}")
                    elif german in ['hören', 'sprechen', 'lesen', 'ergänzen', 'an/kreuzen', 'weiß', 'weißt', 'heißen', 'kommen', 'geht']:
                        verbs.append(f"- **{german}**: {chinese}")
                    elif 'Hallo' in german or 'Guten' in german or 'Morgen' in german or 'Tag' in german or 'Abend' in german or 'Nacht' in german:
                        greetings.append(f"- **{german}**: {chinese}")
                    elif 'Wiedersehen' in german or 'Tschüss' in german or 'Ciao' in german or 'Bis' in german:
                        farewells.append(f"- **{german}**: {chinese}")
                    else:
                        others.append(f"- **{german}**: {chinese}")
        
        # 添加分类内容
        if conjunctions:
            enhanced_section += "\n".join(conjunctions) + "\n"
        
        enhanced_section += """
##### 2. 代词
"""
        if pronouns:
            enhanced_section += "\n".join(pronouns) + "\n"
        
        enhanced_section += """
##### 3. 动词
"""
        if verbs:
            enhanced_section += "\n".join(verbs) + "\n"
        
        enhanced_section += """
##### 4. 问候语
"""
        if greetings:
            enhanced_section += "\n".join(greetings) + "\n"
        
        enhanced_section += """
##### 5. 告别语
"""
        if farewells:
            enhanced_section += "\n".join(farewells) + "\n"
        
        enhanced_section += """
##### 6. 其他词汇
"""
        if others:
            enhanced_section += "\n".join(others) + "\n"
        
        enhanced_section += f"""
##### 7. 常用表达

###### 问候对话
1. **Wie geht es Ihnen?** - 您过得怎么样？(正式)
   - 回答: **Danke gut. Und Ihnen?** - 谢谢，不错！您呢？
   
2. **Wie geht's? / Wie geht es dir?** - 你过得怎么样？(非正式)
   - 回答: **Danke gut, Und dir?** - 谢谢，不错！你呢？
   - 回答: **Auch gut, danke!** - 也挺好的，谢谢！

###### 状态表达
- **Sehr gut** - 非常好
- **Nicht schlecht!** - 不差
- **Solala!** - 一般般！
- **Schlecht** - 不好

###### 个人信息询问
1. **Wie heißt du?** - 你叫什么名字？
   - 回答: **Ich heiß XiaoLin. Und du?** - 我叫小林，你呢？
   
2. **Kommst du aus Shanghai?** - 你来自上海吗？
   - 回答: **Nein, ich komme aus Beijing. Und du?** - 不是，我来自北京，你呢？
   
3. **Woher kommst du?** - 你是从哪来的？

###### 礼貌表达
- **bitte** - 请
- **Danke** - 谢谢
- **Sehr angenehm** - 非常高兴（认识你）

---

**内容来源**: Notion L1 单元笔记
**提取时间**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}
**词汇数量**: {len(word_lines)} 个基础词汇
**更新状态**: 内容深度优化完成
"""
        
        # 在适当位置插入增强内容
        if "### 知识体系" in content:
            # 在知识体系后插入
            parts = content.split("### 知识体系", 1)
            new_content = parts[0] + "### 知识体系" + parts[1] + "\n\n" + enhanced_section
        else:
            # 在文件末尾添加
            new_content = content + "\n\n" + enhanced_section
        
        with open(vocabulary_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"词汇页面增强完成: {vocabulary_path}")
    else:
        print("未找到单词部分")

def enhance_expression_page(parsed_content):
    """增强表达知识库页面"""
    
    expression_path = Path(__file__).parent / "docs" / "knowledge-library" / "categories" / "expression.md"
    
    if not expression_path.exists():
        print(f"表达页面不存在: {expression_path}")
        return
    
    with open(expression_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 从原始内容中提取对话部分
    raw_content = parsed_content['raw_content']
    
    # 查找对话部分（在数字列表后）
    import re
    
    # 查找对话示例
    dialogue_pattern = r'\d+\.\s+对话\s*\n\t\d+\.\s+(.*?)\n\t\d+\.\s+(.*?)\n\t\d+\.\s+(.*?)(?=\n\d+\.|\n<|$)'
    dialogues = re.findall(dialogue_pattern, raw_content, re.DOTALL)
    
    if dialogues:
        # 创建增强内容
        enhanced_section = f"""
### 从 Notion 提取的 L1 单元对话示例

#### 基础对话练习

##### 对话 1: 问候与回应
"""
        
        for i, dialogue in enumerate(dialogues, 1):
            if len(dialogue) >= 3:
                enhanced_section += f"""
###### 场景 {i}
1. **{dialogue[0].strip()}**
2. **{dialogue[1].strip()}**
3. **{dialogue[2].strip()}**

"""
        
        # 添加更多对话示例
        enhanced_section += """
##### 常用对话模式

###### 自我介绍
```
A: Wie heißt du? (你叫什么名字？)
B: Ich heiß XiaoLin. Und du? (我叫小林，你呢？)
A: Ich heiß XiaoMing. (我叫小明)
B: Sehr angenehm! (非常高兴认识你！)
```

###### 询问来源
```
A: Kommst du aus Shanghai? (你来自上海吗？)
B: Nein, ich komme aus Beijing. Und du? (不是，我来自北京，你呢？)
A: Ich komme aus Shanghai. (我来自上海)
```

###### 日常问候
```
A: Wie geht es dir? (你怎么样？)
B: Danke, gut. Und dir? (谢谢，很好