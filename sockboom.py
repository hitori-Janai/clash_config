import requests
import time
from queue import Queue
import yaml
import test

config_yml = test.readYml('config.yml')
url_sockboom = config_yml['url_sockboom']
nodes_path = './config/nodes/'
config_name = 'sockboom.yml'


def run_time(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print('running', end-start, 's')
    return wrapper


class Sockboom():
    def __init__(self):
        self.qurl = Queue()
        self.data = list()
        self.qurl.put(url_sockboom)
        self.sockboom_path = nodes_path + config_name
        self.new_config = {}

    def download(self):
        response = requests.get(self.qurl.get(), stream=True)
        self.sockboom_node = yaml.load(response.content.decode('utf-8'), Loader=yaml.FullLoader)
        with open(self.sockboom_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

    def generate_proxies(self):  # 添加代理组所有数组
        self.new_config |= {'proxies': self.sockboom_node['proxies']}
        return self

    def generate_group(self):
        group = test.generate_group(test.group_path, self.new_config)
        self.new_config |= group
        return self

    def generate_other(self):
        start, end = test.gennerate_other_group()
        self.new_config = start | end | self.new_config
        return self

    @run_time
    def run(self):
        self.download()
        self.generate_proxies().generate_other().generate_group()
        test.saveYml(test.config_path, self.new_config)


if __name__ == '__main__':
    Sockboom().run()
