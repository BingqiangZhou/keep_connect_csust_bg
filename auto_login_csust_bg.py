
import time

from utils.csust_bg import CSUST_BG
from utils.network import check_internet_connected
from utils.config import load_config, get_an_account_info
from utils.tips import info
from utils.logger import Logger
from utils.wifi import LinkWifi

wifi = LinkWifi()
csust_bg = CSUST_BG()
logger = Logger("./out.log")

wifi_name = 'csust-bg'
config = load_config("./config/auto_login_csust_bg.json")
logger.write(info(config))

account_infos = load_config(config['account_infos_file'])

first_time = True

while True:

    # 判断是否已连接到网络
    if check_internet_connected() is False: # 网络连接
        # 判断csust-bg是否在附近
        if wifi.check_wifi_in_nearby(wifi_name): # csust-bg wifi在附近，可以连接
            
            # 连接wifi csust-bg
            if wifi.connect_wifi(wifi_name) == wifi.status('connected'):
                logger.write(info("try login in csust-bg..."))
                while True:
                    # 尝试登陆csust-bg
                    account, password = get_an_account_info(account_infos)
                    # print(account, password)
                    login_result = csust_bg.login(account, password)
                    if login_result == CSUST_BG.LOGIN_FAILED: # 登录失败，一般是账号登不上去
                        account_infos.pop(account)
                        if len(account_infos) == 0:
                            break
                        continue
                    elif login_result == CSUST_BG.LOGIN_ERROR: # 出现异常，一般是请求1.1.1.1出错
                        logger.write(info("connect failed, try again..."))
                        # account_infos.clear()
                    else: # 登录成功
                        logger.write(info("network have been connected!"))
                        break
        else: #  csust-bg wifi不在附近，不可连接，退出程序
            info("csust-bg wifi not in nearby!")
            break
    if len(account_infos) == 0:
        break
    time.sleep(config['check_per_second'])