# YiKaTong
校园一卡通密码用户暴力破解

使用方法：
  下载main.py文件和下载https://www.lanzous.com/i2cothe https://www.lanzous.com/i2coucf https://www.lanzous.com/i2djk5e
  请更改mian.py里面的学号
  请根据相应的学校的一卡通网站更改相应的url，一般只要改变学校简称字母缩写而已
  以下路径请根据实际情况更改
  
  在cmd中输入pip install pytesseract
  把Tesseract-OCR解压到C:\Program Files (x86)目录
  把nums.traineddata.rar（里面的文件是我专门为一卡通系统验证码训练的识别文件，提高验证码的识别率，目测识别率比99%还搞） 里面的文件解压到C:\Program Files (x86)\Tesseract-OCR\tessdata目录
  
  在C:\Users\daimiaopeng\AppData\Local\Programs\Python\Python36\Lib\site-packages 目录找到pytesseract-0.2.5-py3.6.egg，把下载的文件（pytesseract-0.2.5-py3.6.egg.zip解压后的pytesseract-0.2.5-py3.6）和它替换 ，如果没有的话则找到
  site-packages\pytesseract 目录把 pytesseract.py文件里的 tesseract_cmd = 'tesseract' 改成 tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
  
  然后点击main.py就行了，密码会保存在password.txt文件中，可以在main.py里面改指定的参数
  遍历密码速度有些慢，可以改一下文件参数，同时运行多个，这样速度可以加快很多
