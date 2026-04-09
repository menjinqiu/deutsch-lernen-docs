#!/usr/bin/env python3
"""
知识库重构脚本
基于 Notion 实际内容重新设计知识库结构
"""

import os
from pathlib import Path
import datetime

def create_redesigned_l1_unit():
    """创建重构版的 L1 单元知识库"""
    
    # 首先替换原来的 L1 单元页面
    l1_path = Path(__file__).parent / "docs" / "knowledge-library" / "units" / "L1.md"
    
    content = f"""# L1 单元知识库

## 📚 单元概述

基于你的 Notion 学习笔记构建的 L1 单元知识库，包含发音规则、基础词汇和实用对话。

### 📊 内容统计
- **发音规则**: 20+ 条具体规则
- **基础词汇**: 40+ 个核心词汇
- **对话示例**: 4个基础对话 + 情景练习
- **学习重点**: 德语发音基础 + 日常交流

---

## 🔊 **发音规则 (从你的笔记提取)**

### 1. 元音发音
#### 基本元音
- **a, e, i, o, u** - 德语五个基本元音

#### 长元音标志
```
a：a aa ah      (如：Tag, Saal, Bahn)
e：e ee eh      (如：weg, See, mehr)
i：i ie ih      (如：wir, sie, ihn)
o：o oo oh      (如：von, Boot, ohne)
u：u uh         (如：du, Uhr)
```

### 2. e的发音规则 (你的笔记重点)
#### 三种发音
1. **长音 [e:]** (读作 ei~)
   - e, ee, eh
   - 示例：weg, See, mehr

2. **短音 [ɛ]** (读作 ai!)
   - e + 两个或以上辅音字母
   - ä + 两个或以上辅音字母
   - 示例：essen, Männer

3. **非重读音 [ə]** (啊和屙的中间音)
   - 前缀：ge-, be-
   - 后缀：-e, -er, -en, -el
   - 示例：gehen, besser, machen, Mantel

### 3. s的发音规则
1. **[s]** - s+辅音/词尾
   - Sklave, ist, das

2. **[s]** - ss
   - klasse

3. **[s]** - ß
   - heißen

4. **[z]** - sa-se-si-so-su
   - sagen, sehen, sie, so, suchen

5. **[z]** - s+元音
   - sagen
   *注意：s+元音时只能发浊辅音*

### 4. 特殊字母发音
#### h的发音
1. h+元音：作为辅音发 [h]
   - haben
2. 元音+h：h不发音，作为长元音标志
   - gehen, sehen

#### z的发音 [ts] (呲)
- zahlen, Platz, Rätsel, abends, circa

### 5. 复合元音发音
#### [ao] 发音 (凹)
- au：auf, Auto, Haus

#### [ai] 发音 (爱)
- ei, ai, ey, ay：Ei, Mai, Meyer, Bayern

#### [y] 发音 (aoai)
- eu, äu：deutsch, Häuser

*所有复合元音都发长音*

### 6. 重要字母组合
#### r的发音
1. r+元音：小舌音 (或"喝"代替)
   - ra-, re-, ri-, ro-, ru-
   - 示例：rot, reisen
2. 元音+r：元音化，近似 [a]
   - 示例：Ruhr

#### st, sp的发音规则
1. 词首/音节首：[ʃt], [ʃp]
   - 示例：stehen, sprechen
2. 词中/词尾：[st], [sp]
   - 示例：Fenster, Transport
   *注意：后接元音时浊化为 [ʃd], [ʃb]*

#### ch的发音规则 (重点)
1. **Ach-Laut [x]** (喝)
   - a, o, u, au + ch
   - 重点单词：acht, hoch, Buch, auch

2. **ich-Laut [ç]** (类似于西)
   - 其他元音 + ch
   - 示例：echt, mich, gleich, euch, Milch

3. ch + 元音：
   - [k]：Charakter, Chor, Chrom (a,o,l,r前)
   - [ç]：Chemie, China
   - [ʃ]：Chef (法语外来词)

### 7. 其他重要规则
#### ig的发音
1. 词尾：[ɪç] (依溪)
   - 示例：lustig
2. 后有元音：[ɪg]
   - 示例：igel

#### 名词后缀发音
- **-tion**：[tsi̯oːn] (次用，41)
- **-ssion**：[si̯oːn] (思用，41)
- **-sion**：[zi̯oːn] (z用，41)
- **-ismus**：重音在 [i] 上，阳性名词

---

## 📖 **基础词汇 (从你的笔记提取)**

### 1. 连接词
- **aber** - 但是
- **und** - 并且
- **oder** - 或者

### 2. 代词
- **Sie** - 您 (正式)
- **ich** - 我
- **du** - 你 (非正式)
- **Ihnen** - 您 (与格)
- **dir** - 你 (与格)

### 3. 动词
- **hören** - 听
- **sprechen** - 说
- **lesen** - 读
- **ergänzen** - 填写
- **an/kreuzen** - (填表，答题)打勾，勾选
- **weiß, weißt** - 知道
- **heißen** - 叫做
- **kommen** - 来
- **geht** - 过，进行

### 4. 问候语
- **Hallo!** - 你好！(搭讪，随意打招呼)
- **Guten Morgen!** - 早上好 (5-10a.m.)
- **Morgen!** - 早上好 (简写)
- **Guten Tag!** - 你好！(白天用)
- **Guten Abend** - 晚上好 (6-10p.m.)
- **Gute Nacht!** - 晚安

### 5. 告别语
- **Auf Wiedersehen!** - 期待再见 (正式)
- **Tschüss!** - Bye！(非正式)
- **Ciao** - 再见 (意大利语)
- **Bis morgen** - 明天见！
- **Bis gleich** - 一会见！
- **Bis bald** - 期待不久之后见

### 6. 其他实用词汇
- **bitte** - 请
- **was** - 什么
- **wo** - 哪里
- **wie** - 怎么样
- **danke** - 谢谢
- **gut** - 好
- **auch** - 也
- **sehr** - 非常
- **nicht** - 不
- **ja** - 是
- **nein** - 不是
- **aus** - 从...
- **woher** - 从哪？

### 7. 时间相关
- **Tag** - 白天，一天
- **Morgen** - 早晨，清晨
- **Abend** - 傍晚
- **Nacht** - 夜晚

### 8. 状态描述
- **richtig** - 正确
- **falsch** - 错误
- **schlecht** - 不好
- **Solala** - 一般般
- **angenehm** - 愉快的，惬意的

---

## 💬 **实用对话 (从你的笔记提取)**

### 1. 基础问候对话
#### 正式问候
```
A: Guten Tag! Wie geht es Ihnen?
   (您好！您过得怎么样？)
B: Guten Tag! Danke, gut. Und Ihnen?
   (您好！谢谢，不错。您呢？)
A: Auch gut, danke.
   (也挺好，谢谢)
```

#### 非正式问候
```
A: Hallo! Wie geht's?
   (嗨！怎么样？)
B: Hallo! Danke, gut. Und dir?
   (嗨！谢谢，不错。你呢？)
A: Auch gut!
   (也挺好！)
```

### 2. 自我介绍对话
```
A: Wie heißt du?
   (你叫什么名字？)
B: Ich heiß XiaoLin. Und du?
   (我叫小林，你呢？)
A: Ich heiß XiaoMing.
   (我叫小明)
B: Sehr angenehm!
   (非常高兴认识你！)
```

### 3. 询问来源对话
```
A: Kommst du aus Shanghai?
   (你来自上海吗？)
B: Nein, ich komme aus Beijing. Und du?
   (不是，我来自北京，你呢？)
A: Ich komme aus Shanghai.
   (我来自上海)
```

### 4. 详细询问对话
```
A: Woher kommst du?
   (你是从哪来的？)
B: Ich komme aus Beijing.
   (我来自北京)
```

### 5. 状态表达
- **Sehr gut** - 非常好
- **Nicht schlecht!** - 不差
- **Solala!** - 一般般！
- **Schlecht** - 不好

---

## 🎯 **学习重点总结**

### 发音重点
1. **e的三种发音** - 长音、短音、非重读音
2. **ch的两种发音** - Ach-Laut 和 ich-Laut
3. **复合元音** - au, ei, eu 的发音
4. **特殊字母组合** - st/sp, sch, tsch

### 词汇重点
1. **基础问候语** - Hallo, Guten Tag, Auf Wiedersehen
2. **人称代词** - ich, du, Sie
3. **常用动词** - hören, sprechen, lesen
4. **连接词** - aber, und, oder

### 表达重点
1. **自我介绍** - Wie heißt du? Ich heiß...
2. **询问来源** - Woher kommst du? Ich komme aus...
3. **日常问候** - Wie geht es dir? Danke, gut.
4. **礼貌表达** - bitte, danke, sehr angenehm

---

## 📝 **学习建议**

### 发音练习
1. **跟读练习** - 跟着录音练习发音
2. **对比练习** - 对比相似发音的区别
3. **单词练习** - 在单词中练习发音规则
4. **句子练习** - 在句子中练习连贯发音

### 词汇记忆
1. **分类记忆** - 按词性分类记忆
2. **情景记忆** - 在对话情景中记忆
3. **重复记忆** - 多次重复加强记忆
4. **应用记忆** - 在实际中使用记忆

### 对话练习
1. **角色扮演** - 扮演不同角色练习对话
2. **情景模拟** - 模拟真实场景练习
3. **录音对比** - 录音后与标准对比
4. **实际应用** - 在实际交流中应用

---

## 🔗 **相关资源**

### 你的 Notion 笔记
- L1 单元完整笔记
- 发音规则详细记录
- 词汇和对话整理

### 练习资源
- [发音练习](../categories/pronunciation.md)
- [词汇练习](../categories/vocabulary.md)
- [表达练习](../categories/expression.md)
- [智能练习生成器](../../tools/exercise-system.md)

### 学习工具
- [知识搜索](../search.md)
- [学习路径](../learning-paths.md)
- [进度追踪](../progress.md)

---

**最后更新**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}  
**内容来源**: 你的 Notion L1 单元学习笔记  
**重构原则**: 去除空洞内容，提取具体价值  
**学习状态**: 待开始学习  
**掌握目标**: 发音准确 + 词汇熟练 + 对话流利