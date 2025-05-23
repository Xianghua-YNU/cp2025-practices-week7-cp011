# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：CP011
- 成员：杨程宇 马海尔吉 王珏 肖澎
- 实验日期：20250409

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。
1： sp.symbols()
    sp.cos()
    sp.tan()
2:  sp.symbols()
    sp.cos()
    exp()
3:  exp()
    cos(t)
    sin(t)

---

## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

*(插入图片或截图并简要分析曲线特点)*![Figure 2025-04-09 111136 (1)](https://github.com/user-attachments/assets/2196ed20-3cc4-4c03-bd9b-c185a5968b36)

周期性，关于y轴对称，在x=0.5附近剧烈震荡
### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

*(插入图片或截图并简要分析隐函数曲线特点)*![Figure 2025-04-09 111136 (2)](https://github.com/user-attachments/assets/4ff74f1d-062d-4de0-b86f-964aa45059e0)

非对称结构，在x=0附近y值变化显著，其余区域较为平缓
### 问题3: 参数曲面绘制结果

*(插入图片或截图并简要分析三维曲面的特点)*![Figure 2025-04-09 111136 (3)](https://github.com/user-attachments/assets/67a24ff3-5f56-4ccb-8a8e-b20cabe60ead)
随着xyz的变化，曲面螺旋上升，z方向大致为线性，xOy平面的投影是一个圆

---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？照葫芦画瓢
- 实验中你遇到了哪些问题？如何解决？人机结合解决问题
- 你对SymPy的绘图功能有什么建议或意见？无

---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html
