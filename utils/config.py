import json
import random

# 加载配置
def load_config(config_file_path):
    with open(config_file_path, 'r') as f:
        config = json.load(f)
    return config

def get_an_account_info(account_infos: dict):
    account = random.choice(list(account_infos.keys()))
    password = account_infos[account]
    return account, password

def load_accounts_from_txt(txt_file):
    account_infos = {}
    with open(txt_file, 'r') as f:
        info = f.readline()
        while len(info) != 0:
            account, password = [s.strip() for s in info.split(":")]
            account_infos.update({account: password})
            info = f.readline()
    return account_infos