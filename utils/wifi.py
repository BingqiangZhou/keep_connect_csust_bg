from pywifi import PyWiFi, const, Profile
import time

class LinkWifi():
    def __init__(self):
        self.wifi = PyWiFi()
        self.iface = self.wifi.interfaces()[0]

        self.akm = {
            'None': const.AKM_TYPE_NONE,
            'WPA': const.AKM_TYPE_WPAPSK,
            'WPA2': const.AKM_TYPE_WPA2PSK,
        }

    def check_wifi_connected(self, timeout=5):
        max_try_times = timeout // 0.5
        cur_try_times = 0
        while True:
            status = self.iface.status()
            if status in [const.IFACE_INACTIVE, const.IFACE_CONNECTED]:
                return status
            else:
                if cur_try_times >= max_try_times:
                    break
                time.sleep(0.5)
                cur_try_times += 1
        return const.IFACE_DISCONNECTED
    
    @staticmethod
    def status(status):
        if status == "disconnected":
            return const.IFACE_DISCONNECTED
        elif status == "scanning":
            return const.IFACE_SCANNING
        elif status == "inactive":
            return const.IFACE_INACTIVE
        elif status == "connecting":
            return const.IFACE_CONNECTING
        elif status == "connected":
            return const.IFACE_CONNECTED
        else:
            return -1


    def connect_wifi(self, wifi_name, wifi_key=None, akm='WPA2', check_connected=True):

        assert akm in ['None', 'WPA', 'WPA2']

        profile = Profile()
        # The ssid of the AP(Authentication Profile).
        profile.ssid = wifi_name

        # The authentication algorithm of the AP. For normal case, almost all the APs use open algorithm.
        profile.auth = const.AUTH_ALG_OPEN

        # The cipher type of the AP. The cipher type should be set to the Profile if the akm is not AKM_TYPE_NONE.
        cipher = const.CIPHER_TYPE_CCMP
        if wifi_key == None:
            akm = 'None'
            cipher = const.CIPHER_TYPE_NONE
        else:
            profile.key = wifi_key
        profile.cipher = cipher

        # The key management type of the AP.
        profile.akm.append(self.akm[akm])

        profile = self.iface.add_network_profile(profile)
        self.iface.connect(profile)

        if check_connected:
            return self.check_wifi_connected()
        else:
            return True

    def disconnect_wifi(self):
        is_connected = self.check_wifi_connected(timeout=1)

        if is_connected:
            # Disconnect current AP connection.
            self.iface.disconnect()


    def get_wifi_list(self, time_out=8, no_wait=True):
        # Trigger the interface to scan APs.
        self.iface.scan()
        max_try_times = time_out // 0.5
        cur_try_times = 0
        if no_wait:
            while True:
                profiles = self.__get_scan_result__(only_name=False)
                if len(profiles) > 0:
                    return profiles
                else:
                    if cur_try_times >= max_try_times:
                        break
                    time.sleep(0.5)
                    cur_try_times += 1
            return None
        else:
            time.sleep(time_out)
            return self.__get_scan_result__(only_name=False)
    
    def check_wifi_in_nearby(self, wifi_name, time_out=8):
        self.iface.scan()
        max_try_times = time_out * 2
        for i in range(max_try_times):
            time.sleep(0.5)
            # print(self.__get_scan_result__())
            if wifi_name in self.__get_scan_result__():
                return True
        return False
    
    def __get_scan_result__(self, only_name=True):
        wifi_name_list = []
        wifi_list = []
        profiles = self.iface.scan_results()
        if profiles is not None:
            for p in profiles:
                if p.ssid not in wifi_name_list:
                    wifi_list.append(p)
                    wifi_name_list.append(p.ssid)
        if only_name:
            return wifi_name_list
        return wifi_list


# wifi = LinkWifi()
# # wifi.check_wifi_connected('csust-bg')
# profiles = wifi.get_wifi_list(timeout=2, return_when_get=False)
# if profiles is not None:
#     for p in profiles:
#         print(p.ssid, p.key, p.akm, p.cipher, p.auth)
    
