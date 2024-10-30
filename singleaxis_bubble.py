"""使用 matplotlib 绘制单轴分组气泡图"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D

def load_style():
    try:
        plt.style.use("chartlab.mplstyle")
    except:
        pass
    # plt.rcParams["font.sans-serif"]=["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"]= False

def create_chart(ax):
    np.random.seed(1)
    days = ["data1", "data2", "data3","data4", "data5"]
    size = 30
    data ={day:np.random.randint(20, 500, size=size) for day in days}
    colors =["#e97a7a", "#5595d1", "#e5c679", "#5db4b4", "#bb7dcc"] 

    for i, (day, values)in enumerate(data.items()):
        x_data = np.random.uniform(0,24,size)
        ax.scatter(x_data,[i]*size, s=values, c=colors[i], alpha=0.5, label=day)
    
    ax.set_yticks(range(len(days)))
    ax.set_yticklabels(days)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
    ax.set_ylim(-0.5, 5)
    ax.grid(axis='y')
    ax.set_xlabel("X axis")
    ax.set_title("Single axis grouped bubble chart")
    legend = ax.legend(loc="upper center",ncol=5)
    legend.get_frame().set_edgecolor("#ffffff")
        
    def create_marker(color, label, size):
        return Line2D(
            [0],
            [0],
            marker="o",
            color="#ffffff",
            markersize=size,
            markerfacecolor=color,
            markeredgecolor="#ffffff",
            label=label,
        )
        
    age_markers = [
        create_marker("#aaaaaa", "data=20", 8),
        create_marker("#aaaaaa", "data=300", 14),
        create_marker("#aaaaaa", "data=500", 22),
    ]

    legend_age = ax.legend(handles=age_markers, loc="upper center", ncol=3)
    legend_age.get_frame().set_edgecolor("#ffffff")
    ax.add_artist(legend_age)
    plt.tight_layout()

if __name__ == "__main__":
    load_style()
    fig,ax = plt.subplots(figsize=(8, 5), dpi=150)
    create_chart(ax)
    plt.savefig("singleaxis_bubble.png")