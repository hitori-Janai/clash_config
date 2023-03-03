import requests
import urllib.parse
import datetime
import os
import test

url = 'https://clashnode.com/wp-content/uploads/2023/03/20230303.yaml'
nodes_path = './config/nodes/'

def newUrl(url, month, file_name):
    parsed_url = urllib.parse.urlparse(url)
# Split the path into a list of components
    path_components = parsed_url.path.split('/')
    
    path_components[-1] = file_name
    path_components[-2] = month

# Join the path components back into a string
    new_path = '/'.join(path_components)

# Replace the path attribute of the parsed URL with the new path
    new_parsed_url = parsed_url._replace(path=new_path)

# Unparse the URL back into a string
    new_url = urllib.parse.urlunparse(new_parsed_url)
    return new_url

def todayYml():
    now = datetime.date.today()
    formatted_date = now.strftime("%Y%m%d")
    return formatted_date+'.yaml'

def todayMonth():
    now = datetime.date.today()
    formatted_date = now.strftime("%m")
    return formatted_date

def crawler(url, nodes_path):
    today_yml = todayYml()
    new_url = newUrl(url, todayMonth(), today_yml)

    parsed_url = urllib.parse.urlparse(url)
# Get the domain name from the netloc attribute
    domain_name = parsed_url.netloc
# Send a GET request to the server and save the response as a stream
    print("new_url",new_url)
    response = requests.get(new_url, stream=True)


    dirs_path = nodes_path + domain_name + '/'
    os.makedirs(dirs_path, exist_ok=True)
    filepath = dirs_path + today_yml
# Open a local file with wb (write binary) permission.
    with open(filepath, 'wb') as f:
    # Loop over the response stream
        for chunk in response.iter_content(chunk_size=1024):
        # Write data chunk to local file
            f.write(chunk)
    return filepath

def main():
    filepath = crawler(url, nodes_path)
    node = test.readYml(filepath)
    test.saveYml(test.proxies_path,{'proxies':node['proxies']})
# main()