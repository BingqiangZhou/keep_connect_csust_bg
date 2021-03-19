# keep_network_connect.py相关说明

1. 源码以及相关包
   - [keep_network_connect.py源码](../keep_network_connect.py)
   - [requests包](https://pypi.org/project/requests/)
   - [pywifi包](https://pypi.org/project/pywifi/)
   - [pythonping](https://pypi.org/project/pythonping/)

2. 配置文件内容

    ```bash
        {
            # 程序每多少秒检查一次连接
            "check_per_second": 300, 

            # 学长打包的登陆csust的可执行程序的路径
            # 以下设置为相对路径（当前目录下），设置绝对路径更加方便，避免不必要的麻烦。
            "start_process": "Auto_login.exe", 

            # 可执行程序最大输出行数，超过最大输出函数，则结束尝试，
            # 一般一次连接尝试输出不超过三十行，当尝试次数过多时，说明账号列表中大多数账号已失效，
            # 设置为600，即设置最大尝试次数为二十几次。
            "check_max_line": 600
        }
    ```

3. 学长打包好的自动登陆csust-bg的可执行文件。

    [Auto_login.exe](https://github.com/linfangzhi/CSUST_network_auto_login/releases/download/1.0/Auto_login.exe) 
