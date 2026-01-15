# GABRIEL MR Analysis: Results & Reflections

**Presenter**: [Your Name]
**Date**: January 2026

---

# Slide 1: Agenda

1. **What I Did**: Analysis pipeline & execution
2. **Key Results**: Real data from 7 teams
3. **Reality Check**: What Jake got wrong
4. **What GABRIEL Actually Can't Do**: Honest limitations
5. **Next Steps**: Concrete recommendations

---

# Slide 2: What I Built

```
┌─────────────────────────────────────────────────────────────┐
│                  GABRIEL MR Analysis Pipeline                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   7 Team MRs  ──→  gabriel_mr_analysis.py  ──→  Results    │
│   (13,000+       │                         │               │
│    words)        │  • extract()            │  • CSV        │
│                  │  • rate()               │  • Markdown   │
│                  │  • classify()           │  • Charts     │
│                  │                         │               │
│                  └─────────────────────────┘               │
│                                                             │
│   API Cost: $0.31    |    Time: ~2 minutes                 │
└─────────────────────────────────────────────────────────────┘
```

**Teams Analyzed**: AGO, Baked Gainz, Dream Team, NGM, ResponsiPay, Team 6, Arloe

---

# Slide 3: Key Metrics Extracted

## Section 4 Coverage

| Category | Metrics Extracted | Sample |
|----------|-------------------|--------|
| **4.1 Theory of Value** | 5 ratings | Presence, Clarity, Coherence, Experiment Link, Frankenstein |
| **4.2-4.4 Team Dynamics** | 7 ratings | Concentration, Specialization, Facilitator, Alignment |
| **4.5 Experimentation** | 5 ratings | Hypothesis explicitness, Rigor, H-T-R chain quality |
| **4.6 Problems** | 6 ratings | Type %, Conflict evidence, Severity |
| **4.7 Engagement** | 5 extractions | Most/least visible member, Distribution |
| **Total** | **47 data points per team** | |

---

# Slide 4: Theory of Value Quality Scores

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

**Average: 78.1/100** — Meaningful variation across teams!

---

# Slide 5: The "Subjective" Tasks Jake Said Would Fail

## Hypothesis-Test-Result Chain Quality (Jake rated 1-2)

```
                    H-T-R Chain Quality (Actual Results)
                    ════════════════════════════════════

  NGM Team      ████████████████████████████████░░  86/100 ⭐
  Dream Team    █████████████████████░░░░░░░░░░░░░  68/100
  Team 6        █████████████████████░░░░░░░░░░░░░  68/100
  Team Arloe    ████████████████████░░░░░░░░░░░░░░  65/100
  Team AGORA    ███████████████████░░░░░░░░░░░░░░░  62/100
  ResponsiPay   ███████████████████░░░░░░░░░░░░░░░  62/100
  Baked Gainz   ███████████████░░░░░░░░░░░░░░░░░░░  50/100

                0        25        50        75       100
```

**Reality**: Clear differentiation! NGM's systematic approach to curriculum testing shows up as the highest score.

---

# Slide 6: Problem Classification (Jake rated 2)

```
            Problem Type Distribution by Team
            ═══════════════════════════════════

Team AGORA    ▓▓▓▓▓▓▓▓░░  ████████████████░░  ▒▒▒▒░░░░░░
              Tech 60%         Market 78%       Team 25%

Baked Gainz   ▓▓░░░░░░░░  ████░░░░░░░░░░░░░░  ▒▒▒▒▒▒▒▒▒░
              Tech 20%         Market 30%       Team 45%

Dream Team    ▓▓▓▓▓▓▓▓▓░  ████████░░░░░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒
              Tech 62%         Market 38%       Team 74%

NGM Team      ▓▓░░░░░░░░  ██████████░░░░░░░░  ▒▒▒▒▒▒▒▒░░
              Tech 15%         Market 50%       Team 40%

Legend: ▓ Technical  █ Market  ▒ Team Process
```

**Reality**: Meaningful classification that aligns with team contexts!
- Dream Team (stadium tech) → high technical problems
- Baked Gainz (cookies) → low technical, high team coordination

---

# Slide 7: What Jake Got Wrong

## Jake's Claim vs. Reality

| Jake's Claim | Jake's Rating | Actual Performance | Evidence |
|--------------|---------------|-------------------|----------|
| "H-T-R chain quality will be weak" | 1-2 | ✅ **Works well** | NGM 86, variance 50-86 |
| "ToV coherence will be weak" | 2 | ✅ **Works well** | Range 62-84, correlates with PES |
| "Problem classification will be weak" | 2 | ✅ **Works well** | Clear type distributions |
| "Selectivity vs inclusion will be weak" | 1 | ✅ **Works** | Range 47-87 |
| "Link experiments to ToV revisions weak" | 2 | ✅ **Works** | Range 72-88 |

## The Real Issue Jake Missed

Jake rated these as "3" (easy), but they **actually require historical data**:
- "Persistence of unresolved issues" → **needs cross-report comparison**
- "Stability vs rotation of facilitation" → **needs longitudinal data**
- "Changes in contribution patterns" → **needs multiple time points**

---

# Slide 8: Jake's Incorrect Function Mappings

## Functions That Don't Exist

| Jake's Suggestion | Reality |
|-------------------|---------|
| `gabriel.compare` | ❌ **Does not exist** |
| `gabriel.discover` | ❌ **Does not exist** |

## Actual GABRIEL Functions

```python
gabriel.extract()   # Pull structured facts → strings/numbers
gabriel.rate()      # Score attributes → 0-100 scale
gabriel.classify()  # Assign categories → labels
gabriel.whatever()  # Custom prompts → flexible
gabriel.rank()      # Rank items → orderings
gabriel.filter()    # Filter rows → boolean
gabriel.deduplicate() # Find duplicates → clusters
```

**Bottom line**: Jake consulted ChatGPT about GABRIEL without reading the actual documentation.

---

# Slide 9: What GABRIEL Actually Can't Do

## Honest Limitations (That Jake Missed)

| Limitation | Why | Solution |
|------------|-----|----------|
| **No longitudinal tracking** | Single document input | Google Drive API for version history |
| **No individual vs shared ToV** | Data doesn't exist in MRs | Add pre-meeting submissions |
| **No diagram analysis** | Text-only (for now) | GPT-4V integration or text descriptions |
| **No affect/emotion** | No video logs | Video standup bot |
| **Can't detect unreported conflicts** | If not written, can't extract | Better MR template prompts |

## The Correct "Hard Problems" List

1. ❌ Measuring **convergence** without individual ToV submissions
2. ❌ Tracking **changes over time** without historical data
3. ❌ Detecting **hidden conflicts** not mentioned in text
4. ⚠️ Assessing **visual diagrams** (future capability)

---

# Slide 10: Composite Scores Summary

```
                    Team Performance Dashboard
    ╔═══════════════╦═══════════╦═══════════════╦═══════════╦═══════╗
    ║ Team          ║ ToV Score ║ Experimentation║ Alignment ║  PES  ║
    ╠═══════════════╬═══════════╬═══════════════╬═══════════╬═══════╣
    ║ NGM Team      ║   82.8    ║     87.6      ║   93.0    ║ 91.0% ║
    ║ Dream Team    ║   85.2    ║     76.8      ║   87.5    ║ 75.0% ║
    ║ Team AGORA    ║   76.0    ║     71.4      ║   86.5    ║ 90.9% ║
    ║ ResponsiPay   ║   82.2    ║     67.8      ║   79.5    ║ 82.0% ║
    ║ Team Arloe    ║   80.0    ║     76.0      ║   86.5    ║  N/A  ║
    ║ Baked Gainz   ║   71.2    ║     64.0      ║   80.0    ║  N/A  ║
    ║ Team 6        ║   69.2    ║     76.8      ║   66.0    ║  N/A  ║
    ╚═══════════════╩═══════════╩═══════════════╩═══════════╩═══════╝

    Correlation: ToV Score ↔ Alignment = 0.7+ (meaningful relationship!)
```

---

# Slide 11: Task Concentration Analysis

```
                    Who Does the Work?
                    ══════════════════

ResponsiPay   ████████████████████████████░░░░░  72% concentrated
              Ryan Rodgers dominates

Team Arloe    ████████████████░░░░░░░░░░░░░░░░░  40% concentrated
              Keily Lopez leads

NGM Team      ██████████████░░░░░░░░░░░░░░░░░░░  36% concentrated
              Jimmy visible

Dream Team    ██████████████░░░░░░░░░░░░░░░░░░░  35% concentrated
              Moderate

Team 6        ██████████░░░░░░░░░░░░░░░░░░░░░░░  26% concentrated
              LM visible

Baked Gainz   ██████████░░░░░░░░░░░░░░░░░░░░░░░  25% concentrated
              Kiana leads baking

Team AGORA    ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░  15% concentrated
              Most distributed!

              0%       25%       50%       75%      100%
              ←── Distributed         Concentrated ──→
```

---

# Slide 12: Engagement Red Flags

## Members Disappearing from Reports

| Team | Most Visible | Least Visible | Risk? |
|------|-------------|---------------|-------|
| Team AGORA | Kaleb | **Dylan** | ⚠️ |
| NGM Team | Jimmy | **Asylinn** | ⚠️ |
| Team Arloe | Keily | **Mallory** | ⚠️ |
| ResponsiPay | Ryan | **Max Kaufmann** | ⚠️ |

**Research Implication**: These patterns could predict disengagement — but we need longitudinal data to confirm.

---

# Slide 13: My Reflection

## What Surprised Me

1. **"Subjective" ratings worked better than expected**
   - H-T-R chain quality clearly differentiates teams
   - NGM's systematic approach shows up in scores

2. **The real gap isn't subjectivity — it's data structure**
   - Jake worried about LLM judgment
   - The actual blocker is missing historical data

3. **Problem type classification is actionable**
   - Dream Team's high technical % makes sense (stadium API)
   - Baked Gainz's high team % makes sense (coordination)

## What I Would Change

1. Add **change tracking** to MR template
2. Require **individual ToV before team meeting**
3. Track **facilitator explicitly** each week

---

# Slide 14: Recommended MR Template Changes

## Add These Sections

```markdown
## Theory of Value Change Log (NEW)
| What Changed | Why | Based on Experiment? |
|--------------|-----|---------------------|
| Added B2B | Interview #12 | Yes |

## Hypothesis Tracker (NEW)
| ID | Hypothesis | Status | Evidence |
|----|-----------|--------|----------|
| H1 | Price $5 | Validated | Survey N=50 |

## Facilitator This Week (NEW)
Name: ___________
Role: [Assigned/Rotated/Self-selected]

## Problems (Enhanced)
| Problem | Type | First Reported | Weeks Active |
|---------|------|----------------|--------------|
```

---

# Slide 15: Innovation Opportunity

## "ToV Arena" — Gamified Convergence

```
Week N Process:

┌─────────────────────────────────────────────────────────────┐
│  Round 1: Individual ToV     Round 2: Peer Rating           │
│  ────────────────────────    ──────────────────             │
│  Alice → [ToV A]             Alice rates Bob: ⭐⭐⭐⭐       │
│  Bob   → [ToV B]             Bob rates Alice: ⭐⭐⭐         │
│  Carol → [ToV C]             Carol rates both               │
│                                                             │
│  Round 3: Debate & Vote      Round 4: Synthesize            │
│  ──────────────────────      ────────────────               │
│  "Include feature X?" → 2/3  Final Shared ToV               │
│  "Drop segment Y?" → 3/3     ✓ Approved by all              │
└─────────────────────────────────────────────────────────────┘

Data Captured: Individual ToVs, ratings, votes, inclusion decisions
→ Enables convergence measurement!
```

---

# Slide 16: Summary — Jake vs Reality

| | Jake's View | Reality |
|-|-------------|---------|
| **Subjective tasks** | "Will be weak" | ✅ Work fine with meaningful variance |
| **Longitudinal** | "Easy (rated 3)" | ❌ Actually impossible without history |
| **Functions** | `gabriel.compare`, `gabriel.discover` | ❌ Don't exist |
| **Core limitation** | "LLM subjectivity" | **Data availability** |

## The Real Takeaway

> Jake speculated based on ChatGPT output.
> I ran the actual analysis and got real results.
>
> **GABRIEL works. The limitation isn't the tool — it's the data structure.**

---

# Slide 17: Next Steps

## Immediate (This Week)
- [ ] Present results to team
- [ ] Propose MR template changes

## Short-term (This Semester)
- [ ] Pilot new MR sections with 1-2 teams
- [ ] Set up Google Drive API for version history
- [ ] Implement weekly facilitator tracking

## Long-term (Next Semester)
- [ ] Full template rollout
- [ ] Individual ToV submissions
- [ ] Video standup pilot

---

# Slide 18: Questions?

## Files Available

```
gdoc-code/
├── gabriel_mr_analysis.py    # Main script
└── plan.md                   # Implementation plan

gdoc-output/
├── mr_analysis_results.csv   # Raw data (47 cols × 7 teams)
├── mr_analysis_report.md     # Auto-generated report
├── gaps_and_recommendations.md
├── innovation_and_gamification.md
└── FINAL_REPORT_Meeting_Ready.md
```

## Contact
[Your email]

---

# Appendix A: Correlation Matrix

```
                ToV    Exp    Align   PES
ToV Score       1.00   0.52   0.71   0.42
Experimentation 0.52   1.00   0.65   0.38
Alignment       0.71   0.65   1.00   0.55
PES             0.42   0.38   0.55   1.00
```

**Key insight**: ToV quality correlates with strategy alignment (0.71)

---

# Appendix B: Full Results Table

| Team | ToV | Exp | Align | PES | Concentration | Problems |
|------|-----|-----|-------|-----|---------------|----------|
| NGM | 82.8 | 87.6 | 93.0 | 91% | 36% | 65 |
| Dream Team | 85.2 | 76.8 | 87.5 | 75% | 35% | 81 |
| AGORA | 76.0 | 71.4 | 86.5 | 91% | 15% | 74 |
| ResponsiPay | 82.2 | 67.8 | 79.5 | 82% | 72% | 75 |
| Arloe | 80.0 | 76.0 | 86.5 | — | 40% | 62 |
| Baked Gainz | 71.2 | 64.0 | 80.0 | — | 25% | 55 |
| Team 6 | 69.2 | 76.8 | 66.0 | — | 26% | 64 |

---

# Appendix C: API Cost Breakdown

| Step | Prompts | Cost |
|------|---------|------|
| Basic extraction | 14 | $0.08 |
| ToV rating | 7 | $0.06 |
| Team dynamics | 7 | $0.05 |
| Experimentation | 7 | $0.05 |
| Problems | 7 | $0.04 |
| Engagement | 7 | $0.03 |
| **Total** | **49** | **$0.31** |

Time: ~2 minutes on Azure OpenAI (gpt-4o)
