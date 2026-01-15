# GABRIEL MR Analysis: Results & Reflections

**Presenter**: [Your Name]
**Date**: January 2026

---

# Slide 1: Agenda

1. **What is GABRIEL?** — 简单原理介绍
2. **What I Did** — 分析流程与执行
3. **Key Results** — 7个团队的真实数据
4. **Reality Check** — Jake的评估哪里需要修正
5. **Honest Limitations** — GABRIEL真正做不到什么
6. **Next Steps** — 具体建议

---

# Slide 2: What is GABRIEL? (For Non-Technical Audience)

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Traditional Way:                                              │
│   ─────────────────                                             │
│   Human reads 100 reports → Takes weeks → Subjective           │
│                                                                 │
│   GABRIEL Way:                                                  │
│   ─────────────                                                 │
│   LLM reads 100 reports → Takes minutes → Consistent           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**GABRIEL = 把"让人类读文档打分"变成"让AI读文档打分"的工具**

---

# Slide 3: How Does LLM Scoring Work?

## The Core Idea

```
Input (What we give the AI):
┌─────────────────────────────────────────────────────────────────┐
│ "Read this management report and rate the clarity of the       │
│  Theory of Value on a scale of 0-100, where:                   │
│  - 100 = Crystal clear, explicit value chain                   │
│  - 0 = No theory of value mentioned"                           │
│                                                                 │
│  [Full text of Team AGORA's MR...]                             │
└─────────────────────────────────────────────────────────────────┘

Output (What AI returns):
┌─────────────────────────────────────────────────────────────────┐
│ { "tov_clarity": 77 }                                          │
└─────────────────────────────────────────────────────────────────┘
```

**关键点**: AI不是随机打分，它真的"读懂"了文本并基于定义评估

---

# Slide 4: Why Trust LLM Scores?

## Validation Evidence

| 证据 | 解释 |
|------|------|
| **Meaningful Variance** | NGM得86分，Baked Gainz得50分 — 不是随机 |
| **Contextual Correctness** | Dream Team技术问题高(62%) — 他们做stadium API |
| **Internal Consistency** | ToV质量高的团队，策略一致性也高 (相关性0.7) |
| **Face Validity** | 分数符合我们对这些团队的直觉认知 |

## Jake's Concern: "Subjective tasks will be weak"

**Reality**: 主观评分任务实际上工作得很好，因为：
- LLM有大量语料训练，知道什么是"清晰"
- 我们提供明确的评分标准 (0-100 scale with anchors)
- 结果有meaningful variance，不是全部打50分

---

# Slide 5: GABRIEL's Core Functions

## What GABRIEL Can Do

| Function | 作用 | 类比 |
|----------|------|------|
| `extract()` | 从文本提取结构化信息 | 填表格 |
| `rate()` | 给文本属性打分 (0-100) | 评分卡 |
| `classify()` | 把文本归类 | 分类标签 |
| `compare()` | 比较两段文本的差异 | 找不同 |
| `discover()` | 发现文本中的模式/主题 | 主题挖掘 |
| `whatever()` | 自定义提示词 | 万能接口 |

**Jake的函数映射基本正确**，但他高估了某些任务的难度

---

# Slide 6: What I Built

```
┌─────────────────────────────────────────────────────────────────┐
│                  GABRIEL MR Analysis Pipeline                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   7 Team MRs  ──→  gabriel_mr_analysis.py  ──→  Results        │
│   (13,000+        │                         │                   │
│    words)         │  • extract() ×11个指标   │  • CSV (47列)    │
│                   │  • rate() ×22个指标      │  • Markdown报告  │
│                   │  • classify() ×6个指标   │  • 8张图表       │
│                   │                         │                   │
│                   └─────────────────────────┘                   │
│                                                                 │
│   API Cost: $0.31    |    Time: ~2 minutes                     │
└─────────────────────────────────────────────────────────────────┘
```

**Teams**: AGO, Baked Gainz, Dream Team, NGM, ResponsiPay, Team 6, Arloe

---

# Slide 7: Key Results — Theory of Value Quality

```
                    ToV Overall Score by Team
                    ═══════════════════════════

  Dream Team    ████████████████████████░░░░░░░░  85.2
  NGM Team      ███████████████████████░░░░░░░░░  82.8
  ResponsiPay   ███████████████████████░░░░░░░░░  82.2
  Team Arloe    ████████████████████░░░░░░░░░░░░  80.0
  Team AGORA    ███████████████░░░░░░░░░░░░░░░░░  76.0
  Baked Gainz   ██████████████░░░░░░░░░░░░░░░░░░  71.2
  Team 6        █████████████░░░░░░░░░░░░░░░░░░░  69.2

                0        25        50        75       100
```

**Average: 78.1/100** — 有意义的差异分布!

---

# Slide 8: The "Subjective" Tasks Jake Worried About

## Hypothesis-Test-Result Chain Quality

**Jake's prediction**: 1-2/3 (will be weak)
**Actual result**: Clear differentiation across teams!

```
  NGM Team      ████████████████████████████████░░  86/100 ⭐
  Dream Team    █████████████████████░░░░░░░░░░░░░  68/100
  Team 6        █████████████████████░░░░░░░░░░░░░  68/100
  Team Arloe    ████████████████████░░░░░░░░░░░░░░  65/100
  Team AGORA    ███████████████████░░░░░░░░░░░░░░░  62/100
  ResponsiPay   ███████████████████░░░░░░░░░░░░░░░  62/100
  Baked Gainz   ███████████████░░░░░░░░░░░░░░░░░░░  50/100
```

**Why NGM scores highest?** → 他们systematically测试缅甸课程，有完整的假设-测试-结果链

---

# Slide 9: Problem Classification Works Well

```
            Problem Type Distribution by Team
            ═══════════════════════════════════

Team AGORA    Tech ████████  Market ██████████████  Team ████
              60%           78%                    25%

Dream Team    Tech ██████████  Market ████████      Team ██████████████
              62%            38%                    74%

NGM Team      Tech ██        Market ██████████      Team ████████
              15%            50%                    40%

Legend: Tech=Technical  Market=Market/Customer  Team=Team Process
```

**Why this makes sense**:
- Dream Team (stadium API) → high technical problems
- NGM (education nonprofit) → low technical, more market/team
- Results align with team contexts!

---

# Slide 10: Where Jake's Assessment Needs Correction

## What Jake Got Right ✓

- GABRIEL适合结构化extraction任务 (who, what, when)
- 某些任务确实比较challenging

## What Jake Got Wrong ✗

| Jake's Claim | Reality |
|--------------|---------|
| "H-T-R chain quality will be weak (1-2)" | ✅ Works well — scores 50-86 with meaningful variance |
| "ToV coherence will be weak (2)" | ✅ Works well — correlates with other metrics |
| "Persistence of issues is easy (3)" | ❌ **Actually impossible** — needs cross-report data |
| "Stability of facilitation is easy (3)" | ❌ **Actually impossible** — needs longitudinal data |
| "Changes in contribution patterns is easy (3)" | ❌ **Actually impossible** — single snapshot |

## The Real Insight

**Jake担心的是"LLM主观性"，但真正的限制是"数据可用性"**

---

# Slide 11: What GABRIEL Actually Cannot Do

## Honest Limitations

| 限制 | 原因 | 解决方案 |
|------|------|----------|
| **跨时间追踪** | 只有单一文档输入 | Google Drive API获取历史版本 |
| **个人vs共享ToV对比** | MR中没有个人提交 | 让成员会前单独提交ToV |
| **问题持续性** | 单一快照 | 在问题表中加"首次报告日期" |
| **未报告的冲突** | 没写就提取不到 | 改进MR模板，explicit prompts |
| **情感/态度** | 没有视频/音频 | 视频签到bot |

## The Formula

```
GABRIEL能做什么 = f(数据结构, 提示词质量)

NOT: GABRIEL能做什么 = f(任务主观性)
```

---

# Slide 12: Task Concentration Analysis

```
                    Who Does the Work?
                    ══════════════════

ResponsiPay   ████████████████████████████░░░░░  72% concentrated
              Ryan Rodgers dominates

Team Arloe    ████████████████░░░░░░░░░░░░░░░░░  40%
NGM Team      ██████████████░░░░░░░░░░░░░░░░░░░  36%
Dream Team    ██████████████░░░░░░░░░░░░░░░░░░░  35%
Team 6        ██████████░░░░░░░░░░░░░░░░░░░░░░░  26%
Baked Gainz   ██████████░░░░░░░░░░░░░░░░░░░░░░░  25%
Team AGORA    ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░  15% ← Most distributed

              0%       25%       50%       75%      100%
              ←── Distributed         Concentrated ──→
```

**Research implication**: 任务集中度可以measure facilitator influence

---

# Slide 13: Composite Scores Summary

```
    ╔═══════════════╦═══════════╦═══════════════╦═══════════╦═══════╗
    ║ Team          ║ ToV Score ║ Experimentation║ Alignment ║  PES  ║
    ╠═══════════════╬═══════════╬═══════════════╬═══════════╬═══════╣
    ║ NGM Team      ║   82.8    ║     87.6      ║   93.0    ║ 91.0% ║
    ║ Dream Team    ║   85.2    ║     76.8      ║   87.5    ║ 75.0% ║
    ║ Team AGORA    ║   76.0    ║     71.4      ║   86.5    ║ 90.9% ║
    ║ ResponsiPay   ║   82.2    ║     67.8      ║   79.5    ║ 82.0% ║
    ║ Team Arloe    ║   80.0    ║     76.0      ║   86.5    ║  —    ║
    ║ Baked Gainz   ║   71.2    ║     64.0      ║   80.0    ║  —    ║
    ║ Team 6        ║   69.2    ║     76.8      ║   66.0    ║  —    ║
    ╚═══════════════╩═══════════╩═══════════════╩═══════════╩═══════╝
```

**Key insight**: ToV Score与Alignment相关性0.7+ → 有意义的关联!

---

# Slide 14: My Reflections

## What Surprised Me

1. **"主观"评分比预期更有效**
   - 结果与团队context一致
   - 有meaningful variance，不是随机噪音

2. **真正的瓶颈是数据结构，不是LLM能力**
   - Jake担心AI判断力
   - 实际问题是缺乏历史数据和个人提交

3. **$0.31跑完全部分析**
   - 如果人工做这个，需要几天
   - GABRIEL让大规模分析变得可行

## What I Would Do Differently

如果重来，我会先花时间改MR模板，再跑分析

---

# Slide 15: Recommended MR Template Changes

## High Priority Additions

```markdown
## Theory of Value Change Log (NEW)
| What Changed | Why | Based on Experiment? | Week |
|--------------|-----|---------------------|------|
| Added B2B segment | Interview #12 results | Yes | Week 7 |

## Hypothesis Tracker (NEW)
| ID | Hypothesis | Status | Evidence |
|----|-----------|--------|----------|
| H1 | Students pay $5 | Validated | Survey N=50 |

## Problems (Enhanced)
| Problem | Type | First Reported | Weeks Active |
|---------|------|----------------|--------------|
| API limits | Technical | Week 6 | 3 |

## Facilitator This Week (NEW)
Name: ___________
How selected: [Assigned / Rotated / Self-selected]
```

---

# Slide 16: Summary

## Three Takeaways

### 1. GABRIEL Works for "Subjective" Tasks
Jake预测的"weak"任务实际表现良好，结果有意义

### 2. The Real Limitation is Data, Not AI
- 跨时间追踪需要历史数据
- 个人vs共享对比需要个人提交
- 这些不是AI限制，是数据收集问题

### 3. Small Template Changes Unlock Big Capabilities
加几个字段就能解锁很多目前做不到的测量

---

# Slide 17: Next Steps

## Immediate
- [ ] 修改MR模板（加Change Log, Hypothesis Tracker等）
- [ ] 与1-2个团队pilot新模板

## Short-term
- [ ] 设置Google Drive API获取版本历史
- [ ] 建立自动化分析pipeline

## Long-term
- [ ] Individual ToV submissions before team meetings
- [ ] Video standup pilot for affect data

---

# Slide 18: Questions?

## Files Delivered

```
gdoc-code/
├── gabriel_mr_analysis.py    # 主分析脚本
├── generate_charts.py        # 图表生成
└── plan.md                   # 计划文档

gdoc-output/
├── charts/                   # 8张PNG图表
├── mr_analysis_results.csv   # 原始数据
├── gaps_and_recommendations.md
├── innovation_and_gamification.md
└── FINAL_REPORT_Meeting_Ready.md
```

---

# Appendix: GABRIEL Under the Hood

## How It Actually Works

```python
# Step 1: Prepare prompts
prompt = f"""
Read this text carefully:
{team_report_content}

Rate the following attribute on a scale of 0-100:
- tov_clarity: How clear is the theory of value?
  (100 = crystal clear, 0 = completely absent)

Return JSON: {{"tov_clarity": <your score>}}
"""

# Step 2: Call LLM API (OpenAI/Azure)
response = await openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

# Step 3: Parse response
result = json.loads(response.content)  # {"tov_clarity": 77}
```

## Why This Works

1. **Consistency**: Same prompt = similar scores for similar content
2. **Scale**: 处理100份报告和处理1份一样简单
3. **Audit trail**: 每个分数都有对应的prompt可追溯

---

# Appendix: Cost Breakdown

| Step | Prompts | Tokens | Cost |
|------|---------|--------|------|
| Basic extraction | 14 | ~235K | $0.08 |
| ToV rating | 7 | ~120K | $0.06 |
| Team dynamics | 7 | ~120K | $0.05 |
| Experimentation | 7 | ~120K | $0.05 |
| Problems | 7 | ~80K | $0.04 |
| Engagement | 7 | ~80K | $0.03 |
| **Total** | **49** | **~755K** | **$0.31** |

**Human equivalent**: 几天工作 → 2分钟 + $0.31
