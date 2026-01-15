"""
Generate presentation charts for GABRIEL MR Analysis
Uses color palette: #D87756 #689BCC #C46686
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Color palette
CORAL = '#D87756'
BLUE = '#689BCC'
ROSE = '#C46686'
DARK = '#2D3748'
LIGHT = '#F7FAFC'

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14

# Output directory
OUTPUT_DIR = Path("../gdoc-output/charts")
OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv("../gdoc-output/mr_analysis_results.csv")

# Clean team names for display
df['display_name'] = df['team_name'].str.replace('Team ', '').str.replace(' - Friendly', '')


def chart1_tov_scores():
    """Theory of Value scores horizontal bar chart"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Sort by score
    sorted_df = df.sort_values('tov_overall_score', ascending=True)

    y_pos = np.arange(len(sorted_df))
    bars = ax.barh(y_pos, sorted_df['tov_overall_score'], color=CORAL, height=0.6)

    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, sorted_df['tov_overall_score'])):
        ax.text(val + 1, i, f'{val:.1f}', va='center', fontweight='bold', color=DARK)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_df['display_name'])
    ax.set_xlabel('ToV Quality Score (0-100)')
    ax.set_title('Theory of Value Quality by Team', fontweight='bold', pad=20)
    ax.set_xlim(0, 100)

    # Add average line
    avg = df['tov_overall_score'].mean()
    ax.axvline(avg, color=BLUE, linestyle='--', linewidth=2, label=f'Average: {avg:.1f}')
    ax.legend(loc='lower right')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'chart1_tov_scores.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 1: ToV Scores")


def chart2_htr_chain():
    """Hypothesis-Test-Result Chain Quality (the 'subjective' task Jake doubted)"""
    fig, ax = plt.subplots(figsize=(10, 6))

    sorted_df = df.sort_values('hypothesis_test_chain', ascending=True)
    y_pos = np.arange(len(sorted_df))

    # Color bars based on performance
    colors = [CORAL if v >= 70 else ROSE if v >= 50 else BLUE for v in sorted_df['hypothesis_test_chain']]
    bars = ax.barh(y_pos, sorted_df['hypothesis_test_chain'], color=colors, height=0.6)

    for i, (bar, val) in enumerate(zip(bars, sorted_df['hypothesis_test_chain'])):
        ax.text(val + 1, i, f'{val:.0f}', va='center', fontweight='bold', color=DARK)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_df['display_name'])
    ax.set_xlabel('H-T-R Chain Quality Score (0-100)')
    ax.set_title('Hypothesis → Test → Result Chain Quality\n(Jake rated this 1-2, "will be weak")',
                 fontweight='bold', pad=20)
    ax.set_xlim(0, 100)

    # Add annotation
    ax.annotate('NGM: Systematic\ncurriculum testing\nshows up clearly!',
                xy=(86, 6), xytext=(70, 4.5),
                fontsize=10, color=CORAL,
                arrowprops=dict(arrowstyle='->', color=CORAL))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'chart2_htr_chain.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 2: H-T-R Chain Quality")


def chart3_problem_types():
    """Problem type distribution stacked bar chart"""
    fig, ax = plt.subplots(figsize=(12, 6))

    teams = df['display_name'].values
    tech = df['technical_problems'].values
    market = df['market_problems'].values
    team = df['team_problems'].values

    x = np.arange(len(teams))
    width = 0.25

    bars1 = ax.bar(x - width, tech, width, label='Technical', color=CORAL)
    bars2 = ax.bar(x, market, width, label='Market', color=BLUE)
    bars3 = ax.bar(x + width, team, width, label='Team Process', color=ROSE)

    ax.set_ylabel('Problem Percentage (%)')
    ax.set_title('Problem Type Distribution by Team\n(Jake rated classification task as 2)',
                 fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(teams, rotation=45, ha='right')
    ax.legend()
    ax.set_ylim(0, 100)

    # Add annotation for Dream Team
    ax.annotate('Dream Team:\nStadium API = high tech',
                xy=(2, 62), xytext=(2.5, 80),
                fontsize=9, color=CORAL,
                arrowprops=dict(arrowstyle='->', color=CORAL))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'chart3_problem_types.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 3: Problem Types")


def chart4_task_concentration():
    """Task concentration bar chart"""
    fig, ax = plt.subplots(figsize=(10, 6))

    sorted_df = df.sort_values('task_concentration', ascending=False)
    y_pos = np.arange(len(sorted_df))

    # Color gradient based on concentration
    colors = [CORAL if v >= 50 else ROSE if v >= 30 else BLUE for v in sorted_df['task_concentration']]
    bars = ax.barh(y_pos, sorted_df['task_concentration'], color=colors, height=0.6)

    for i, (bar, val) in enumerate(zip(bars, sorted_df['task_concentration'])):
        ax.text(val + 1, i, f'{val:.0f}%', va='center', fontweight='bold', color=DARK)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_df['display_name'])
    ax.set_xlabel('Task Concentration (%)')
    ax.set_title('Task Concentration: Who Does the Work?\n(0% = perfectly distributed, 100% = one person)',
                 fontweight='bold', pad=20)
    ax.set_xlim(0, 100)

    # Add zones
    ax.axvspan(0, 30, alpha=0.1, color=BLUE, label='Distributed')
    ax.axvspan(30, 50, alpha=0.1, color=ROSE, label='Moderate')
    ax.axvspan(50, 100, alpha=0.1, color=CORAL, label='Concentrated')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'chart4_task_concentration.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 4: Task Concentration")


def chart5_composite_scores():
    """Composite scores radar/comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Metrics to compare
    metrics = ['tov_overall_score', 'experimentation_score', 'alignment_score']
    metric_labels = ['ToV Quality', 'Experimentation', 'Alignment']

    x = np.arange(len(df))
    width = 0.25

    for i, (metric, label) in enumerate(zip(metrics, metric_labels)):
        offset = (i - 1) * width
        color = [CORAL, BLUE, ROSE][i]
        bars = ax.bar(x + offset, df[metric], width, label=label, color=color)

    ax.set_ylabel('Score (0-100)')
    ax.set_title('Composite Performance Scores by Team', fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(df['display_name'], rotation=45, ha='right')
    ax.legend()
    ax.set_ylim(0, 100)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'chart5_composite_scores.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 5: Composite Scores")


def chart6_jake_vs_reality():
    """Jake's predictions vs actual performance"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Jake's ratings and actual outcomes
    measures = [
        'H-T-R Chain\nQuality',
        'ToV\nCoherence',
        'Problem\nClassification',
        'Selectivity vs\nInclusion',
        'Experiment→ToV\nLink'
    ]

    jake_ratings = [1.5, 2, 2, 1, 2]  # Jake's 1-3 scale
    actual_scores = [
        df['hypothesis_test_chain'].mean() / 100 * 3,  # Normalize to 1-3
        df['tov_coherence'].mean() / 100 * 3,
        (df['technical_problems'].std() + df['market_problems'].std()) / 30 * 3,  # Variance = works
        df['decision_selectivity'].mean() / 100 * 3,
        df['tov_experiment_link'].mean() / 100 * 3
    ]

    x = np.arange(len(measures))
    width = 0.35

    bars1 = ax.bar(x - width/2, jake_ratings, width, label="Jake's Prediction", color=ROSE, alpha=0.7)
    bars2 = ax.bar(x + width/2, actual_scores, width, label='Actual Performance', color=CORAL)

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{height:.1f}', ha='center', va='bottom', fontsize=9)
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{height:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_ylabel('Performance Rating (1-3 scale)')
    ax.set_title('Jake\'s Predictions vs Reality\n("Subjective" tasks Jake said would fail)',
                 fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(measures)
    ax.legend()
    ax.set_ylim(0, 3.5)
    ax.axhline(2, color='gray', linestyle=':', alpha=0.5, label='Adequate (2.0)')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'chart6_jake_vs_reality.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 6: Jake vs Reality")


def chart7_experimentation_breakdown():
    """Experimentation metrics breakdown"""
    fig, ax = plt.subplots(figsize=(12, 7))

    metrics = ['hypothesis_explicitness', 'experiment_rigor', 'hypothesis_test_chain',
               'learning_evidence', 'customer_voice']
    labels = ['Hypothesis\nExplicitness', 'Experiment\nRigor', 'H-T-R\nChain',
              'Learning\nEvidence', 'Customer\nVoice']

    # Create heatmap-style visualization
    data = df[metrics].values

    # Sort teams by average experimentation score
    sort_idx = df['experimentation_score'].argsort()[::-1]
    data_sorted = data[sort_idx]
    teams_sorted = df['display_name'].values[sort_idx]

    im = ax.imshow(data_sorted, cmap='RdYlGn', aspect='auto', vmin=40, vmax=100)

    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(teams_sorted)))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(teams_sorted)

    # Add text annotations
    for i in range(len(teams_sorted)):
        for j in range(len(labels)):
            val = data_sorted[i, j]
            color = 'white' if val < 60 or val > 85 else 'black'
            ax.text(j, i, f'{val:.0f}', ha='center', va='center', color=color, fontweight='bold')

    ax.set_title('Experimentation Quality Breakdown by Team\n(Section 4.5 metrics)', fontweight='bold', pad=20)

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Score (0-100)')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'chart7_experimentation_breakdown.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 7: Experimentation Breakdown")


def chart8_summary_dashboard():
    """Summary dashboard with key metrics"""
    fig = plt.figure(figsize=(14, 10))

    # Create grid
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

    # Metric 1: Average ToV Score
    ax1 = fig.add_subplot(gs[0, 0])
    avg_tov = df['tov_overall_score'].mean()
    ax1.pie([avg_tov, 100-avg_tov], colors=[CORAL, LIGHT], startangle=90,
            wedgeprops=dict(width=0.3))
    ax1.text(0, 0, f'{avg_tov:.1f}', ha='center', va='center', fontsize=28, fontweight='bold', color=CORAL)
    ax1.set_title('Avg ToV Score', fontweight='bold')

    # Metric 2: Average Experimentation Score
    ax2 = fig.add_subplot(gs[0, 1])
    avg_exp = df['experimentation_score'].mean()
    ax2.pie([avg_exp, 100-avg_exp], colors=[BLUE, LIGHT], startangle=90,
            wedgeprops=dict(width=0.3))
    ax2.text(0, 0, f'{avg_exp:.1f}', ha='center', va='center', fontsize=28, fontweight='bold', color=BLUE)
    ax2.set_title('Avg Experimentation', fontweight='bold')

    # Metric 3: Average Alignment Score
    ax3 = fig.add_subplot(gs[0, 2])
    avg_align = df['alignment_score'].mean()
    ax3.pie([avg_align, 100-avg_align], colors=[ROSE, LIGHT], startangle=90,
            wedgeprops=dict(width=0.3))
    ax3.text(0, 0, f'{avg_align:.1f}', ha='center', va='center', fontsize=28, fontweight='bold', color=ROSE)
    ax3.set_title('Avg Alignment', fontweight='bold')

    # Bottom: Summary bar
    ax4 = fig.add_subplot(gs[1, :])

    categories = ['Jake: Works', 'Jake: Weak', 'Actually\nWorks', 'Actually\nNeeds Data']
    values = [8, 10, 15, 3]  # Approximate counts from analysis
    colors_bottom = [BLUE, ROSE, CORAL, '#888888']

    bars = ax4.bar(categories, values, color=colors_bottom)
    ax4.set_ylabel('Number of Measures')
    ax4.set_title('Jake\'s Assessment vs Reality', fontweight='bold', pad=10)

    for bar, val in zip(bars, values):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 str(val), ha='center', fontweight='bold')

    plt.suptitle('GABRIEL MR Analysis: Summary Dashboard', fontsize=16, fontweight='bold', y=0.98)
    plt.savefig(OUTPUT_DIR / 'chart8_summary_dashboard.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Chart 8: Summary Dashboard")


if __name__ == "__main__":
    print("Generating charts...")
    print(f"Output directory: {OUTPUT_DIR.absolute()}")
    print()

    chart1_tov_scores()
    chart2_htr_chain()
    chart3_problem_types()
    chart4_task_concentration()
    chart5_composite_scores()
    chart6_jake_vs_reality()
    chart7_experimentation_breakdown()
    chart8_summary_dashboard()

    print()
    print("=" * 50)
    print(f"All charts saved to: {OUTPUT_DIR}")
    print("=" * 50)
