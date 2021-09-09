import matplotlib.pyplot as plt
import matplotlib.patches as patches

from colorbrains_research.display_plots import get_plot_path


def basecolors(df):
    colors = []
    labels = []
    for i, v in df.iterrows():
        labels.append(v['color_name'])
        colors.append((v['red'], v['green'], v['blue']))

    fig, (ax, ax_greens) = plt.subplots(figsize=(14,8), ncols=2, gridspec_kw={'width_ratios': [3 ,1.5]})
    offset = .25
    width = 3

    max_y = 0.9
    min_y = .05

    annotate_y = 0.5

    for count, (label, color) in enumerate(zip(colors, labels)):
        start = width * count
        _offset = offset * (count + 1)
        rect = patches.Rectangle((start+_offset, min_y), width, max_y, linewidth=1, edgecolor='k', facecolor=color, alpha=0.6)
        ax.add_patch(rect)

        rect = patches.Rectangle((start+_offset, min_y + .95), width, max_y + 0.05, linewidth=1, edgecolor='k', facecolor=color, alpha=0.6)
        ax.add_patch(rect)

        g = ax.annotate(color, (start + _offset + offset * 4, annotate_y), size='large', va='center')
        g.set_bbox(dict(facecolor='white', alpha=0.9,))
        g = ax.annotate(label, (start + _offset + offset, annotate_y + 1), size='small', va='center')
        g.set_bbox(dict(facecolor='white', alpha=0.9,))

    rect = patches.Rectangle((0, 0), 1, 1, linewidth=1, edgecolor='g', facecolor='g', alpha=0.6)
    ax_greens.add_patch(rect)
    rect = patches.Rectangle((1, 0), 1, 1, linewidth=1, edgecolor=(0,1,0), facecolor=(0,1,0), alpha=0.6)
    ax_greens.add_patch(rect)


    g = ax_greens.annotate('g', (0.35, 0.5), size='large', va='center')
    g.set_bbox(dict(facecolor='white', alpha=0.9,))
    g = ax_greens.annotate('(0.0, 1.0, 0.0)', (1.35, 0.5), size='large', va='center')
    g.set_bbox(dict(facecolor='white', alpha=0.9,))


    ax_greens.set_xlim(0, 2)
    ax_greens.set_ylim(0,1)
    ax_greens.axes.get_xaxis().set_visible(False)
    ax_greens.axes.get_yaxis().set_visible(False)
    ax_greens.set_title('Matplotlib Difference Named Green And RGB Green (0,1,0)')


    ax.set_xlim(0, (len(labels) + 0.75) * width)
    ax.set_ylim(0,2)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_title('Matplotlib Basecolors', size=24)
    plt.tight_layout()
    filename = get_plot_path('basecolors.png')
    plt.savefig(filename)
    fig.clear()
    plt.close()
    return filename



def color_comparison(ax, color1, color2):
    rect = patches.Rectangle((0, 0), 1, 1, linewidth=1, edgecolor=color1, facecolor=color1, alpha=0.6)
    ax.add_patch(rect)
    rect = patches.Rectangle((1, 0), 1, 1, linewidth=1, edgecolor=color2, facecolor=color2, alpha=0.6)
    ax.add_patch(rect)


    g = ax.annotate(f'{color1}', (0.35, 0.5), size='large', va='center')
    g.set_bbox(dict(facecolor='white', alpha=0.9,))
    g = ax.annotate(f'{color2}', (1.35, 0.5), size='large', va='center')
    g.set_bbox(dict(facecolor='white', alpha=0.9,))


    ax.set_xlim(0, 2)
    ax.set_ylim(0,1)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_title(f'Matplotlib Difference ({color1}) and ({color2})')

    return ax


def cmy_comparisons():

    fig, axes = plt.subplots(figsize=(14,8), ncols=3, gridspec_kw={'width_ratios': [1 ,1, 1]})
    colorsets = ((0, 0.75, 0.75), (0, 1, 1)), ((0.75, 0, 0.75), (1, 0, 1)), ((0.75, 0.75, 0), (1, 1, 0) )
    for ax, colors in zip(axes, colorsets):
        color_comparison(ax, *colors)
    
    plt.tight_layout()
    filename = get_plot_path('cmy_comparison.png')
    plt.savefig(filename)
    fig.clear()
    plt.close()
    return filename
