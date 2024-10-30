"""带趋势显示的散点图-Scatter plot with trend display"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit

def load_style():
    try:
        plt.style.use("chartlab.mplstyle")
    except:
        pass
    # plt.rcParams["font.sans-serif"]=["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"]= False
    plt.rcParams["axes.edgecolor"]="#ffffff"

def linear_fit(X, Y, color, ax):
    coefficients = np.polyfit(X, Y, 1)
    polynomial =np.poly1d(coefficients)
    xs =np.linspace(np.min(X), np.max(X), 100)
    ys = polynomial(xs)
    ax.plot(xs, ys, color=color, linestyle="--", linewidth=3, label="linear_1d")

def polynomial_fit(X, Y, color, ax):
    coefficients =np.polyfit(X, Y, 2)
    polynomial = np.poly1d(coefficients)
    xs =np.linspace(np.min(X), np.max(X), 100)
    ys = polynomial(xs)
    ax.plot(xs, ys,color=color, linestyle="--", linewidth=3, label=f"polynomial_2d")

def exponential_fit(X, Y,color, ax):
    def model(x, a, b, c):
        return a * np.exp(b*x) + c
    popt, _ = curve_fit(model, X, Y)
    xs = np.linspace(np.min(X), np.max(X), 100)
    ys = model(xs, *popt)
    ax.plot(xs, ys, color=color, linestyle="--", linewidth=3, label="exponential")

def create_chart(ax):
    n=80
    np.random.seed(42)
    # 线性数据
    X1 = np.random.uniform(0, 10, n)
    Y1 = 2 * X1 + 3 + np.random.normal(0, 5, n) + 10
    # 二次多项式数据
    X2 = np.random.uniform(0, 10, n)
    Y2 = 1.5 * X2**2 - 10 * X2 + 5 + np.random.normal(0, 10, n) + 80
    # 指数数据
    X3 = np.random.uniform(0, 10, n)
    Y3 = 2 * np.exp(0.3 * X3) + np.random.normal(0, 15, n) + 40

    # 绘制散点和拟合曲线
    colors =["#e97a7a", "#5595d1", "#e5c679"]
    Xs = [X1, X2, X3]
    Ys = [Y1, Y2, Y3]
    labels = ["linear data", "polynomial data", "exponential data"]
    functions = [linear_fit, polynomial_fit, exponential_fit]
    for i in range(3):
        ax.scatter(Xs[i], Ys[i], s=100, c=colors[i], alpha=0.5, label=labels[i])
        ax.scatter(Xs[i], [-0.5]*len(Xs[i]), marker="|", color=colors[i], alpha=0.5, s=300)

        ax.scatter([-0.5] * len(Xs[i]), Ys[i], marker="_", color=colors[i], alpha=0.5, s=300)

        functions[i](Xs[i], Ys[i], colors[i], ax)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))

    ax.set_title("Scatter plot with trend display")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.legend(ncols=3, loc="upper center")
    plt.tight_layout()

if __name__ == "__main__":
    load_style()
    fig, ax=plt.subplots(figsize=(8, 5), dpi=150)
    create_chart(ax)
    plt.savefig("scatter_trend.png")