import requests, re, time, random
from furl import furl
import codecs

from utils.network import check_internet_connected

class CSUST_BG():
    def __init__(self) -> None:
        self.__reback_url = 'http://1.1.1.1/?isReback=1'
        self.__login_url = 'http://192.168.7.221:801/eportal/'
        self.__login_url_params = {
            "c": "ACSetting",
            "a": "Login",
            "protocol": "http:",
            "hostname": "192.168.7.221",
            "iTermType": 1,
            "&enAdvert": 0,
            "queryACIP": 0,
            "loginMethod": 1,
        }
        self.__login_data = {
            'R1':'0', 
            'R2':'0', 
            'R3':'0', 
            'R6':'0', 
            'para':'00', 
            '0MKKey':'123456',
        }
    
    LOGIN_SUCCEED = 1
    LOGIN_FAILED = 0
    LOGIN_ERROR = -1
    
    def __get_related_infos__(self):
        try:
            response = requests.get(url=self.__reback_url, allow_redirects=False, timeout=5)
            location_url = response.headers['Location']
            location_furl = furl(location_url)
            wlanuserip = location_furl.args['wlanuserip']
            wlanacname = location_furl.args['wlanacname']
            wlanacip = location_furl.args['wlanacip']
            wlanusermac = location_furl.args['wlanusermac']
            wlanusermac = re.findall('\\w{1,2}', wlanusermac[:12]) # 将前面12个字母两两一组拆开
            wlanusermac = '-'.join(wlanusermac) # 将上面拆开的之后的字母间加入‘-’
            self.__login_url_params.update({
                "wlanuserip": wlanuserip,
                "wlanacip": wlanacip,
                "wlanacname": wlanacname,
                "mac": wlanusermac,
                "ip": wlanuserip,
            })
            # post_url = 'http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=192.168.7.221&iTermType=1&wlanuserip={wlanuserip}&wlanacip={wlanacip}&wlanacname={wlanacname}&mac={wlanusermac}&ip={wlanuserip}&enAdvert=0&queryACIP=0&loginMethod=1'.format(wlanusermac=wlanusermac,
            # wlanacip=wlanacip,
            # wlanacname=wlanacname,
            # wlanuserip=wlanuserip)
            return True
        except:
            return check_internet_connected()

    def login(self, account, password):
        try:
            if self.__get_related_infos__() is False:
                raise Exception('get info failed!')
            time.sleep(0.5)
            self.__login_data.update({
                'DDDDD': f',0,{account}', 
                'upass': f'{password}', 
            })
            post_url = furl(self.__login_url).add(self.__login_url_params).url
            requests.post(url=post_url, data=self.__login_data)
            if check_internet_connected():
                return CSUST_BG.LOGIN_SUCCEED
            return CSUST_BG.LOGIN_FAILED
        except:
            return CSUST_BG.LOGIN_ERROR

# CSUST_BG().login('003786', '003786')