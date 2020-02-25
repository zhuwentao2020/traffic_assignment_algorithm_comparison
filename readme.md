# 交通分配-线性成本

说明|标号
-|-
需求|$D$
路径集合|$\mathcal{A}$
路径($a \in \mathcal{A}$)通行能力|$C_a$
路径($a \in \mathcal{A}$)自由时间|$T_a$
流量空间|$\mathcal{V}$


$$\mathcal{V} = \left\{ v: \sum_{a \in \mathcal{R}} v_a = D; v_a \geq 0, \forall a \in \mathcal{A} \right\} $$

$$
\begin{aligned}
\min \quad & \sum_{a \in \mathcal{A}} \frac{T_a v_a^2}{2 C_a}\\
s.t. \quad & v \in \mathcal{V}
\end{aligned}
$$