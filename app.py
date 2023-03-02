import test

# Path of the `.yml` file 
start_path = './config/start.yml'
end_path = './config/end.yml' 
proxies_path = './config/proxies.yml'
config_path = './config/config.yml'

# 
config = {}

def main():
    proxies = test.read_yml(proxies_path)
    start = test.read_yml(start_path)
    end = test.read_yml(end_path)

    # proxies["proxies"] = proxies["proxies"][:5]

    group =  test.generate_group(test.group_path,proxies)
    config = start | end | proxies | group

    test.save_yml(config_path, config)
    
main()