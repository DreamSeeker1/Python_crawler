import json
import requests
import time


class Heihan(object):
    def __init__(self):
        self.start_url = 'http://36kr.com/api/search-column/mainsite?per_page=20&page={}&_={}'
        self.headers = {
'Host': '36kr.com',
'Connection': 'keep-alive',
'Accept': '*/*',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
'X-Tingyun-Id': 'Dio1ZtdC5G4;r=73477054',
'Referer': 'http://36kr.com/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9'
}

    def hodle_html(self,html):
        json_data = json.loads(html)
        content_list = [[i['id'],i['title']] for i in json_data['data']['items']]
        return content_list

    def save_content(self,content_list):
        with open('36kr.txt','a+',encoding='utf8') as f:
            for i in content_list:
                url = 'http://36kr.com/p/'+str(i[0])+'.html'
                f.write(url)
                f.write('\n')
                f.write(i[1])
                f.write('\n')

    def parse_url(self,url):
        resp = requests.get(url, headers=self.headers, timeout=15)
        return resp.content.decode()

    def run(self):
        n = 0
        while n < 20:
            n += 1
            a = time.time()
            a = str(a)
            a = a.replace('.', '')
            a = a[:13]
            next_url = self.start_url.format(n,a)
            html = self.parse_url(next_url)
            if html is not None:
                content_list = self.hodle_html(html)
                print(content_list)
                self.save_content(content_list)

if __name__ == '__main__':
    nh1 = Heihan()
    nh1.run()