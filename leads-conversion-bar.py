import numpy as np
import matplotlib.pyplot as plt


pipedrive_deals_status = ['Lost', 'Open',
                  'Won']
owner_name = {
    'Pedro': [10, 15, 17],
    'Julia': [26, 22, 29],
    'Felipe': [35, 37, 7],
    'Lucas': [32, 11, 9],
    'Marianna': [21, 29, 5],
    'Lara': [8, 19, 5]
}


def survey(owner_name, pipedrive_deals_status):
    labels = list(owner_name.keys())
    data = np.array(list(owner_name.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(pipedrive_deals_status, pipedrive_deals_status.colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


survey(owner_name, pipedrive_deals_status)
plt.show()
