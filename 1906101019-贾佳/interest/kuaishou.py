from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '8', # 手机安卓版本
  'deviceName': 'KWG5T16325001859', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.kuaishou.nebula', # 启动APP Package名称
  'appActivity': 'com.yxcorp.gifshow.HomeActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
#   'User-Agent':'User-Agent:Mozilla/5.0'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# driver.find_element_by_id('texture_view').click()
start_x = 500
start_y = 1500
distance = 1300

time.sleep(10)
        # app开启之后点击一次屏幕，确保页面的展示
# driver.tap([(500, 1200)], 500)  #appium中模拟手指点击方法，叫tap，有两个参数，元素位置和点击持续时间ms

        # 无限滑动
        
while True:
    driver.swipe(start_x, start_y, start_x,start_y-distance,300)#模拟滑动
            # 设置延时等待
    time.sleep(5)