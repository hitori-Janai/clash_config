import test
import crawler
# Path of the `.yml` file 

proxies_path = './config/proxies.yml'
config_path = './config/config.yml'

# 
config = {}

def main():
    proxies = test.readYml(proxies_path)
    start, end = test.gennerate_other_group()

    # proxies["proxies"] = proxies["proxies"][:5]

    group =  test.generate_group(test.group_path,proxies)
    config = start | end | proxies | group

    test.saveYml(config_path, config)






if __name__ == '__main__':
# crawler.main()  
    main()