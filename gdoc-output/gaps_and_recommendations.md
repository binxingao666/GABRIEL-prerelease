# GABRIEL Limitations & Future MR Template Recommendations

## Executive Summary

This document analyzes what GABRIEL **cannot currently extract** from Management Reports
and provides actionable recommendations for enhancing MR templates to enable full
research data collection aligned with Elena's TBV research framework.

---

## Part 1: What GABRIEL Cannot Do (And Why)

### 1.1 Longitudinal Change Tracking

| Desired Measure | Why GABRIEL Can't Do It | Impact |
|-----------------|------------------------|--------|
| Revision frequency of ToV | No historical data access | Cannot measure evolution |
| Changes in contribution patterns | Single snapshot | Cannot detect disengagement |
| Persistence of unresolved problems | No cross-report linking | Cannot identify chronic issues |
| Speed of learning cycles | No temporal markers | Cannot measure iteration velocity |
| Stability of facilitation role | Single point data | Cannot track role changes |

**Root Cause**: Current data is a single time-point snapshot per team. GABRIEL processes
what it's given; it cannot infer historical changes from one document.

**Future Solution**:
```
Option A: Google Drive API integration to fetch revision history
Option B: Structured "Change Log" section in each MR
Option C: Weekly diff reports comparing consecutive MRs
```

---

### 1.2 Individual vs. Shared Theory of Value Comparison

| Desired Measure | Why GABRIEL Can't Do It | Impact |
|-----------------|------------------------|--------|
| Degree of convergence among members | No individual submissions | Cannot measure alignment |
| Whose ideas were incorporated | No attribution data | Cannot assess inclusion |
| "Frankenstein" vs. focused ToV | Can rate, but no ground truth | Subjective rating only |

**Root Cause**: The research design calls for individual ToV submissions BEFORE the
team converges on a shared ToV. Current MRs only contain the shared/final ToV.

**Future Solution**: Elena's design already addresses this:
- Each member submits individual ToV before class
- Team then submits shared ToV
- GABRIEL can compare both sets

**Recommended MR Template Addition**:
```markdown
## Individual Theory of Value Contributions (Week N)

| Member | Individual ToV Summary | Incorporated? |
|--------|----------------------|---------------|
| Alice  | Focus on B2B sales   | Yes - partially |
| Bob    | Direct-to-consumer   | No             |
| Carol  | Hybrid approach      | Yes - fully    |

## Shared Theory of Value
[Team's agreed ToV]

## Aggregation Notes
How did the team decide? What was included/excluded and why?
```

---

### 1.3 Diagram/Visual Content Analysis

| Desired Measure | Why GABRIEL Can't Do It | Impact |
|-----------------|------------------------|--------|
| Boxes-and-arrows ToV diagram | Text-only processing | Cannot analyze structure |
| Visual coherence | No image input | Missing rich data |
| Diagram evolution | No image diff | Cannot track visual changes |

**Root Cause**: GABRIEL's current implementation focuses on text. While the underlying
models (GPT-4o) support vision, the pipeline doesn't process embedded images.

**Future Solutions**:

1. **Short-term**: Require text descriptions of diagrams
```markdown
## Theory of Value Diagram (Text Description)
- Box 1: Customer (UMD Students)
- Arrow: "Needs" → Box 2: Problem (No local marketplace)
- Arrow: "Solved by" → Box 3: Solution (Agora platform)
- Arrow: "Creates" → Box 4: Value (Time savings, trust)
```

2. **Long-term**: Extend GABRIEL to support `modality="image"`
```python
# Future capability
await gabriel.extract(
    df=df,
    column_name="diagram_image_path",
    modality="image",
    attributes={
        "num_boxes": "How many distinct boxes/entities?",
        "num_arrows": "How many connections?",
        "complexity": "Rate diagram complexity 1-10",
    }
)
```

---

### 1.4 Video Log Analysis

| Desired Measure | Why GABRIEL Can't Do It | Impact |
|-----------------|------------------------|--------|
| Affect (enthusiasm, frustration) | No video/audio input | Missing emotional data |
| Procedural justice perception | No spoken word analysis | Cannot assess fairness |
| Non-verbal dynamics | Text-only | Missing rich signals |

**Root Cause**: Elena's design includes video logs at key points. GABRIEL would need
audio transcription + sentiment analysis pipeline.

**Future Solution**:
```python
# Proposed pipeline
1. Video → Audio extraction (ffmpeg)
2. Audio → Transcription (Whisper API)
3. Transcription → GABRIEL analysis

# Or use GABRIEL's audio modality (if available)
await gabriel.rate(
    df=df,
    column_name="video_transcript",
    attributes={
        "enthusiasm_level": "Rate team enthusiasm 0-100",
        "frustration_evidence": "Rate frustration indicators 0-100",
        "fairness_perception": "Rate expressed fairness of process 0-100",
    }
)
```

---

### 1.5 Cross-Team Comparison with Experimental Design

| Desired Measure | Why GABRIEL Can't Do It | Impact |
|-----------------|------------------------|--------|
| Facilitator treatment effects | No experimental metadata | Cannot isolate effects |
| Section/instructor effects | No section identifiers | Cannot control for confounds |
| Random vs. chosen facilitator | No assignment data | Cannot test hypothesis |

**Root Cause**: GABRIEL analyzes content; experimental design metadata must be
provided externally.

**Future Solution**: Include experimental metadata in data pipeline
```python
# Enhanced DataFrame
df = pd.DataFrame({
    "team_id": [...],
    "content": [...],
    "section": ["A", "B", "A", ...],  # Instructor section
    "facilitator_assigned": ["random", "self-selected", ...],
    "facilitator_gender": ["M", "F", ...],
    "facilitator_experience": [1, 3, 2, ...],
})

# Then GABRIEL can be used within experimental analysis
treatment_df = df[df["facilitator_assigned"] == "random"]
control_df = df[df["facilitator_assigned"] == "self-selected"]
```

---

## Part 2: Recommended MR Template Enhancements

### 2.1 Theory of Value Section (Enhanced)

```markdown
## Theory of Value

### Current Shared ToV (Diagram + Text)
[Insert diagram here]

**Text Description:**
- Customer: [Who]
- Problem: [What pain point]
- Solution: [Our offering]
- Value Created: [Why it matters]
- Revenue Model: [How we capture value]

### ToV Change Log (Since Last Report)
| Change | Reason | Based on Experiment? |
|--------|--------|---------------------|
| Added B2B segment | Customer interviews | Yes - Interview #12 |
| Removed feature X | Low demand signal | Yes - Survey results |

### Individual ToV Contributions (Pre-Meeting)
| Member | Key Insight/Proposal | Status |
|--------|---------------------|--------|
| Alice  | Partner with vendors | Incorporated |
| Bob    | Focus on Gen Z | Deferred |
```

---

### 2.2 Experimentation Section (Enhanced)

```markdown
## Experimentation & Learning

### Active Hypotheses
| ID | Hypothesis | Test Method | Status |
|----|-----------|-------------|--------|
| H1 | Students prefer local over Amazon | Survey | Validated |
| H2 | Vendors will pay 5% commission | Interviews | Testing |

### Experiment Results This Week
| Hypothesis | Test | Result | Learning | ToV Impact |
|-----------|------|--------|----------|------------|
| H1 | Survey N=50 | 72% prefer local | Strong signal | Added "local" to value prop |

### Learning Velocity
- Hypotheses tested this week: 2
- Hypotheses validated: 1
- Pivots triggered: 0
```

---

### 2.3 Team Dynamics Section (New)

```markdown
## Team Dynamics

### Facilitation This Week
- Facilitator: [Name]
- Facilitator role: [Assigned randomly / Self-selected / Rotated]
- Key coordination activities: [List]

### Decision Log
| Decision | Options Considered | Final Choice | Dissent? |
|----------|-------------------|--------------|----------|
| Logo design | 3 options | Option B | Bob preferred A |
| Pricing | $5 vs $7 | $5 | Unanimous |

### Member Contribution Summary
| Member | Hours | Cognitive Tasks | Execution Tasks |
|--------|-------|-----------------|-----------------|
| Alice  | 8     | Strategy (2)    | Code (3)        |
| Bob    | 6     | Research (1)    | Design (2)      |

### Process Reflection
- What worked well this week?
- What didn't work?
- Any unresolved disagreements?
```

---

### 2.4 Problems Section (Enhanced)

```markdown
## Problems

### New Problems This Week
| ID | Problem | Type | Owner | Severity | First Reported |
|----|---------|------|-------|----------|----------------|
| P1 | API limit | Technical | Bob | High | Week 8 |
| P2 | Low response | Market | Alice | Medium | Week 9 |

### Recurring Problems
| ID | Problem | Weeks Active | Resolution Progress |
|----|---------|--------------|---------------------|
| P1 | API limit | 3 | Exploring alternatives |

### Conflict/Disagreement Log
| Topic | Parties | Status | Resolution Path |
|-------|---------|--------|-----------------|
| Pricing | Alice vs Bob | Resolved | Data-driven decision |
```

---

## Part 3: Research Question Mapping

### What We CAN Measure Now (With Current MRs)

| Research Component | GABRIEL Method | Confidence |
|-------------------|----------------|------------|
| ToV articulation quality | `rate()` | High |
| Task distribution patterns | `extract()` + analysis | High |
| Experimentation rigor | `rate()` | Medium |
| Problem types | `classify()` | High |
| Member visibility | `extract()` | Medium |

### What We CANNOT Measure Now (Need Template Changes)

| Research Component | Missing Data | Template Solution |
|-------------------|--------------|-------------------|
| ToV convergence | Individual submissions | Section 2.1 |
| ToV revision history | Change log | Section 2.1 |
| Facilitator effects | Role metadata | Section 2.3 |
| Conflict dynamics | Explicit logging | Section 2.4 |
| Learning velocity | Structured tracking | Section 2.2 |

### What Requires External Data Sources

| Research Component | External Source Needed |
|-------------------|----------------------|
| Video log affect | Whisper transcription |
| Historical diffs | Google Drive API |
| Individual surveys | Separate collection |
| Section metadata | Course roster |

---

## Part 4: Implementation Priority

### Priority 1: Quick Wins (Can implement immediately)

1. Add "ToV Change Log" section to MR template
2. Add "Hypothesis Tracking" table
3. Add "Facilitator This Week" field
4. Add "First Reported" date to Problems

### Priority 2: Medium Effort (Next semester)

1. Individual ToV submissions before team meeting
2. Decision Log with dissent tracking
3. Member contribution hours/types

### Priority 3: Infrastructure (Requires development)

1. Google Drive API for version history
2. Video log transcription pipeline
3. GABRIEL image/audio modality support

---

## Conclusion

GABRIEL is highly capable for **single-document, text-based analysis** of structured
MR content. The key gaps are:

1. **Temporal**: No longitudinal tracking without historical data
2. **Multi-source**: No individual vs. shared comparison without separate inputs
3. **Multimodal**: No diagram/video analysis without pipeline extensions

The recommended template enhancements would unlock ~80% of Elena's research measures
using GABRIEL's existing capabilities, while the remaining ~20% require infrastructure
investment.

---

*Document prepared for Elena's research team meeting*
*Contact: PhD Student Team*
