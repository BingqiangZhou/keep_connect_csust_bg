# 自动连接Wifi，登陆csust-bg，并保持连接

在学长代码[linfangzhi/CSUST_network_auto_login](https://github.com/linfangzhi/CSUST_network_auto_login)的基础上，添加如下功能：

1. 自动连接wifi (只支持windows、linux平台)
2. 断开，自动重新连接
3. 自动获取账号列表(不会公开)

为了防止账号信息泄漏，这里有些代码不会上传。

## 相关文件说明

1. [keep_network_connect.py](/data/keep_network_connect.md): 与学长打包好的可执行文件[Auto_login.exe](https://github.com/linfangzhi/CSUST_network_auto_login/releases/download/1.0/Auto_login.exe)联动，加入自动连接wifi功能，实现断开自动连接。

2. [auto_login_csust_bg.py](/auto_login_csust_bg.py): 在学长代码的基础上，修改自动连接代码，加入自动连接wifi、断开自动连接功能，**注：账号信息未上传，代码不可用**。

## 相关可执行文件下载

1. [Auto_login.exe](https://github.com/linfangzhi/CSUST_network_auto_login/releases/download/1.0/Auto_login.exe) 学长打包好的自动登陆csust-bg的可执行文件。
2. WebDriver
      - [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
      - [WebDriver for Chrome](https://chromedriver.chromium.org/downloads)
      - [WebDriver in Safari](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari)
      - [WebDriver for Firefox](https://github.com/mozilla/geckodriver/releases)