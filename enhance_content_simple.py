#!/usr/bin/env python3
"""
知识库内容增强脚本 - 简化版
将从 Notion 提取的内容整合到知识库中
"""

import os
from pathlib import Path
import datetime

def enhance_pronunciation_page():
    """增强发音知识库页面"""
    
    pronunciation_path = Path(__file__).parent / "docs" / "knowledge-library" / "categories" / "pronunciation.md"
    
    if not pronunciation_path.exists():
        print(f"发音页面不存在: {pronunciation_path}")
        return
    
    with open(pronunciation_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
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
    
    # 在文件末尾添加增强内容
    new_content = content + "\n\n" + enhanced_section
    
    with open(pronunciation_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"发音页面增强完成: {pronunciation_path}")

def enhance_vocabulary_page():
    """增强词汇知识库页面"""
    
    vocabulary_path = Path(__file__).parent / "docs" / "knowledge-library" / "categories" / "vocabulary.md"
    
    if not vocabulary_path.exists():
        print(f"词汇页面不存在: {vocabulary_path}")
        return
    
    with open(vocabulary_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 创建增强内容
    enhanced_section = f"""
### 从 Notion 提取的 L1 单元基础词汇

#### 基础词汇列表

##### 1. 连接词
- **aber**: but 但是
- **und**: and 并且
- **oder**: or 或者

##### 2. 代词
- **Sie**: 您 (正式)
- **ich**: 我
- **du**: 你 (非正式)
- **Ihnen**: 您 (与格)
- **dir**: 你 (与格)

##### 3. 动词
- **hören**: 听
- **sprechen**: 说
- **lesen**: 读
- **ergänzen**: 填写
- **an/kreuzen**: (填表，答题)打勾，勾选
- **weiß, weißt**: 知道
- **heißen**: 叫做
- **kommen**: 来
- **geht**: 过，进行 (gehen的第三人称单数)

##### 4. 问候语
- **Hallo!**: 你好！(搭讪，随意打招呼)
- **Guten Morgen!**: 早上好 (5-10a.m.)
- **Morgen!**: 早上好 (简写)
- **Guten Tag!**: 你好！(白天用)
- **Guten Abend**: 晚上好 (6-10p.m.)
- **Gute Nacht!**: 晚安

##### 5. 告别语
- **Auf Wiedersehen!**: 期待再见 (正式)
- **Tschüss!**: Bye！(非正式)
- **Ciao**: 再见 (意大利语)
- **Bis morgen**: 明天见！
- **Bis gleich**: 一会见！
- **Bis bald**: 期待不久之后见

##### 6. 其他词汇
- **bitte**: please 请
- **long-kurz**: 长 - 短
- **richtig-falsch**: 正确 - 错误
- **was**: what 什么
- **wo**: where 哪里
- **Tag**: day 白天，一天
- **Morgen**: morning 早晨，清晨
- **Abend**: 傍晚
- **Nacht**: night 夜晚
- **Wie**: how 怎么样
- **Danke**: 谢谢
- **gut**: 好
- **auch**: 也
- **sehr**: 非常
- **angenehm**: 愉快的，惬意的
- **nicht**: 不
- **schlecht**: 不好
- **Solala**: 一般般
- **ja**: 是
- **nein**: 不是
- **aus**: 从...
- **woher**: 从哪？

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
**词汇数量**: 40+ 个基础词汇
**更新状态**: 内容深度优化完成
"""
    
    # 在文件末尾添加增强内容
    new_content = content + "\n\n" + enhanced_section
    
    with open(vocabulary_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"词汇页面增强完成: {vocabulary_path}")

def enhance_expression_page():
    """增强表达知识库页面"""
    
    expression_path = Path(__file__).parent / "docs" / "knowledge-library" / "categories" / "expression.md"
    
    if not expression_path.exists():
        print(f"表达页面不存在: {expression_path}")
        return
    
    with open(expression_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 创建增强内容
    enhanced_section = f"""
### 从 Notion 提取的 L1 单元对话示例

#### 基础对话练习

##### 对话 1: 问候与回应
```
A: Wie geht es dir? (你怎么样？)
B: Danke, gut. Und dir? (谢谢，很好。你呢？)
A: Auch gut, danke! (也很好，谢谢！)
```

##### 对话 2: 自我介绍
```
A: Wie heißt du? (你叫什么名字？)
B: Ich heiß XiaoLin. Und du? (我叫小林，你呢？)
A: Ich heiß XiaoMing. (我叫小明)
B: Sehr angenehm! (非常高兴认识你！)
```

##### 对话 3: 询问来源
```
A: Kommst du aus Shanghai? (你来自上海吗？)
B: Nein, ich komme aus Beijing. Und du? (不是，我来自北京，你呢？)
A: Ich komme aus Shanghai. (我来自上海)
```

##### 对话 4: 详细询问
```
A: Woher kommst du? (你是从哪来的？)
B: Ich komme aus Beijing. (我来自北京)
```

#### 常用对话模式

##### 正式问候
```
A: Guten Tag! Wie geht es Ihnen? (您好！您过得怎么样？)
B: Guten Tag! Danke, gut. Und Ihnen? (您好！谢谢，不错。您呢？)
A: Auch gut, danke. (也挺好，谢谢)
```

##### 非正式问候
```
A: Hallo! Wie geht's? (嗨！怎么样？)
B: Hallo! Danke, gut. Und dir? (嗨！谢谢，不错。你呢？)
A: Auch gut! (也挺好！)
```

##### 时间问候
```
早晨: Guten Morgen! (早上好！)
白天: Guten Tag! (你好！)
傍晚: Guten Abend! (晚上好！)
晚上: Gute Nacht! (晚安！)
```

##### 告别表达
```
正式: Auf Wiedersehen! (期待再见！)
非正式: Tschüss! (拜拜！)
约定: Bis morgen! (明天见！)
```

#### 情景表达练习

##### 餐厅场景
```
服务员: Guten Tag! Was möchten Sie bestellen? (您好！您想点什么？)
顾客: Guten Tag! Ich möchte eine Pizza, bitte. (您好！我想要一个披萨，请)
服务员: Eine Pizza. Sonst noch etwas? (一个披萨。还要别的吗？)
顾客: Nein, danke. Das ist alles. (不用了，谢谢。就这些)
```

##### 购物场景
```
顾客: Entschuldigung, haben Sie dieses Buch? (不好意思，你们有这本书吗？)
店员: Ja, wir haben es. Es kostet 20 Euro. (是的，我们有。20欧元)
顾客: Gut, ich nehme es. (好的，我要了)
```

##### 问路场景
```
游客: Entschuldigung, wo ist der Bahnhof? (不好意思，火车站在哪？)
当地人: Gehen Sie geradeaus, dann links. (直走，然后左转)
游客: Wie weit ist es? (有多远？)
当地人: Etwa 10 Minuten zu Fuß. (大约步行10分钟)
游客: Vielen Dank! (非常感谢！)
当地人: Bitte schön! (不客气！)
```

---

**内容来源**: Notion L1 单元笔记
**提取时间**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')}
**更新状态**: 内容深度优化完成
"""
    
    # 在文件末尾添加增强内容
    new_content = content + "\n\n" + enhanced_section
    
    with open(expression_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"表达页面增强完成: {expression_path}")

def main():
    """主函数"""
    print("开始知识库内容深度优化...")
    
    # 增强发音页面
    enhance_pronunciation_page()
    
    # 增强词汇页面
    enhance_vocabulary_page()
    
    # 增强表达页面
    enhance_expression_page()
    
    print("知识库内容深度优化完成！")

if __name__ == "__main__":
    main()