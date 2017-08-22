import re
import time
import sys
from educationSystem import image_download
from educationSystem.utils import disposeImage, autoRecognize
from selenium import webdriver
from educationSystem.utils import GPA
url="http://202.119.113.135/"
class GetHhuGrade(object):
    #初始化学生信息
    def __init__(self,id,passwd):
        self.id=id
        self.passwd=passwd
        self.driver=webdriver.PhantomJS()
        self.driver.get(url)
        self.login()
    #尝试登录
    def login(self):
        # 下载验证码图片
        self.driver.save_screenshot(sys.path[1]+"/educationSystem/verifyImage/verifyResource.png")
        # 处理验证码图片
        disposeImage.disposeImage()
        v_yzm = autoRecognize.autoRecognize()
        self.driver.find_element_by_xpath("//input[@name='zjh']").send_keys(self.id)
        self.driver.find_element_by_xpath("//input[@name='mm']").send_keys(self.passwd)

        v_yzm=self.get_verifyCode(v_yzm)
        self.driver.find_element_by_name("v_yzm").send_keys(v_yzm)
        # 登录

        self.driver.find_element_by_id("btnSure").click()
        #如果登录失败
        if(self.get_name()==''):
            print("验证码识别错误，重新识别")
            self.driver.get(url)
            self.login()
        else:
            #打印成绩信息
            print("姓名：",self.get_name())
            self.print_grade()
    #获取学生姓名
    def get_name(self):
        self.driver.get("http://202.119.113.135/menu/top.jsp")
        nameStr = self.driver.find_element_by_xpath("//td[@nowrap='']").text
        name = re.compile(".*\((.*)\)").match(nameStr).group(1)
        return name
    #识别验证码
    def get_verifyCode(self,v_yzm):
        count = 1
        whetherQuit = 0
        while (True):
            if (v_yzm == '' or len(v_yzm)!=4):
                # 没有获取到验证码
                whetherQuit = 0
                # 点击换一张验证码
                self.driver.find_element_by_link_text("看不清，换一张").click()
                time.sleep(1)
               # print("识别验证码第", count, "次")
                count = count + 1
                # 下载验证码图片
                self.driver.save_screenshot(sys.path[1]+"/educationSystem/verifyImage/verifyResource.png")
                # 处理验证码图片
                disposeImage.disposeImage()
                # 获取验证码
                v_yzm = autoRecognize.autoRecognize()

            else:
                whetherQuit = 1
            if (whetherQuit == 1):
                # 获取到了验证码：退出循环
                break
        v_yzm = v_yzm.replace(' ', '')
        result = ''
        for one in re.findall(r"(\w*)", v_yzm):
            result = result + one
        print(result)
        print("已自动识别验证码")
        return result
    #打印成绩
    def print_grade(self):
        grades_countGpa=[]
        self.driver.get("http://202.119.113.135/bxqcjcxAction.do")
        grades = self.driver.find_elements_by_xpath("//td[@class='pageAlign']/table/thead/tr[position()>1]")
        print("课程", "\000\000\000\000\000\000\000\000\000\000", "成绩", "\000\000\000\000\000", "全院名次")
        for grade in grades:
            print(grade.find_element_by_xpath("td[3]").text + "\000\000\000\000\000",
                  grade.find_element_by_xpath("td[10]").text + "\000\000\000\000\000",
                  grade.find_element_by_xpath("td[11]").text)
            #计算绩点
            if grade.find_element_by_xpath("td[6]").text.replace(' ','')=='必修' and grade.find_element_by_xpath("td[10]").text!='':
                #获取该门课程的学分
                credit=grade.find_element_by_xpath("td[5]").text.replace(' ','')
                grades_countGpa.append({'score':grade.find_element_by_xpath("td[10]").text.replace(' ',''),
                               'credit':float(credit)
                               })

        print("绩点:",GPA.CountGpa(grades_countGpa).count_Gpa())
    def get_driver(self):
        return self.driver