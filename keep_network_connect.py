import time

from utils.network import check_internet_connected, start_subprocess_to_login_csust_bg
from utils.config import load_config
from utils.tips import info
from utils.logger import Logger

from utils.wifi import LinkWifi

wifi = LinkWifi()
logger = Logger('./out.log')

config = load_config('config/keep_network_connect.json')
logger.write(info(f"config: {config}\n"))

while True:
    # 判断是否已连接到网络
    if check_internet_connected() is False:
        
        # 连接WiFi
        if wifi.connect_wifi('csust-bg') == wifi.status('connected'):
            logger.write(info("connecting"))
            
            # 启动子进程，登录csust-bg
            if start_subprocess_to_login_csust_bg(config['start_process'], config['check_max_line']) is True:
                logger.write(info("network has been connected!"))
            else:
                logger.write(info("connect failed!")) # 运行出现错误，或者尝试次数过多

    # 等待N秒
    time.sleep(config['check_per_second'])
