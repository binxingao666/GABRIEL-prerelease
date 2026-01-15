"""
GABRIEL Management Report Analysis
===================================

This script analyzes 7 team management reports using GABRIEL to extract measures
aligned with Elena's research question about theories of value in entrepreneurial teams.

Section 4 Measures Implemented:
- 4.1 Theory of Value (presence, clarity, coherence)
- 4.2 Task Allocation (distribution, concentration)
- 4.3 Facilitation & Leadership (evidence, centralization)
- 4.4 Decision Making (selectivity)
- 4.5 Experimentation (hypotheses, quality)
- 4.6 Problems & Conflict (types, frequency)
- 4.7 Engagement (visibility, task types)
- 4.8 Venture Trajectory (performance metrics)

Output:
- CSV files with extracted/rated data
- Markdown summary report
"""

import os
import sys
import asyncio
import pandas as pd
from pathlib import Path
from collections import Counter
import json
import re

# Add src to path
sys.path.insert(0, os.path.abspath('../src'))

import gabriel

# Azure OpenAI Configuration
os.environ["AZURE_OPENAI_API_KEY"] = "7WORZn9u5O1Ng0wodxWuoPppWWbNkU6NZnH2hLtjckxS82mNL0zrJQQJ99BLACHYHv6XJ3w3AAABACOG8HXc"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://azure-api-pingzhi-eastus2.openai.azure.com/"

# Paths
REPORT_DIR = Path("../gdoc-report")
OUTPUT_DIR = Path("../gdoc-output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Team metadata
TEAMS = {
    "AGO": {
        "file": "2025-11-21 MR AGO.md",
        "name": "Team AGORA",
        "venture": "Agora - Student marketplace platform"
    },
    "BGAI": {
        "file": "Dec 1 2025 BGAI Draft.md",
        "name": "Baked Gainz",
        "venture": "Protein-infused baked goods"
    },
    "TDT": {
        "file": "Dec 12 2025 MR TDT Draft.md",
        "name": "The Dream Team",
        "venture": "Seatr - Stadium seat ordering"
    },
    "NGM": {
        "file": "Dec 5 2025 MR Draft.md",
        "name": "NGM Team",
        "venture": "Next Generation Myanmar education"
    },
    "RSP": {
        "file": "Dec 5 2025 MR RSP Draft.md",
        "name": "ResponsiPay",
        "venture": "Responsible payment platform"
    },
    "T06": {
        "file": "Dec 5 2025 MR T06 Draft.md",
        "name": "Team 6 - Friendly",
        "venture": "Friendly - Scheduling app"
    },
    "Arloe": {
        "file": "MR Arloe Dec 5 2025.md",
        "name": "Team Arloe",
        "venture": "Arloe - Campus clothing marketplace"
    }
}

MODEL = "gpt-4o"  # Azure model deployment name


def load_reports() -> pd.DataFrame:
    """Load all management reports into a DataFrame."""
    data = []
    for team_id, info in TEAMS.items():
        file_path = REPORT_DIR / info["file"]
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            data.append({
                "team_id": team_id,
                "team_name": info["name"],
                "venture": info["venture"],
                "content": content,
                "word_count": len(content.split())
            })
        else:
            print(f"Warning: File not found: {file_path}")

    return pd.DataFrame(data)


async def extract_basic_info(df: pd.DataFrame) -> pd.DataFrame:
    """
    Section 4.1 & 4.8: Extract basic structured information.
    """
    print("\n[1/6] Extracting basic information...")

    result = await gabriel.extract(
        df=df,
        column_name="content",
        attributes={
            "team_members": "List all team member names mentioned, separated by commas",
            "num_members": "How many team members are there? (number only)",
            "report_week": "What week or date is this report for?",
            "precision_score_total": "What is the total Precision Execution Score percentage? (number only, e.g., 90)",
            "num_tasks_completed": "How many tasks have been completed or marked 'Yes' in the Tasks table?",
            "num_tasks_pending": "How many tasks are still pending or in progress?",
            "num_problems_listed": "How many problems are listed in the Problems section?",
            "num_priorities_listed": "How many priorities are listed in the Priorities section?",
            "has_theory_of_value": "Does this report explicitly mention or discuss a 'Theory of Value' or business model? (yes/no)",
            "has_pivot_mentioned": "Does this report mention any pivot, change in direction, or shift in business idea? (yes/no)",
            "has_first_sale": "Does this report mention achieving a first sale or customer? (yes/no)",
        },
        additional_instructions="Extract information precisely. For numbers, return only the numeric value. For yes/no questions, return only 'yes' or 'no'.",
        save_dir=str(OUTPUT_DIR / "extraction" / "basic_info"),
        model=MODEL,
        reset_files=True,
    )

    return result


async def rate_theory_of_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    Section 4.1: Rate Theory of Value clarity and coherence.
    """
    print("\n[2/6] Rating Theory of Value quality...")

    result = await gabriel.rate(
        df=df,
        column_name="content",
        attributes={
            "tov_presence": "How clearly is a Theory of Value (business model, value proposition, cause-effect-value chain) articulated in this report? (100 = very clear and explicit, 0 = not mentioned at all)",
            "tov_clarity": "How clear and understandable is the description of how the venture creates value for customers? (100 = crystal clear, 0 = confusing or absent)",
            "tov_coherence": "How coherent is the logical chain from customer problem → solution → value creation? (100 = highly coherent, 0 = disconnected or illogical)",
            "tov_experiment_link": "How well does the report connect experiments/tests to validating or refining the theory of value? (100 = strong explicit links, 0 = no connection)",
            "tov_frankenstein": "Does the theory of value appear to be a 'Frankenstein' that tries to include too many disconnected ideas, rather than a focused, selective representation? (100 = very fragmented/unfocused, 0 = tightly focused)",
        },
        save_dir=str(OUTPUT_DIR / "ratings" / "theory_of_value"),
        model=MODEL,
        reset_files=True,
    )

    return result


async def rate_team_dynamics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Section 4.2, 4.3, 4.4: Rate task allocation, facilitation, and decision-making.
    """
    print("\n[3/6] Rating team dynamics...")

    result = await gabriel.rate(
        df=df,
        column_name="content",
        attributes={
            # 4.2 Task Allocation
            "task_concentration": "How concentrated is the work on just one or two people vs. distributed across all team members? (100 = one person does everything, 0 = perfectly distributed)",
            "role_specialization": "How much do team members appear to specialize in certain types of tasks (e.g., one person always does tech, another marketing)? (100 = highly specialized roles, 0 = everyone does everything)",

            # 4.3 Facilitation & Leadership
            "facilitator_evidence": "How much evidence is there of a de facto coordinator/facilitator who sets priorities, assigns tasks, or summarizes decisions? (100 = very clear leader, 0 = no coordination visible)",
            "coordination_centralization": "How centralized is the coordination? (100 = one person controls all coordination, 0 = coordination is distributed/rotated)",
            "task_tov_coherence": "How well do the tasks and priorities align with the stated theory of value/business model? (100 = perfect alignment, 0 = tasks seem disconnected from value proposition)",

            # 4.4 Decision Making
            "decision_selectivity": "How selective vs. inclusive are the team's decisions? (100 = very selective, narrowing down options, 0 = trying to accommodate many conflicting ideas)",
            "strategy_consistency": "How consistent are the actions and decisions with the stated strategy/theory of value? (100 = perfect consistency, 0 = significant drift)",
        },
        save_dir=str(OUTPUT_DIR / "ratings" / "team_dynamics"),
        model=MODEL,
        reset_files=True,
    )

    return result


async def rate_experimentation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Section 4.5: Rate experimentation and learning quality.
    """
    print("\n[4/6] Rating experimentation quality...")

    result = await gabriel.rate(
        df=df,
        column_name="content",
        attributes={
            "hypothesis_explicitness": "How explicit are the hypotheses the team is testing? (100 = clear, testable hypotheses stated, 0 = no hypotheses mentioned)",
            "experiment_rigor": "How rigorous is the experimentation methodology (interviews, surveys, A/B tests, prototypes)? (100 = systematic and well-designed, 0 = ad hoc or absent)",
            "hypothesis_test_chain": "How well does the report show a complete hypothesis → test → result → interpretation chain? (100 = complete chain visible, 0 = no connection between elements)",
            "learning_evidence": "How much evidence of learning from experiments is shown (insights, pivots based on data, updated assumptions)? (100 = strong learning visible, 0 = no learning evident)",
            "customer_voice": "How much is the customer voice present through interviews, surveys, or direct quotes? (100 = rich customer insights, 0 = no customer perspective)",
        },
        save_dir=str(OUTPUT_DIR / "ratings" / "experimentation"),
        model=MODEL,
        reset_files=True,
    )

    return result


async def classify_problems(df: pd.DataFrame) -> pd.DataFrame:
    """
    Section 4.6: Classify problems by type.
    """
    print("\n[5/6] Classifying problems...")

    # Extract problems section for classification
    problems_df = df.copy()

    # Extract problems text
    def extract_problems_section(content):
        # Find Problems section
        problems_match = re.search(r'\*\*Problems\*\*.*?(?=\*\*Priorities\*\*|\*\*Plans\*\*|\Z)',
                                   content, re.DOTALL | re.IGNORECASE)
        if problems_match:
            return problems_match.group(0)
        return "No problems section found"

    problems_df["problems_section"] = problems_df["content"].apply(extract_problems_section)

    result = await gabriel.rate(
        df=problems_df,
        column_name="problems_section",
        attributes={
            "technical_problems": "What percentage of the problems listed are technical issues (coding, website, API, platform limitations)? (0-100)",
            "market_problems": "What percentage of the problems are market/customer-related (finding customers, market fit, competition)? (0-100)",
            "team_problems": "What percentage of the problems are team process issues (coordination, communication, time management, conflict)? (0-100)",
            "financial_problems": "What percentage of the problems are financial (funding, costs, pricing)? (0-100)",
            "conflict_evidence": "How much evidence is there of internal disagreements or conflicts about direction? (100 = explicit conflicts, 0 = no conflicts mentioned)",
            "problem_severity": "Overall, how severe are the problems described? (100 = critical blockers, 0 = minor issues)",
        },
        save_dir=str(OUTPUT_DIR / "ratings" / "problems"),
        model=MODEL,
        reset_files=True,
    )

    # Merge back
    for col in ["technical_problems", "market_problems", "team_problems",
                "financial_problems", "conflict_evidence", "problem_severity"]:
        if col in result.columns:
            df[col] = result[col]

    return df


async def analyze_engagement(df: pd.DataFrame) -> pd.DataFrame:
    """
    Section 4.7: Analyze member engagement and visibility.
    """
    print("\n[6/6] Analyzing engagement patterns...")

    result = await gabriel.extract(
        df=df,
        column_name="content",
        attributes={
            "most_mentioned_member": "Which team member name appears most frequently in the Progress and Tasks sections?",
            "least_mentioned_member": "Which team member name appears least frequently or is absent from Progress section?",
            "cognitive_tasks_count": "How many tasks involve strategic thinking, planning, research, or decision-making (cognitive work)?",
            "execution_tasks_count": "How many tasks involve implementation, building, coding, or routine execution work?",
            "equal_distribution": "Does the work appear equally distributed among all members? (yes/somewhat/no)",
        },
        additional_instructions="Focus on the Progress and Tasks tables to determine member involvement.",
        save_dir=str(OUTPUT_DIR / "extraction" / "engagement"),
        model=MODEL,
        reset_files=True,
    )

    return result


def calculate_derived_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate derived metrics from extracted/rated data."""

    # Convert string numbers to numeric where possible
    numeric_cols = ["num_members", "precision_score_total", "num_tasks_completed",
                    "num_tasks_pending", "num_problems_listed", "num_priorities_listed"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Task completion rate
    if "num_tasks_completed" in df.columns and "num_tasks_pending" in df.columns:
        total_tasks = df["num_tasks_completed"].fillna(0) + df["num_tasks_pending"].fillna(0)
        df["task_completion_rate"] = (df["num_tasks_completed"].fillna(0) / total_tasks.replace(0, 1) * 100).round(1)

    # Overall ToV score (average of ToV metrics, excluding Frankenstein which is inverse)
    tov_cols = ["tov_presence", "tov_clarity", "tov_coherence", "tov_experiment_link"]
    available_tov_cols = [c for c in tov_cols if c in df.columns]
    if available_tov_cols:
        df["tov_overall_score"] = df[available_tov_cols].mean(axis=1).round(1)

    # Experimentation score
    exp_cols = ["hypothesis_explicitness", "experiment_rigor", "hypothesis_test_chain",
                "learning_evidence", "customer_voice"]
    available_exp_cols = [c for c in exp_cols if c in df.columns]
    if available_exp_cols:
        df["experimentation_score"] = df[available_exp_cols].mean(axis=1).round(1)

    # Team dynamics score
    dynamics_cols = ["task_tov_coherence", "strategy_consistency"]
    available_dynamics_cols = [c for c in dynamics_cols if c in df.columns]
    if available_dynamics_cols:
        df["alignment_score"] = df[available_dynamics_cols].mean(axis=1).round(1)

    return df


def generate_markdown_report(df: pd.DataFrame) -> str:
    """Generate a comprehensive Markdown report."""

    report = """# GABRIEL Management Report Analysis Results

## Executive Summary

This analysis examines 7 entrepreneurial team management reports using GABRIEL
to extract measures aligned with the Theory-Based View (TBV) research framework.

---

## Team Overview

| Team | Venture | Members | PES Score |
|------|---------|---------|-----------|
"""

    for _, row in df.iterrows():
        members = row.get("num_members", "N/A")
        pes = row.get("precision_score_total", "N/A")
        report += f"| {row['team_name']} | {row['venture']} | {members} | {pes}% |\n"

    report += """
---

## Section 4.1: Theory of Value Analysis

Measures how clearly teams articulate their business model and value proposition.

| Team | Presence | Clarity | Coherence | Experiment Link | Frankenstein Score |
|------|----------|---------|-----------|-----------------|-------------------|
"""

    tov_cols = ["tov_presence", "tov_clarity", "tov_coherence", "tov_experiment_link", "tov_frankenstein"]
    for _, row in df.iterrows():
        values = [str(row.get(c, "N/A")) for c in tov_cols]
        report += f"| {row['team_name']} | {' | '.join(values)} |\n"

    # Add interpretation
    if "tov_overall_score" in df.columns:
        avg_tov = df["tov_overall_score"].mean()
        report += f"""
**Key Finding**: Average Theory of Value score across teams: **{avg_tov:.1f}/100**

"""

    report += """
---

## Section 4.2-4.4: Team Dynamics

Measures task allocation, facilitation patterns, and decision-making.

| Team | Task Concentration | Role Specialization | Facilitator Evidence | Strategy Consistency |
|------|-------------------|---------------------|---------------------|---------------------|
"""

    dynamics_cols = ["task_concentration", "role_specialization", "facilitator_evidence", "strategy_consistency"]
    for _, row in df.iterrows():
        values = [str(row.get(c, "N/A")) for c in dynamics_cols]
        report += f"| {row['team_name']} | {' | '.join(values)} |\n"

    report += """
---

## Section 4.5: Experimentation Quality

Measures the rigor of hypothesis testing and learning cycles.

| Team | Hypothesis Explicitness | Experiment Rigor | H-T-R Chain | Learning Evidence | Customer Voice |
|------|------------------------|------------------|-------------|-------------------|----------------|
"""

    exp_cols = ["hypothesis_explicitness", "experiment_rigor", "hypothesis_test_chain",
                "learning_evidence", "customer_voice"]
    for _, row in df.iterrows():
        values = [str(row.get(c, "N/A")) for c in exp_cols]
        report += f"| {row['team_name']} | {' | '.join(values)} |\n"

    if "experimentation_score" in df.columns:
        avg_exp = df["experimentation_score"].mean()
        report += f"""
**Key Finding**: Average Experimentation score: **{avg_exp:.1f}/100**

"""

    report += """
---

## Section 4.6: Problems Classification

Categorizes the types of problems teams face.

| Team | Technical % | Market % | Team % | Financial % | Conflict Evidence | Severity |
|------|------------|----------|--------|-------------|-------------------|----------|
"""

    prob_cols = ["technical_problems", "market_problems", "team_problems",
                 "financial_problems", "conflict_evidence", "problem_severity"]
    for _, row in df.iterrows():
        values = [str(row.get(c, "N/A")) for c in prob_cols]
        report += f"| {row['team_name']} | {' | '.join(values)} |\n"

    report += """
---

## Section 4.7: Engagement Patterns

| Team | Most Mentioned | Least Mentioned | Equal Distribution |
|------|---------------|-----------------|-------------------|
"""

    for _, row in df.iterrows():
        most = row.get("most_mentioned_member", "N/A")
        least = row.get("least_mentioned_member", "N/A")
        equal = row.get("equal_distribution", "N/A")
        report += f"| {row['team_name']} | {most} | {least} | {equal} |\n"

    report += """
---

## Composite Scores Summary

| Team | ToV Score | Experimentation | Alignment | PES |
|------|-----------|-----------------|-----------|-----|
"""

    for _, row in df.iterrows():
        tov = row.get("tov_overall_score", "N/A")
        exp = row.get("experimentation_score", "N/A")
        align = row.get("alignment_score", "N/A")
        pes = row.get("precision_score_total", "N/A")
        report += f"| {row['team_name']} | {tov} | {exp} | {align} | {pes} |\n"

    report += """
---

## Research Implications

### What This Analysis Reveals

1. **Theory of Value Articulation**: Varies significantly across teams
2. **Task Distribution**: Evidence of both concentrated and distributed patterns
3. **Experimentation Maturity**: Range from ad-hoc to systematic approaches
4. **Problem Types**: Mix of technical, market, and team challenges

### Limitations (Addressed in Gap Analysis)

- Single time point snapshot (no longitudinal tracking)
- No individual vs. shared ToV comparison
- No diagram/visual analysis
- Problem persistence cannot be measured

---

*Generated by GABRIEL MR Analysis Pipeline*
*Colors: #D87756 #689BCC #C46686*
"""

    return report


async def main():
    """Main analysis pipeline."""
    print("=" * 60)
    print("GABRIEL Management Report Analysis")
    print("=" * 60)

    # Load reports
    print("\nLoading management reports...")
    df = load_reports()
    print(f"Loaded {len(df)} reports")

    # Run all analyses
    basic_df = await extract_basic_info(df)
    tov_df = await rate_theory_of_value(df)
    dynamics_df = await rate_team_dynamics(df)
    exp_df = await rate_experimentation(df)

    # Merge results
    result_df = df[["team_id", "team_name", "venture", "word_count"]].copy()

    # Merge basic extraction
    basic_cols = ["team_members", "num_members", "report_week", "precision_score_total",
                  "num_tasks_completed", "num_tasks_pending", "num_problems_listed",
                  "num_priorities_listed", "has_theory_of_value", "has_pivot_mentioned", "has_first_sale"]
    for col in basic_cols:
        if col in basic_df.columns:
            result_df[col] = basic_df[col]

    # Merge ToV ratings
    tov_cols = ["tov_presence", "tov_clarity", "tov_coherence", "tov_experiment_link", "tov_frankenstein"]
    for col in tov_cols:
        if col in tov_df.columns:
            result_df[col] = tov_df[col]

    # Merge dynamics ratings
    dynamics_cols = ["task_concentration", "role_specialization", "facilitator_evidence",
                     "coordination_centralization", "task_tov_coherence", "decision_selectivity",
                     "strategy_consistency"]
    for col in dynamics_cols:
        if col in dynamics_df.columns:
            result_df[col] = dynamics_df[col]

    # Merge experimentation ratings
    exp_cols = ["hypothesis_explicitness", "experiment_rigor", "hypothesis_test_chain",
                "learning_evidence", "customer_voice"]
    for col in exp_cols:
        if col in exp_df.columns:
            result_df[col] = exp_df[col]

    # Problems analysis (modifies df in place)
    df_with_problems = await classify_problems(df)
    prob_cols = ["technical_problems", "market_problems", "team_problems",
                 "financial_problems", "conflict_evidence", "problem_severity"]
    for col in prob_cols:
        if col in df_with_problems.columns:
            result_df[col] = df_with_problems[col]

    # Engagement analysis
    engagement_df = await analyze_engagement(df)
    engagement_cols = ["most_mentioned_member", "least_mentioned_member",
                       "cognitive_tasks_count", "execution_tasks_count", "equal_distribution"]
    for col in engagement_cols:
        if col in engagement_df.columns:
            result_df[col] = engagement_df[col]

    # Calculate derived metrics
    result_df = calculate_derived_metrics(result_df)

    # Save results
    print("\n" + "=" * 60)
    print("Saving results...")

    # CSV
    csv_path = OUTPUT_DIR / "mr_analysis_results.csv"
    result_df.to_csv(csv_path, index=False)
    print(f"  CSV saved: {csv_path}")

    # Markdown report
    md_report = generate_markdown_report(result_df)
    md_path = OUTPUT_DIR / "mr_analysis_report.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_report)
    print(f"  Markdown saved: {md_path}")

    # Summary stats
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)

    if "tov_overall_score" in result_df.columns:
        print(f"\nAverage Theory of Value Score: {result_df['tov_overall_score'].mean():.1f}")
    if "experimentation_score" in result_df.columns:
        print(f"Average Experimentation Score: {result_df['experimentation_score'].mean():.1f}")
    if "precision_score_total" in result_df.columns:
        valid_pes = pd.to_numeric(result_df["precision_score_total"], errors='coerce').dropna()
        if len(valid_pes) > 0:
            print(f"Average PES Score: {valid_pes.mean():.1f}%")

    print(f"\nResults saved to: {OUTPUT_DIR}")

    return result_df


if __name__ == "__main__":
    result = asyncio.run(main())
