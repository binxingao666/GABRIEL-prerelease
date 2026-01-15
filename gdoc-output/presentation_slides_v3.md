# GABRIEL MR Analysis: Results & Reflections

**Presenter**: [Your Name]
**Date**: January 2026

---

# Slide 1: Agenda

1. **What is GABRIEL?** — 简单原理介绍
2. **What I Did** — 分析流程与执行
3. **Key Results** — 7个团队的真实数据
4. **Capability Assessment** — 哪些任务可行，哪些需要改进
5. **MR Template Improvements** — 具体模板改进建议 (4 sub-slides)
6. **Validity Limitations** — Self-Report Extraction Problem
7. **Reflections & Next Steps**

---

# Slide 2: What is GABRIEL? (For Non-Technical Audience)

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Traditional Way:                                              │
│   ─────────────────                                             │
│   Human reads 100 reports → Takes weeks → Subjective bias       │
│                                                                 │
│   GABRIEL Way:                                                  │
│   ─────────────                                                 │
│   LLM reads 100 reports → Takes minutes → Consistent criteria   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**GABRIEL = 把"让人类读文档打分"变成"让AI读文档打分"的标准化工具**

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

**关键点**: AI基于明确定义的标准评估，不是随机打分

---

# Slide 4: Why Trust LLM Scores?

## Validation Evidence from This Analysis

| 证据类型 | 本次分析中的体现 |
|----------|------------------|
| **Meaningful Variance** | 同一指标，NGM得86分，Baked Gainz得50分 |
| **Contextual Correctness** | Dream Team技术问题高(62%) — 他们确实在做stadium API |
| **Internal Consistency** | ToV质量高的团队，策略一致性也高 (r=0.7) |
| **Face Validity** | 分数分布符合对这些团队的认知 |

---

# Slide 5: GABRIEL's Core Functions

| Function | 作用 | 类比 |
|----------|------|------|
| `extract()` | 从文本提取结构化信息 | 填表格 |
| `rate()` | 给文本属性打分 (0-100) | 评分卡 |
| `classify()` | 把文本归类 | 贴标签 |
| `compare()` | 比较两段文本的差异 | 找不同 |
| `discover()` | 发现文本中的模式/主题 | 主题挖掘 |
| `whatever()` | 自定义提示词分析 | 万能接口 |

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
│                   │  • classify() ×6个指标   │  • 可视化图表    │
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

                        Average: 78.1
```

---

# Slide 8: Hypothesis-Test-Result Chain Quality

## 这是一个"主观评估"任务 — 但结果很有意义

```
  NGM Team      ████████████████████████████████░░  86/100 ⭐
  Dream Team    █████████████████████░░░░░░░░░░░░░  68/100
  Team 6        █████████████████████░░░░░░░░░░░░░  68/100
  Team Arloe    ████████████████████░░░░░░░░░░░░░░  65/100
  Team AGORA    ███████████████████░░░░░░░░░░░░░░░  62/100
  ResponsiPay   ███████████████████░░░░░░░░░░░░░░░  62/100
  Baked Gainz   ███████████████░░░░░░░░░░░░░░░░░░░  50/100
```

**NGM为什么最高?**
他们对缅甸学生进行了系统性的课程测试，MR中有完整的假设→测试→结果→解释链条

---

# Slide 9: Problem Classification

```
            Problem Type Distribution by Team
            ═══════════════════════════════════

Team AGORA    Tech ████████░░  Market ████████████████  Team ████░░
              60%              78%                      25%

Dream Team    Tech ██████████  Market ████████░░░░░░░░  Team ██████████████
              62%              38%                      74%

NGM Team      Tech ██░░░░░░░░  Market ██████████░░░░░░  Team ████████░░
              15%              50%                      40%

Baked Gainz   Tech ██░░░░░░░░  Market ████░░░░░░░░░░░░  Team ██████████
              20%              30%                      45%
```

**分类结果与团队实际情况一致**:
- Dream Team做stadium技术集成 → 技术问题高
- Baked Gainz做饼干 → 技术问题低，团队协调问题多

---

# Slide 10: Task Concentration — Who Does the Work?

```
ResponsiPay   ████████████████████████████░░░░░  72%
              → 高度集中在一人

Team Arloe    ████████████████░░░░░░░░░░░░░░░░░  40%
NGM Team      ██████████████░░░░░░░░░░░░░░░░░░░  36%
Dream Team    ██████████████░░░░░░░░░░░░░░░░░░░  35%
Team 6        ██████████░░░░░░░░░░░░░░░░░░░░░░░  26%
Baked Gainz   ██████████░░░░░░░░░░░░░░░░░░░░░░░  25%
Team AGORA    ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░  15%
              → 分布最均匀

              0%       25%       50%       75%      100%
              ←── Distributed         Concentrated ──→
```

---

# Slide 11: Composite Scores Summary

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

**发现**: ToV质量与策略一致性显著相关 (r ≈ 0.7)

---

# Slide 12: Capability Assessment — What Works Well

## ✅ GABRIEL表现良好的任务

| 任务类型 | 示例 | 为什么有效 |
|----------|------|-----------|
| **结构化提取** | 团队成员、任务数量、问题数量 | 信息明确存在于文本中 |
| **质量评分** | ToV清晰度、实验严谨性 | 有明确评分标准，AI训练数据丰富 |
| **分类** | 问题类型、任务类型 | 类别定义清晰 |
| **单文档分析** | 任何单份MR的内容分析 | 完整上下文可用 |

---

# Slide 13: Capability Assessment — What Needs Work

## ⚠️ 当前数据结构下做不到的任务

| 任务 | 为什么做不到 | 解决方案 |
|------|-------------|----------|
| **跨时间追踪变化** | 只有单一文档，无历史版本 | Google Drive API获取版本历史 |
| **问题持续性** | 无法知道问题是否跨周存在 | MR中加"首次报告日期"字段 |
| **协调角色稳定性** | 无法比较不同周的协调者 | MR中加"本周协调者"字段 |
| **个人vs共享ToV对比** | MR中只有共享ToV | 让成员会前单独提交个人ToV |
| **贡献模式变化** | 单一快照无法看趋势 | 需要多份连续MR |

## 关键洞察

**限制不在于AI能力，而在于数据收集方式**

---

# Slide 14: MR Template Improvements — Overview

## 为什么要改模板？

```
┌─────────────────────────────────────────────────────────────────┐
│  Current MR Template          │  Research Capability            │
├───────────────────────────────┼─────────────────────────────────┤
│  ❌ No change tracking        │  Can't measure ToV revision     │
│  ❌ No problem dates          │  Can't measure persistence      │
│  ❌ No facilitator field      │  Can't track role stability     │
│  ❌ No individual submissions │  Can't measure convergence      │
│  ❌ No hypothesis tracker     │  Can't link experiments to ToV  │
└─────────────────────────────────────────────────────────────────┘
```

## Template Changes by Priority

| Change | Effort | Research Value | Unlocks |
|--------|--------|----------------|---------|
| ToV Change Log | 🟢 Low | 🔴 Critical | Revision tracking |
| Problem First Reported | 🟢 Low | 🔴 Critical | Persistence |
| Facilitator This Week | 🟢 Low | 🟡 High | Role stability |
| Hypothesis Tracker | 🟡 Medium | 🟡 High | Exp→ToV links |
| Individual ToV Submissions | 🟡 Medium | 🔴 Critical | Convergence |

---

# Slide 14.1: Template Change #1 — ToV Change Log

## 现状问题
MR只有当前ToV快照，无法知道ToV如何演变

## 新增字段

```markdown
## Theory of Value Change Log (NEW)
| What Changed | Why | Based on Experiment? | Week |
|--------------|-----|---------------------|------|
| Added B2B segment | Interview #12 showed demand | Yes | 7 |
| Dropped college market | Survey: low WTP | Yes | 9 |
| Pivoted to subscription | Competitor analysis | No | 11 |
```

## 研究价值
- 追踪ToV修订频率和原因
- 识别experiment-driven vs. intuition-driven changes
- 量化团队的learning velocity

---

# Slide 14.2: Template Change #2 — Problem Tracking Enhancement

## 现状问题
只知道"有问题"，不知道问题持续多久

## 改进字段

```markdown
## Problems (Enhanced)
| Problem | Type | Owner | First Reported | Weeks Active | Status |
|---------|------|-------|----------------|--------------|--------|
| API rate limits | Technical | RR | Week 6 | 3 | Open |
| Customer churn | Market | CF | Week 8 | 1 | Resolved |
```

## 研究价值
- 测量problem persistence（Section 4.6关键指标）
- 识别chronic blockers vs. quick fixes
- 关联problem duration与team performance

---

# Slide 14.3: Template Change #3 — Facilitator & Convergence

## 新增: Facilitator Tracking

```markdown
## This Week's Facilitator
- **Name**: ___________
- **Selection**: [ ] Assigned [ ] Rotated [ ] Self-selected
- **Key Decisions Made**: ___________
```

## 新增: Individual ToV Contributions (Pre-Meeting)

```markdown
## Individual ToV Proposals
| Member | My Proposed Focus | Incorporated? |
|--------|-------------------|---------------|
| Alice  | B2C local market | Yes |
| Bob    | B2B partnerships | Deferred |
| Carol  | Freemium model | No - voted against |
```

## 研究价值
- 追踪facilitation role stability
- 测量individual→shared ToV convergence（TBV核心问题）
- 量化"whose ideas get incorporated"

---

# Slide 14.4: Template Change #4 — Hypothesis Tracker

## 新增: Experiment-ToV Linkage

```markdown
## Hypothesis Tracker
| ID | Hypothesis | Status | Evidence | Linked ToV Element |
|----|-----------|--------|----------|-------------------|
| H1 | Students pay $5 | Validated | Survey N=50 | Revenue model |
| H2 | Parents are buyers | Testing | 3/10 interviews | Customer segment |
| H3 | Weekly usage | Invalidated | Analytics | Value prop |
```

## 新增: How Experiments Changed ToV

```markdown
## Experiment → ToV Changes
| Experiment | Finding | ToV Change Made |
|------------|---------|-----------------|
| Survey #1 | Low WTP in college | Dropped segment |
| Interview #5 | Parents pay | Added segment |
```

## 研究价值
- 显式连接experiments与ToV evolution
- 测量hypothesis-test-result chain quality
- 验证teams是否真的"evidence-based"

---

# Slide 15: Validity Limitation — The Self-Report Extraction Problem

## The Core Issue

**GABRIEL analyzes team narratives, not objective reality.**

```
Example from ResponsiPay:
┌──────────────────────────────────────────────────────────────┐
│ Objective Measure (task_concentration): 72%                   │
│ → Ryan Rodgers owns 60%+ of tasks in the table               │
│                                                               │
│ Self-Report Extraction (equal_distribution): "somewhat"       │
│ → Team wrote: "all found time to each contribute"             │
└──────────────────────────────────────────────────────────────┘
```

**GABRIEL faithfully extracted both. But they measure different things!**

---

# Slide 16: Which Metrics Are Affected?

## Self-Report Confound (Validity Risk)

| Risk Level | Metric | Issue |
|------------|--------|-------|
| 🔴 High | `conflict_evidence` | Teams hide or minimize conflicts |
| 🔴 High | `learning_evidence` | Teams claim learning without proof |
| 🔴 High | `problem_severity` | Subjective team assessment |
| 🟡 Medium | `has_pivot_mentioned` | Only if team chose to write it |

## More Objective (Lower Risk)

| Risk Level | Metric | Why More Reliable |
|------------|--------|-------------------|
| 🟢 Low | `task_concentration` | Counts task table entries |
| 🟢 Low | `tov_clarity` | AI assesses text quality |
| 🟢 Low | `num_problems_listed` | Objective count |

**Key Insight**: This is not a GABRIEL bug — it's a fundamental property of self-reported data

---

# Slide 17: Better Prompt Design

## ❌ Self-Report Extraction (Low Validity)

```python
"Does the work appear equally distributed among all members?
 (yes/somewhat/no)"
```
→ AI extracts team's self-assessment

## ✅ Behavioral Counting (Higher Validity)

```python
"Count how many tasks each team member owns in the Tasks table.
 Return as JSON: {member_name: task_count}"
```
→ AI counts objective data

## Recommendation

**Prefer behavioral measures over extracting self-assessments**

---

# Slide 18: My Reflections

## What This Analysis Revealed

1. **主观评分任务比预期更有效**
   - 结果有meaningful variance (不是全打50分)
   - 分数与团队实际情况一致

2. **真正的瓶颈是数据结构**
   - 不是"AI能不能判断"
   - 而是"数据里有没有这个信息"

3. **小改动能解锁大能力**
   - 加几个字段就能实现跨时间追踪
   - 模板改进比换工具更重要

4. **Self-Report ≠ Ground Truth** (NEW)
   - GABRIEL提取的是team的narrative
   - 需要用behavioral counting替代self-assessment extraction

---

# Slide 19: Summary Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│           GABRIEL MR Analysis: Key Metrics                      │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   Avg ToV Score │ Avg Experiment  │    Avg Alignment            │
│                 │                 │                             │
│      78.1       │      74.3       │       82.7                  │
│     /100        │     /100        │      /100                   │
├─────────────────┴─────────────────┴─────────────────────────────┤
│                                                                 │
│   能直接使用: ~65% of Section 4 measures                        │
│   需要模板改进: ~35% of Section 4 measures                      │
│                                                                 │
│   API成本: $0.31  |  运行时间: 2分钟  |  7个团队 × 47个指标     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

# Slide 20: Next Steps

## Immediate
- [ ] 修改MR模板 (加Change Log, 问题首报日期等)
- [ ] 与1-2个团队pilot新模板

## Short-term
- [ ] 设置历史版本获取机制
- [ ] 建立自动化分析pipeline

## Long-term
- [ ] 实现Individual ToV提交流程
- [ ] 探索视频签到获取情感数据

---

# Slide 21: Questions?

## Deliverables

```
gdoc-code/
├── gabriel_mr_analysis.py    # 主分析脚本 (可复用)
├── generate_charts.py        # 图表生成
└── plan.md                   # 方法论文档

gdoc-output/
├── charts/                   # 可视化图表
├── mr_analysis_results.csv   # 完整数据 (47列 × 7团队)
├── mr_analysis_report.md     # 自动生成的报告
└── gaps_and_recommendations.md  # 详细gap分析
```

---

# Appendix A: Metric Calculation Details

## Composite Metrics Formula

```
tov_overall_score = mean(tov_presence, tov_clarity, tov_coherence, tov_experiment_link)

experimentation_score = mean(hypothesis_explicitness, experiment_rigor,
                             hypothesis_test_chain, learning_evidence, customer_voice)

alignment_score = mean(task_tov_coherence, strategy_consistency)
```

---

# Appendix A.1: Theory of Value Metrics (Section 4.1)

## `tov_overall_score` 的组成部分

| Attribute | Prompt | Scale |
|-----------|--------|-------|
| `tov_presence` | "How clearly is a Theory of Value (business model, value proposition, cause-effect-value chain) articulated in this report?" | 100=very clear, 0=not mentioned |
| `tov_clarity` | "How clear and understandable is the description of how the venture creates value for customers?" | 100=crystal clear, 0=confusing |
| `tov_coherence` | "How coherent is the logical chain from customer problem → solution → value creation?" | 100=highly coherent, 0=disconnected |
| `tov_experiment_link` | "How well does the report connect experiments/tests to validating or refining the theory of value?" | 100=strong links, 0=no connection |

**Note**: `tov_frankenstein` 单独报告，不计入overall score (因为它是反向指标)

---

# Appendix A.2: Team Dynamics Metrics (Section 4.2-4.4)

## Task Allocation (4.2)

| Attribute | Prompt | Scale |
|-----------|--------|-------|
| `task_concentration` | "How concentrated is the work on just one or two people vs. distributed across all team members?" | 100=one person does everything, 0=perfectly distributed |
| `role_specialization` | "How much do team members appear to specialize in certain types of tasks?" | 100=highly specialized, 0=everyone does everything |

## Facilitation & Leadership (4.3)

| Attribute | Prompt | Scale |
|-----------|--------|-------|
| `facilitator_evidence` | "How much evidence is there of a de facto coordinator/facilitator who sets priorities, assigns tasks?" | 100=very clear leader, 0=no coordination |
| `coordination_centralization` | "How centralized is the coordination?" | 100=one person controls all, 0=distributed |
| `task_tov_coherence` | "How well do the tasks and priorities align with the stated theory of value?" | 100=perfect alignment, 0=disconnected |

## Decision Making (4.4)

| Attribute | Prompt | Scale |
|-----------|--------|-------|
| `decision_selectivity` | "How selective vs. inclusive are the team's decisions?" | 100=very selective, 0=accommodating many |
| `strategy_consistency` | "How consistent are the actions and decisions with the stated strategy/theory of value?" | 100=perfect consistency, 0=significant drift |

---

# Appendix A.3: Experimentation Metrics (Section 4.5)

## `experimentation_score` 的组成部分

| Attribute | Prompt | Scale |
|-----------|--------|-------|
| `hypothesis_explicitness` | "How explicit are the hypotheses the team is testing?" | 100=clear testable hypotheses, 0=none mentioned |
| `experiment_rigor` | "How rigorous is the experimentation methodology (interviews, surveys, A/B tests, prototypes)?" | 100=systematic, 0=ad hoc |
| `hypothesis_test_chain` | "How well does the report show a complete hypothesis → test → result → interpretation chain?" | 100=complete chain, 0=no connection |
| `learning_evidence` | "How much evidence of learning from experiments is shown (insights, pivots based on data)?" | 100=strong learning, 0=none evident |
| `customer_voice` | "How much is the customer voice present through interviews, surveys, or direct quotes?" | 100=rich insights, 0=no customer perspective |

---

# Appendix A.4: Problem Classification (Section 4.6)

## Problem Type Percentages

| Attribute | Prompt |
|-----------|--------|
| `technical_problems` | "What percentage of the problems listed are technical issues (coding, website, API, platform limitations)?" |
| `market_problems` | "What percentage of the problems are market/customer-related (finding customers, market fit, competition)?" |
| `team_problems` | "What percentage of the problems are team process issues (coordination, communication, time management, conflict)?" |
| `financial_problems` | "What percentage of the problems are financial (funding, costs, pricing)?" |

## Other Problem Metrics

| Attribute | Prompt | Scale |
|-----------|--------|-------|
| `conflict_evidence` | "How much evidence is there of internal disagreements or conflicts about direction?" | 100=explicit conflicts, 0=none mentioned |
| `problem_severity` | "Overall, how severe are the problems described?" | 100=critical blockers, 0=minor issues |

---

# Appendix A.5: Engagement Metrics (Section 4.7)

## Extraction Attributes

| Attribute | Prompt | Type |
|-----------|--------|------|
| `most_mentioned_member` | "Which team member name appears most frequently in the Progress and Tasks sections?" | String |
| `least_mentioned_member` | "Which team member name appears least frequently or is absent from Progress section?" | String |
| `cognitive_tasks_count` | "How many tasks involve strategic thinking, planning, research, or decision-making?" | Number |
| `execution_tasks_count` | "How many tasks involve implementation, building, coding, or routine execution work?" | Number |
| `equal_distribution` | "Does the work appear equally distributed among all members?" | yes/somewhat/no |

**⚠️ Validity Warning**: `equal_distribution` 是self-report extraction，validity较低（见Slide 15-17）

---

# Appendix B: Technical Details

## How GABRIEL Works Under the Hood

```python
# Simplified workflow
prompt = f"""
Read this management report:
{content}

Rate on 0-100: How clear is the theory of value?
Return JSON: {{"tov_clarity": <score>}}
"""

response = await openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

score = json.loads(response)["tov_clarity"]  # e.g., 77
```

## Cost Structure

| Component | Cost |
|-----------|------|
| Input tokens (~755K) | $0.19 |
| Output tokens (~30K) | $0.12 |
| **Total** | **$0.31** |

Human equivalent effort: Several days → 2 minutes
