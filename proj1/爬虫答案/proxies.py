import json
from lxml import etree

import requests
import time


class Heihan(object):
    def __init__(self):
        self.start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.headers = {
'Host': 'www.kuaidaili.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://www.baidu.com/link?url=KCAT_rDQw-JNo6f6DAqGWWVEwbMa6G8Yf2hNn-6ARvNKUm1MHSsFWLGO5rgTg1Gz&wd=&eqid=b11fa5080003d9f4000000025a7c0394',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'channelid=0; _ga=GA1.2.1839423082.1518076808; _gid=GA1.2.207332776.1518076808; _gat=1; sid=1518076088309655; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1518076808,1518076821; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1518076821'
}

    def hodle_html(self,html):
        tr_list = html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr")
        content_list = []
        for i in tr_list:
            one_ip = []
            IP = i.xpath('./td[@data-title="IP"]/text()')
            port = i.xpath('./td[@data-title="PORT"]/text()')
            anonymous_de = i.xpath('./td[@data-title="匿名度"]/text()')
            one_ip.append(IP)
            one_ip.append(port)
            one_ip.append(anonymous_de)
            content_list.append(one_ip)
        return content_list

    def save_content(self,content_list):
        with open('ip.txt','a+',encoding='utf8') as f:
            for i in content_list:
                ip = 'ip：'+str(i[0])+' '
                f.write(ip)
                port = 'port：' + str(i[1]) + ' '
                f.write(port)
                aaa = '匿名度：' + str(i[2]) + ' '
                f.write(aaa)
                f.write('\n')

    def parse_url(self,url):
        time.sleep(2)
        resp = requests.get(url, headers=self.headers, timeout=15)
        return etree.HTML(resp.content)

    def run(self):
        n = 0
        while n < 20:
            n += 1
            next_url = self.start_url.format(n)
            html = self.parse_url(next_url)
            # print(html.xpath("//table[@class='table table-bordered table-striped']"))
            if html is not None:
                content_list = self.hodle_html(html)
                self.save_content(content_list)

if __name__ == '__main__':
    nh1 = Heihan()
    nh1.run()