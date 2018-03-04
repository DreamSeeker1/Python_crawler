import json
import requests
import time


class Heihan(object):
    def __init__(self):
        self.start_url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}'
        self.headers = {
'Host': 'neihanshequ.com',
'Connection': 'keep-alive',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-CSRFToken': '7e6e260a547acd228b48b72bdf555a72',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
'Referer': 'http://neihanshequ.com/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'csrftoken=7e6e260a547acd228b48b72bdf555a72; tt_webid=6519685378109752846; uuid="w:812f1a36388644a0857f402900831b45"; _ga=GA1.2.2111294360.1517982542; _gid=GA1.2.1042682935.1517982542'
}

    def hodle_html(self,html):
        json_data = json.loads(html)
        max_time = json_data['data']['max_time']
        has_more = json_data['data']['has_more']
        content_list = [[i['group']['share_url'],i['group']['text']] for i in json_data['data']['data']]
        return max_time,content_list,has_more

    def save_content(self,content_list):
        with open('neihan1.txt','a+',encoding='utf8') as f:
            for i in content_list:
                f.write(i[0])
                f.write('\n')
                f.write(i[1])
                f.write('\n')

    def parse_url(self,url):
        resp = requests.get(url, headers=self.headers, timeout=15)
        return resp.content.decode()

    def run(self):
        next_url = self.start_url
        has_more = True
        n = 0
        while has_more:
            if n == 20:
                break
            n += 1
            html = self.parse_url(next_url)
            print(next_url)
            if html is not None:
                max_time,content_list,has_more = self.hodle_html(html)
                print(content_list)
                self.save_content(content_list)
                next_url = self.start_url.format(max_time)
            else:
                has_more = False


if __name__ == '__main__':
    nh1 = Heihan()
    nh1.run()