import test
import crawler
# Path of the `.yml` file 
start_path = './config/start.yml'
end_path = './config/end.yml' 
proxies_path = './config/proxies.yml'
config_path = './config/config.yml'

# 
config = {}

def main():
    proxies = test.readYml(proxies_path)
    start = test.readYml(start_path)
    end = test.readYml(end_path)

    # proxies["proxies"] = proxies["proxies"][:5]

    group =  test.generate_group(test.group_path,proxies)
    config = start | end | proxies | group

    test.saveYml(config_path, config)






# crawler.main()  
main()