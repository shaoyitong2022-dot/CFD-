# CFDPython 中文本土化教程（12 步走向 Navier–Stokes + 谐振子 PINN）

一门**面向中国物理系学生**的计算流体力学（CFD）+ 科学机器学习（SciML）入门课程：
从零手写有限差分求解器，一路走到 Navier–Stokes 方程；再用最小的例子理解 PINN（物理信息神经网络）。

> 本课程是 [Barba & Forsyth 的 CFD Python（12 steps to Navier–Stokes）](https://github.com/barbagroup/CFDPython) 的**中文本土化 + 逐行注释版**，并扩展了一条完整的 PINN 主线。
> 官方课程内容遵循 CC-BY 4.0 / BSD-3 许可发布（见 [LICENSE](LICENSE)），本仓库所有讲义在同样许可下提供。

---

## 为什么为物理系学生做这门课

物理系的同学大多在《数学物理方法》里学过偏微分方程，
但"怎么把 $\frac{\partial u}{\partial t} + c\frac{\partial u}{\partial x}=0$ 变成一行能跑的代码"——学校里往往不讲。
这门课的每一课都把 **公式 ↔ 代码 逐行对照**，让数理背景直接变成代码能力。

## 课程结构（两条轨，共 15 课）

**A 轨 · FDM（CFDPython 12 步）**——手写数值求解器

| 课 | 内容 | 帮你掌握 |
|---|---|---|
| 0001 | 环境点火与 NumPy | 数组、切片、第一张图、向量化 |
| 0002 | Step 1 一维线性对流 | 迎风差分、怎么把 PDE 变成代码 |
| 0003 | Step 2 非线性对流 | 波速=自身，帽子的尖锐化 |
| 0004 | CFL 条件专章 | 格式稳定性，域名解析 |
| 0005 | Step 3 一维扩散 | 中心差分、FTCS |
| 0006 | Step 4 一维 Burgers | SymPy 符号求导、周期边界 |
| 0007 | Step 5+6 二维对流 | 二维网格、meshgrid、向量化 |
| 0008 | Step 7+8 二维扩散与 Burgers | 积木组装 |
| 0009 | Step 9+10 Laplace 与 Poisson | 椭圆方程、迭代法 |
| 0010 | Step 11+12 二维 NS 腔流/通道流 | 投影法、压力泊松方程 |

**B 轨 · PINN（谐振子）**——理解物理信息神经网络

| 课 | 内容 | 帮你掌握 |
|---|---|---|
| 0011 | PINN 概念 | 裸 NN 为什么只会插值 |
| 0012 | PyTorch 训练循环 | FCN 网络类、Adam |
| 0013 | autograd 与物理损失 | torch.autograd.grad 二阶导 |
| 0014 | PINN 合体 | 数据损失 + 物理损失、外推成功 |
| 0015 | 三线对比（收官） | 解析 vs FDM vs PINN 同框 |

## 快速开始

```bash
# 1. 克隆本仓库
git clone https://github.com/<your-name>/cfdpython-zh.git
cd cfdpython-zh

# 2. 用 conda 建环境（或直接用 Anaconda 预装环境）
conda create -n cfd python=3.10
conda activate cfd
conda install -c conda-forge numpy matplotlib sympy scipy jupyter

# 3. 打开教程导航页（或用浏览器直接打开 index.html）
docs/index.html          # 课程导航（15 课索引）
# 或逐课打开 lessons/0002-*.html ... 开始学习
```

> PyCharm 用户：新建项目 → Python Interpreter 选 `cfd` 环境 → 打开 `.ipynb` 即可运行。

## 学习方法建议（写给初学者）

这门课沿用了 Barba 教授亲授的几"铁律"，请务必照做：

1. **手打，不复制粘贴**——每个代码块都亲手敲一遍，这是最有价值的一步。
2. **每课做"闭卷自测"**——课页末尾有小测（合上书回答，再对答案）。
3. **改参数、做实验**——每课都设计了"改 `nx`、改 `dt`、看变化"的实验，动手才懂。

## 目录结构

```
├── index.html          # 课程导航首页
├── docs/               # 推荐从这里看 HTML 讲义
├── lessons/            # 15 课 HTML 讲义
├── tablet/             # 平板/离线自包含版（单文件，可直接传到手机/平板看）
├── reference/          # 术语表等参考
├── code/
│   └── cfdpython-repo/ # 官方 CFDPython 原始 notebook（教材底本）
└── LICENSE             # CC-BY 4.0
```

## 致谢与许可

- 课程内容建立在 **Prof. Lorena A. Barba 与 Gilbert F. Forsyth 的 [CFD Python](https://github.com/barbagroup/CFDPython)** 之上，系其官方教程的中文本土化 + 逐行注释扩展。引用请见其 JOSS 论文：
  > Barba, L. A., & Forsyth, G. F. (2018). CFD Python: the 12 steps to Navier–Stokes equations. *Journal of Open Source Education*, 1(9), 21. https://doi.org/10.21105/jose.00021
- 原始官方教学内容：CC-BY 4.0；官方代码：BSD-3。
- 本仓库全部讲义与代码：**[CC-BY 4.0](LICENSE)**。
- 若你使用本仓库，欢迎保留原课程署名，并 Star 支持。

## 后续扩展（另见其他仓库）

- **C 轨**：DeepXDE 工业级 PINN 框架
- **FNO 轨**：Fourier Neural Operator 算子学习