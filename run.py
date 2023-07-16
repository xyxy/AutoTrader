from autotrader import Trader
from autotrader.utils.stock import get_today_ipo_data

if __name__ == "__main__":
    user = Trader().init_trader(folder_path=r"C:\同花顺软件\同花顺")
    print(user.position)
    print(get_today_ipo_data())
    print(user.balance)
    # for i in range(10):
    #     print(user.position)
    user.buy('162411', price=0.55, amount=100)
    # 雪球组合比例调仓
    user.adjust_weight('股票代码', 0.2)

