"""使用 matplotlib 绘制带分布显示的散点图"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def load_style():
    try:
        plt.style.use("chartlab.mplstyle")
    except:
        pass
    # 设置中文字体，以正常显示中文
    # plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"] = False
    # 自定义样式
    plt.rcParams["axes.edgecolor"] = "#ffffff"

def create_chart(fig):
    ## 生成数据
    n = 80
    np.random.seed(7)
    X1 =np.random.normal(30, 8, n)
    Y1 = np.random.normal(60, 18, n)
    X2 = np.random.normal(70, 13, n)
    Y2 = np.random.normal(90, 20, n)
    X3 = np.random.normal(55, 15, n)
    Y3 = np.random.normal(50, 15, n)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    colors = ["#e97a7a", "#5595d1", "#e5c679", "#5db4b4", "#bb7dcc"]
    # 创建子图
    grid = plt.GridSpec(6, 6, hspace=0.2, wspace=0.2)
    main_ax = fig.add_subplot(grid[1:6, 0:5])
    y_hist_ax = fig.add_subplot(grid[1:6, 5], sharey=main_ax)
    x_hist_ax = fig.add_subplot(grid[0, 0:5], sharex=main_ax)

    # 绘制主散点图
    main_ax.scatter(X1, Y1, s=100, c=colors[0], alpha=0.5, label="label1")
    main_ax.scatter(X2, Y2, s=100, c=colors[1], alpha=0.5, label="label2")
    main_ax.scatter(X3, Y3, s=100, c=colors[2], alpha=0.5, label="label3")

    # 绘制直方图
    width_x = 1
    width_y = 2.5

    bins = np.arange(min(X1),max(X1)+ width_x,width_x)
    x_hist_ax.hist(X1, bins=bins, color=colors[0], alpha=0.5, edgecolor="#ffffff", linewidth=1)
    bins = np.arange(min(Y1), max(Y1)+ width_y, width_y)
    y_hist_ax.hist(
        Y1,
        bins=bins,
        orientation="horizontal",
        color=colors[0],
        alpha=0.5,
        edgecolor="#ffffff",
        linewidth=1,
    )

    bins = np.arange(min(X2),max(X2)+ width_x,width_x)
    x_hist_ax.hist(X2, bins=bins, color=colors[1], alpha=0.5, edgecolor="#ffffff", linewidth=1)
    bins = np.arange(min(Y2), max(Y2)+ width_y, width_y)
    y_hist_ax.hist(
        Y2,
        bins=bins,
        orientation="horizontal",
        color=colors[1],
        alpha=0.5,
        edgecolor="#ffffff",
        linewidth=1,
    )

    bins = np.arange(min(X3),max(X3)+ width_x,width_x)
    x_hist_ax.hist(X3, bins=bins, color=colors[2], alpha=0.5, edgecolor="#ffffff", linewidth=1)
    bins = np.arange(min(Y3), max(Y3)+ width_y, width_y)
    y_hist_ax.hist(
        Y3,
        bins=bins,
        orientation="horizontal",
        color=colors[2],
        alpha=0.5,
        edgecolor="#ffffff",
        linewidth=1,
    )

    # 去掉直方图的标签
    x_hist_ax.tick_params(
        axis="x", which="both", bottom=False, top=False, labelbottom=False)
    y_hist_ax.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

    # 设置刻度间距
    main_ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    main_ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    main_ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    main_ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))

    ## 设置文本信息
    fig.suptitle("Scatter plot with distribution display")
    main_ax.set_xlabel("X axis")
    main_ax.set_ylabel("Y axis")
    main_ax.legend(loc="upper center",ncols=3)
    plt.tight_layout()

if __name__ == "__main__":
    load_style()
    fig = plt.figure(figsize=(8, 5),dpi=150)
    create_chart(fig)
    plt.savefig("scatter_distribution.png")