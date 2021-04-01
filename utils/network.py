import time
import codecs
import random
import requests
import subprocess
from pythonping import ping

# from utils.wifi import LinkWifi

# wifi = LinkWifi()

hosts = [
    "https://cn.bing.com/", "https://www.baidu.com", "http://www.sina.com.cn/", "https://weibo.com/", "http://www.sohu.com/", 
    "http://www.qq.com/", "http://www.163.com/", "https://www.jd.com/", "https://www.suning.com", "https://www.hao123.com/",
    "https://www.taobao.com/", "http://www.ctrip.com/", "http://www.zhihu.com/", "http://www.iqiyi.com/", "https://www.ximalaya.com/",
    "http://www.cnki.net/", "https://www.ifeng.com/", "https://58.com/", "https://www.vip.com/", "https://www.douban.com/",
    "http://xueshu.baidu.com/", "https://www.hupu.com/", "https://music.163.com/", "http://www.huya.com/"
]

user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
    (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

# 检测网络是否已连接
# def check_internet_connected():
#     try:
#         if wifi.check_wifi_connected() == LinkWifi.status("connected"):
#             host_url = random.choice(hosts)
#             response = requests.get(host_url, timeout=1, headers=user_agent, allow_redirects=False)
#             # print(response.text)
#             # if response.status_code == 200:
#             #     return True
#             return True
#     except:
#         return False

# 检测网络是否已连接
def check_internet_connected():
    try:
        result = ping('baidu.com', timeout=0.1)
        # if "Request timed out" in str(result):
            # return False
        # return True
        if "Reply from" in str(result):
            return True
        return False
    except:
        return False

# 启动子进程来连接csust-bg
def start_subprocess_to_login_csust_bg(process_path, max_out_lines=1000, check_str="登录成功"):
    p = subprocess.Popen(process_path, shell=True, stdout=subprocess.PIPE)
    line = 0
    while p.poll() == None:
        time.sleep(0.1)
        out = p.stdout.readline()
        line += 1
        # 输出超过max_out_lines行还没有返回输出
        if line >= max_out_lines:
            break
        if check_str in codecs.decode(out, 'gb2312'):
            p.kill()
            return True
    p.kill()
    return False

# for host_url in hosts:
#     response = requests.get(host_url, timeout=1, headers=user_agent, allow_redirects=False)
#     print(host_url, response.status_code)
