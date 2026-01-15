# GABRIEL MR Analysis: Results & Reflections

**Presenter**: [Your Name]
**Date**: January 2026

---

# Slide 1: Agenda

1. **What is GABRIEL?** — A brief introduction to the principles
2. **What I Did** — Analysis pipeline and execution
3. **Key Results** — Real data from 7 teams
4. **Capability Assessment** — What works, what needs improvement
5. **MR Template Improvements** — Specific template recommendations (4 sub-slides)
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

**GABRIEL = A standardized tool that transforms "humans reading and scoring documents" into "AI reading and scoring documents"**

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

**Key Point**: AI evaluates based on clearly defined criteria, not random scoring

---

# Slide 4: Why Trust LLM Scores?

## Validation Evidence from This Analysis

| Evidence Type | Manifestation in This Analysis |
|---------------|-------------------------------|
| **Meaningful Variance** | Same metric: NGM scored 86, Baked Gainz scored 50 |
| **Contextual Correctness** | Dream Team has high technical problems (62%) — they're building stadium API |
| **Internal Consistency** | Teams with high ToV quality also have high strategy consistency (r=0.7) |
| **Face Validity** | Score distributions match our understanding of these teams |

---

# Slide 5: GABRIEL's Core Functions

| Function | Purpose | Analogy |
|----------|---------|---------|
| `extract()` | Extract structured information from text | Form filling |
| `rate()` | Score text attributes (0-100) | Scorecard |
| `classify()` | Categorize text | Labeling |
| `compare()` | Compare differences between two texts | Spot the difference |
| `discover()` | Find patterns/themes in text | Topic mining |
| `whatever()` | Custom prompt analysis | Universal interface |

---

# Slide 6: What I Built

```
┌─────────────────────────────────────────────────────────────────┐
│                  GABRIEL MR Analysis Pipeline                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   7 Team MRs  ──→  gabriel_mr_analysis.py  ──→  Results        │
│   (13,000+        │                         │                   │
│    words)         │  • extract() ×11 metrics │  • CSV (47 cols) │
│                   │  • rate() ×22 metrics    │  • Markdown report│
│                   │  • classify() ×6 metrics │  • Visualizations │
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

## This is a "subjective assessment" task — but results are meaningful

```
  NGM Team      ████████████████████████████████░░  86/100 ⭐
  Dream Team    █████████████████████░░░░░░░░░░░░░  68/100
  Team 6        █████████████████████░░░░░░░░░░░░░  68/100
  Team Arloe    ████████████████████░░░░░░░░░░░░░░  65/100
  Team AGORA    ███████████████████░░░░░░░░░░░░░░░  62/100
  ResponsiPay   ███████████████████░░░░░░░░░░░░░░░  62/100
  Baked Gainz   ███████████████░░░░░░░░░░░░░░░░░░░  50/100
```

**Why did NGM score highest?**
They conducted systematic curriculum testing with Myanmar students. Their MR contains complete hypothesis → test → result → interpretation chains.

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

**Classification results align with team contexts**:

- Dream Team is doing stadium tech integration → high technical problems
- Baked Gainz is making cookies → low technical problems, more team coordination issues

---

# Slide 10: Task Concentration — Who Does the Work?

```
ResponsiPay   ████████████████████████████░░░░░  72%
              → Highly concentrated on one person

Team Arloe    ████████████████░░░░░░░░░░░░░░░░░  40%
NGM Team      ██████████████░░░░░░░░░░░░░░░░░░░  36%
Dream Team    ██████████████░░░░░░░░░░░░░░░░░░░  35%
Team 6        ██████████░░░░░░░░░░░░░░░░░░░░░░░  26%
Baked Gainz   ██████████░░░░░░░░░░░░░░░░░░░░░░░  25%
Team AGORA    ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░  15%
              → Most evenly distributed

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

**Finding**: ToV quality is significantly correlated with strategy consistency (r ≈ 0.7)

---

# Slide 12: Capability Assessment — What Works Well

## ✅ Tasks where GABRIEL performs well

| Task Type | Examples | Why It Works |
|-----------|----------|--------------|
| **Structured Extraction** | Team members, task counts, problem counts | Information explicitly exists in text |
| **Quality Scoring** | ToV clarity, experimentation raigor | Clear scoring criteria, rich AI training data |
| **Classification** | Problem types, task types | Well-defined categories |
| **Single Document Analysis** | Any single MR content analysis | Complete context available |

---

# Slide 13: Capability Assessment — What Needs Work

## ⚠️ Tasks not possible with current data structure

| Task | Why Not Possible | Solution |
|------|------------------|----------|
| **Cross-time change tracking** | Only single document, no historical versions | Google Drive API for version history |
| **Problem persistence** | Can't tell if problem persists across weeks | Add "First Reported Date" field to MR |
| **Facilitator role stability** | Can't compare facilitators across weeks | Add "This Week's Facilitator" field |
| **Individual vs Shared ToV comparison** | MR only has shared ToV | Have members submit individual ToV before meeting |
| **Contribution pattern changes** | Single snapshot can't show trends | Need multiple consecutive MRs |

## Key Insight

**The limitation is not AI capability, but data collection methods**

---

# Slide 14: MR Template Improvements — Overview

## Why Change the Template?

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

## Current Problem
MR only has current ToV snapshot; cannot track how ToV evolved

## New Fields

```markdown
## Theory of Value Change Log (NEW)
| What Changed | Why | Based on Experiment? | Week |
|--------------|-----|---------------------|------|
| Added B2B segment | Interview #12 showed demand | Yes | 7 |
| Dropped college market | Survey: low WTP | Yes | 9 |
| Pivoted to subscription | Competitor analysis | No | 11 |
```

| What Changed            | Why                         | Based on Experiment? | Week |
| ----------------------- | --------------------------- | -------------------- | ---- |
| Added B2B segment       | Interview #12 showed demand | Yes                  | 7    |
| Dropped college market  | Survey: low WTP             | Yes                  | 9    |
| Pivoted to subscription | Competitor analysis         | No                   | 11   |

## Research Value

- Track ToV revision frequency and reasons
- Identify experiment-driven vs. intuition-driven changes
- Quantify team's learning velocity

---

# Slide 14.2: Template Change #2 — Problem Tracking Enhancement

## Current Problem
Only know "there's a problem"; don't know how long it persists

## Enhanced Fields

```markdown
## Problems (Enhanced)
| Problem | Type | Owner | First Reported | Weeks Active | Status |
|---------|------|-------|----------------|--------------|--------|
| API rate limits | Technical | RR | Week 6 | 3 | Open |
| Customer churn | Market | CF | Week 8 | 1 | Resolved |
```

| Problem         | Type      | Owner | First Reported | Weeks Active | Status   |
| --------------- | --------- | ----- | -------------- | ------------ | -------- |
| API rate limits | Technical | RR    | Week 6         | 3            | Open     |
| Customer churn  | Market    | CF    | Week 8         | 1            | Resolved |

## Research Value

- Measure problem persistence (key Section 4.6 metric)
- Identify chronic blockers vs. quick fixes
- Correlate problem duration with team performance

---

# Slide 14.3: Template Change #3 — Facilitator & Convergence

## New: Facilitator Tracking

```markdown
## This Week's Facilitator
- **Name**: ___________
- **Selection**: [ ] Assigned [ ] Rotated [ ] Self-selected
- **Key Decisions Made**: ___________
```

## New: Individual ToV Contributions (Pre-Meeting)

```markdown
## Individual ToV Proposals
| Member | My Proposed Focus | Incorporated? |
|--------|-------------------|---------------|
| Alice  | B2C local market | Yes |
| Bob    | B2B partnerships | Deferred |
| Carol  | Freemium model | No - voted against |
```

| Member | My Proposed Focus | Incorporated?      |
| ------ | ----------------- | ------------------ |
| Alice  | B2C local market  | Yes                |
| Bob    | B2B partnerships  | Deferred           |
| Carol  | Freemium model    | No - voted against |

## Research Value

- Track facilitation role stability
- Measure individual → shared ToV convergence (core TBV question)
- Quantify "whose ideas get incorporated"

---

# Slide 14.4: Template Change #4 — Hypothesis Tracker

## New: Experiment-ToV Linkage

```markdown
## Hypothesis Tracker
| ID | Hypothesis | Status | Evidence | Linked ToV Element |
|----|-----------|--------|----------|-------------------|
| H1 | Students pay $5 | Validated | Survey N=50 | Revenue model |
| H2 | Parents are buyers | Testing | 3/10 interviews | Customer segment |
| H3 | Weekly usage | Invalidated | Analytics | Value prop |
```

## New: How Experiments Changed ToV

```markdown
## Experiment → ToV Changes
| Experiment | Finding | ToV Change Made |
|------------|---------|-----------------|
| Survey #1 | Low WTP in college | Dropped segment |
| Interview #5 | Parents pay | Added segment |
```

## Research Value
- Explicitly link experiments to ToV evolution
- Measure hypothesis-test-result chain quality
- Verify whether teams are truly "evidence-based"

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

1. **Subjective scoring tasks work better than expected**
   - Results have meaningful variance (not all scores at 50)
   - Scores align with team realities

2. **The real bottleneck is data structure**
   - Not "can AI make judgments"
   - But "is the information in the data"

3. **Small changes unlock big capabilities**
   - Adding a few fields enables cross-time tracking
   - Template improvements matter more than tool changes

4. **Self-Report ≠ Ground Truth** (NEW)
   - GABRIEL extracts team's narrative
   - Need to use behavioral counting instead of self-assessment extraction

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
│   Works directly: ~65% of Section 4 measures                    │
│   Needs template changes: ~35% of Section 4 measures            │
│                                                                 │
│   API cost: $0.31  |  Runtime: 2 min  |  7 teams × 47 metrics   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

# Slide 20: Next Steps

## Immediate
- [ ] Modify MR template (add Change Log, problem first-reported date, etc.)
- [ ] Pilot new template with 1-2 teams

## Short-term
- [ ] Set up historical version retrieval mechanism
- [ ] Build automated analysis pipeline

## Long-term
- [ ] Implement Individual ToV submission workflow
- [ ] Explore video check-ins for affect data

---

# Slide 21: Questions?

## Deliverables

```
gdoc-code/
├── gabriel_mr_analysis.py    # Main analysis script (reusable)
├── generate_charts.py        # Chart generation
└── plan.md                   # Methodology document

gdoc-output/
├── charts/                   # Visualization charts
├── mr_analysis_results.csv   # Complete data (47 cols × 7 teams)
├── mr_analysis_report.md     # Auto-generated report
└── gaps_and_recommendations.md  # Detailed gap analysis
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

## Components of `tov_overall_score`

| Attribute | Prompt | Scale |
|-----------|--------|-------|
| `tov_presence` | "How clearly is a Theory of Value (business model, value proposition, cause-effect-value chain) articulated in this report?" | 100=very clear, 0=not mentioned |
| `tov_clarity` | "How clear and understandable is the description of how the venture creates value for customers?" | 100=crystal clear, 0=confusing |
| `tov_coherence` | "How coherent is the logical chain from customer problem → solution → value creation?" | 100=highly coherent, 0=disconnected |
| `tov_experiment_link` | "How well does the report connect experiments/tests to validating or refining the theory of value?" | 100=strong links, 0=no connection |

**Note**: `tov_frankenstein` is reported separately, not included in overall score (it's an inverse metric)

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

## Components of `experimentation_score`

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

**⚠️ Validity Warning**: `equal_distribution` is a self-report extraction with lower validity (see Slides 15-17)

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
