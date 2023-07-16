# 获取资金状况
user.balance

# 获取持仓
user.position

# 买入
user.buy('162411', price=0.55, amount=100)

# 卖出
user.sell('162411', price=0.55, amount=100)

# 一键打新
user.auto_ipo()

# 撤单
user.cancel_entrust('buy/sell 获取的 entrust_no')

# 查询当日成交
user.today_trades

# 查询当日委托
user.today_entrusts

# 查询今日可申购新股
from easytrader.utils.stock import get_today_ipo_data
ipo_data = get_today_ipo_data()
print(ipo_data)

# 刷新数据
user.refresh()

# 雪球组合比例调仓
user.adjust_weight('股票代码', 目标比例)

# 退出客户端软件
user.exit()

# 交易服务端——启动服务
from easytrader import server
server.run(port=1430) # 默认端口为 1430

# 量化策略端——调用服务
from easytrader import remoteclient
user = remoteclient.use('使用客户端类型，可选 yh_client, ht_client, ths, xq等', host='服务器ip', port='服务器端口，默认为1430')
user.buy(......)
user.sell(......)

# 交易函数用法同上，见“四、交易相关”
# 初始化跟踪的 trader
xq_user = easytrader.use('xq')
xq_user.prepare('xq.json')

# 跟踪 joinquant / ricequant 的模拟交易


# 初始化跟踪 joinquant / ricequant 的 follower
target = 'jq'  # joinquant
target = 'rq'  # ricequant
follower = easytrader.follower(target)
follower.login(user='rq/jq用户名', password='rq/jq密码')

# 连接 follower 和 trader
# joinquant
follower.follow(xq_user, 'jq的模拟交易url')
jq_follower.follow(user, '模拟交易url',
                   trade_cmd_expire_seconds=100000000000, cmd_cache=False)

# ricequant
follower.follow(xq_user, run_id)

# 初始化跟踪的 trader
同上

# 初始化跟踪 雪球组合 的 follower
xq_follower = easytrader.follower('xq')
xq_follower.login(cookies='雪球 cookies，登陆后获取，获取方式见 https://smalltool.github.io/2016/08/02/cookie/')

# 连接 follower 和 trader
xq_follower.follow(xq_user, 'xq组合ID，类似ZH123456', total_assets=100000)

# 多用户跟踪多策略
follower.follow(users=[xq_user, yh_user], strategies=['组合1', '组合2'], total_assets=[10000, 10000])

# 登录
python cli.py --use yh --prepare gf.json

# 获取余额 / 持仓 / 以及其他变量
python cli.py --get balance

# 买卖 / 撤单
python cli.py --do buy 162411 0.450 100

# 查看帮助
python cli.py --help




