# clash_config
https://docs.cfw.lbyczf.com/contents/parser.html#%E8%BF%9B%E9%98%B6%E6%96%B9%E6%B3%95-javascript
https://cdn.jsdelivr.net/gh/ hitori-Janai/clash_config/ config/start.yml

https://cdn.jsdelivr.net/gh/hitori-Janai/clash_config/parser.js

clash预处理脚本
https://raw.githubusercontent.com/hitori-Janai/clash_config/main/parser.js

```yaml
parsers: # array
  - reg: 'slbable$'
    yaml:
      prepend-rules:
        - DOMAIN-KEYWORD,bilibili.com,动画疯 # rules最前面增加一个规则
        - PROCESS-NAME,GenshinImpact.exe,【GAME】香港  VIP 8 - HGC
        - DOMAIN,clkservice.youdao.com,REJECT
        - DOMAIN,gorgon.youdao.com,REJECT
    # file: "D:/workspace/learn/clash_config/parser.js"
    remote:
      url: https://raw.githubusercontent.com/hitori-Janai/clash_config/main/parser.js
    commands:
      # - proxy-groups.1.proxies.0+'⚖️ 负载均衡-散列'
```

