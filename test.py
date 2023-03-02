import yaml
import copy
import numpy as np
from random import shuffle

proxies_path = './config/proxies.yml'

group_path = './config/proxy_group/select.yml'

group_num = 5

# 读取yml文件
def read_yml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        yml_data = yaml.safe_load(f)
    return yml_data

# 存储yml文件
def save_yml(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, allow_unicode=True)

# 手动代理组
def select_group(path, proxies_name):
    select = read_yml(path)
    sel_group(proxies_name, select)
    newp_names = p_group(proxies_name, select)
    load_group(select, newp_names)
    return select

def load_group(select, newp_names):
    select['proxy-groups'][2]['proxies'] = newp_names
    select['proxy-groups'][3]['proxies'] = newp_names

def sel_group(proxies_name, select):
    select['proxy-groups'][0]['proxies'] = proxies_name

def p_group(proxies_name, select):
    newp_names = []
    p = select['proxy-groups'].pop(2)
    shuffle(proxies_name) # 乱序代理名字
    for i, proxy_name in enumerate(np.array_split(proxies_name,group_num)): # enumerate(proxies_name): # 
        newp = copy.deepcopy(p)
        newp['proxies'] = proxy_name.tolist() # 添加代理
        newp_name = 'p'+str(i)
        newp['name'] = newp_name # 修改组名
        newp_names.append(newp_name)
        select['proxy-groups'].append(newp)
    return newp_names


def generate_group(path, proxies):
    group = select_group(path, [p['name'] for p in proxies["proxies"]])
    return group