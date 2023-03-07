module.exports.parse = async (
  raw,
  { axios, yaml, notify, console },
  { name, url, interval, selected }
) => {
  var math = require("mathjs");

  const obj = yaml.parse(raw);

  let group_str = `
      name: ⚖️ 负载均衡-散列
      type: load-balance
      url: http://www.apple.com/library/test/success.html
      interval: 300
      proxies:
      strategy: consistent-hashing
      `;
  // 插入p0~p4组
  let p_group = [];
  let num = math.ceil(obj["proxies"].length / 5);
  let p;
  for (let i = 0; i < obj["proxies"].length; i++) {
    if (i % num == 0) {
      p = yaml.parse(group_str);
      p["name"] = "p" + i / num;
      p["type"] = "url-test";
      p["proxies"] = [];
      delete p.strategy;
      p_group.push(p);
    }
    const element = obj["proxies"][i];
    p["proxies"].push(element["name"]);
  }
  obj["proxy-groups"].push(...p_group); // 使用扩展运算符将p_group展开为单个元素

  // 插入⚖️ 负载均衡-散列
  let group_load = yaml.parse(group_str);
  group_load["proxies"] = p_group.map((p) => p.name);
  obj["proxy-groups"].push(group_load);
  obj["proxy-groups"][1].proxies.unshift('⚖️ 负载均衡-散列')
  return yaml.stringify(obj);
};
