# autotrader使用说明

## 准备工作：

1. 同花顺交易软件普通版（PC端）。
2. 登录一次同花顺账号并设置**记住密码**和**自动登录**。
3. 登录一次同花顺中委托下单并设置**自动启动交易**。



<img src=".\static\image-20230602200233562.png" alt="image-20230602200233562" style="zoom: 50%;" /><img src=".\static\image-20230602205535490.png" alt="image-20230602205535490"  />



## 操作流程：

1. 安装依赖包：pip install -r requirements.txt
2. 启动测试项目：python run.py

## 补充说明：

- 调用实例或函数：

```python
import autotrader
from autotrader.utils.stock import get_today_ipo_data

user = autotrader.Trader().init_trader(folder_path=r"C:\同花顺软件\同花顺")
print(user.position)
print(get_today_ipo_data())

```

- 使用方法与easytrader使用一致，easytrader使用文档：https://easytrader.readthedocs.io/zh/master/usage/

  

- 该项目仅支持同花顺普通版，仅供学习。

