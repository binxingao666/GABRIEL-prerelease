# GABRIEL MR Analysis Plan

## Overview

This plan addresses Elena's research question: **How do entrepreneurial teams construct, revise, and converge on shared theories of value over time?**

We will analyze 7 team management reports using GABRIEL to extract, rate, and classify relevant measures from Section 4.

---

## Data Sources

| Team | File | Venture Idea |
|------|------|--------------|
| AGORA (AGO) | 2025-11-21 MR AGO.md | Student marketplace platform |
| Baked Gainz (BGAI) | Dec 1 2025 BGAI Draft.md | Protein-infused baked goods |
| The Dream Team (TDT) | Dec 12 2025 MR TDT Draft.md | Stadium seat ordering (Seatr) |
| NGM Team | Dec 5 2025 MR Draft.md | Myanmar education nonprofit |
| ResponsiPay (RSP) | Dec 5 2025 MR RSP Draft.md | Responsible payment platform |
| Team 6 (T06) | Dec 5 2025 MR T06 Draft.md | Friendly scheduling app |
| Arloe | MR Arloe Dec 5 2025.md | Campus clothing marketplace |

---

## Section 4 Measures Analysis

### 4.1 Theory of Value (ToV)

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Presence of articulated ToV | YES | `extract()` - detect if ToV section exists |
| Clarity of ToV | YES | `rate()` - score 0-100 on clarity |
| Coherence of cause-impact-value chain | YES | `rate()` - score coherence |
| Degree of convergence | PARTIAL | Need individual submissions (future) |
| Revision frequency | NO (now) | Need historical versions (Google Drive API) |
| Link between experiments and revisions | YES | `extract()` + `rate()` |

### 4.2 Task Allocation

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Who assigned to tasks | YES | `extract()` - parse task tables |
| Concentration vs dispersion (Gini) | YES | `extract()` + Python post-processing |
| Role specialization | YES | `extract()` - track owner patterns |
| Team composition changes | PARTIAL | Need historical data |

### 4.3 Facilitation & Leadership

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Evidence of de facto facilitator | YES | `extract()` + `rate()` |
| Centralization of coordination | YES | `rate()` - score centralization |
| Stability of facilitation | NO (now) | Need historical data |
| Coherence with ToV | YES | `rate()` - alignment score |

### 4.4 Decision Making

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Number of critical decisions | YES | `extract()` - count decisions |
| Selectivity vs inclusion | YES | `rate()` - Frankenstein vs focused |
| Consistency with ToV | YES | `rate()` - drift score |

### 4.5 Experimentation & Learning

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Number of hypotheses | YES | `extract()` - count hypotheses |
| Number/type of experiments | YES | `extract()` + `classify()` |
| Quality of hypothesis-test-result chain | YES | `rate()` - scientific rigor score |
| Speed of learning cycle | PARTIAL | Need historical data |

### 4.6 Problems & Conflict

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Frequency of problems | YES | `extract()` - count problems |
| Type of problems | YES | `classify()` - technical/market/team |
| Evidence of disagreements | YES | `extract()` + `rate()` |
| Persistence of unresolved issues | NO (now) | Need historical data |

### 4.7 Engagement & Involvement

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Visibility of contributions | YES | `extract()` - name mention frequency |
| Changes in contribution patterns | NO (now) | Need historical data |
| Cognitive vs execution balance | YES | `classify()` - task type categorization |

### 4.8 Venture Trajectory

| Measure | GABRIEL Feasibility | Method |
|---------|---------------------|--------|
| Number of pivots | PARTIAL | Text mentions, but need history |
| Performance measures | YES | `extract()` - PES, sales, metrics |

---

## Implementation Plan

### Phase 1: GABRIEL Scripts (gdoc-code/)

1. **01_basic_extraction.py** - Extract structured data from all MRs
   - Team name, members, venture idea
   - Task counts, completion rates
   - Problem counts

2. **02_theory_of_value_analysis.py** - ToV-specific analysis
   - Presence detection
   - Clarity and coherence rating
   - Experiment-ToV linkage

3. **03_task_allocation_analysis.py** - Task distribution analysis
   - Owner extraction from tables
   - Concentration metrics (Gini coefficient)
   - Role specialization patterns

4. **04_experimentation_quality.py** - Experimentation analysis
   - Hypothesis extraction
   - Experiment type classification
   - Hypothesis-test-result chain quality

5. **05_problems_classification.py** - Problem analysis
   - Problem extraction and counting
   - Type classification (technical/market/team)
   - Conflict detection

6. **06_engagement_analysis.py** - Member engagement
   - Name mention frequency
   - Task type classification (cognitive vs execution)

### Phase 2: Gap Analysis (gdoc-output/)

**gaps_and_recommendations.md** - Detailed analysis of:
- What GABRIEL cannot do and why
- Required MR template changes
- Future data collection needs

### Phase 3: Innovation & Gamification (gdoc-output/)

**innovation_ideas.md** - Creative proposals:
- Gamification elements for MR engagement
- Novel tools beyond traditional MR

### Phase 4: Complete Report (gdoc-report/)

**GABRIEL_MR_Analysis_Report.md** - Meeting-ready document:
- Executive summary
- Findings with visualizations
- Recommendations
- Research question implications

---

## Color Palette for Visualizations

- Primary: #D87756 (warm coral)
- Secondary: #689BCC (calm blue)
- Accent: #C46686 (rose)

---

## Technical Notes

- API: Azure OpenAI (gpt-5.2)
- Model settings from notebooks/pdf_analysis_tutorial.ipynb
- Results saved with checkpointing for reproducibility

---

## Research Question Mapping

| Elena's RQ Component | GABRIEL Analysis |
|----------------------|------------------|
| Construct ToV | 4.1 Presence + Clarity |
| Revise ToV | Needs historical data |
| Converge on shared ToV | Needs individual submissions |
| Individual experience | 4.7 Engagement metrics |
| Team functioning | 4.2-4.6 Various measures |
| Venture performance | 4.8 + PES scores |

---

## Timeline

| Task | Status |
|------|--------|
| Plan approval | Pending |
| Phase 1: Scripts | Ready to start |
| Phase 2: Gap Analysis | Ready to start |
| Phase 3: Innovation | After Phases 1-2 |
| Phase 4: Report | Final deliverable |
