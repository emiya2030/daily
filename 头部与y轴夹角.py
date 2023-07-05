import numpy as np
from sklearn.linear_model import LinearRegression
import math

# 定义坐标数据
coordinates = np.array([
    [0.0167857, -0.0856498],
    [-0.00646758, -0.108121],
    [-0.0321474, -0.130889],
    [-0.057392, -0.151169],
    [-0.0795655, -0.16783]
])
# 拟合线性回归模型
regression_model = LinearRegression()
regression_model.fit(coordinates[:, 0].reshape(-1, 1), coordinates[:, 1])

# 提取回归系数
slope = regression_model.coef_[0]

# 计算拟合直线与 y 轴之间的夹角
rotation_angle_rad = math.atan(1 / slope)
rotation_angle_deg = math.degrees(rotation_angle_rad)

print(f"拟合直线与 y 轴的夹角: {rotation_angle_deg} 度")
