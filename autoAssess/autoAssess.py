#自动完成评估
import time
from selenium.webdriver import ActionChains
from educationSystem import spider
url="http://202.119.113.135/jxpgXsAction.do?oper=listWj"
class AutoAssess(object):
    def __init__(self,id,passwd):
        #初始化登录,获取成功登录浏览器
        self.driver =spider.GetHhuGrade(id,passwd).get_driver()
    #评估主方法
    def assess(self):
        self.driver.get(url)
        self.traverse_course()
    def traverse_course(self):
        #获取最后一个table
        course_trs=self.driver.find_elements_by_xpath("//td[@class='pageAlign']/table/tbody/tr")
        courses = []
        count=1
        for course_tr in course_trs:
            #统计需要评估的课程
            print(self.get_assess_courses(course_tr,courses,count))
            count=count+1
        #评估课程
        self.assess_course(courses)
    # 统计需要评估的课程
    def get_assess_courses(self,course_tr,courses,count):
        #判断该门课程是否已经评估
        if course_tr.find_element_by_xpath("td[last()]/img").get_attribute("title")=='查看':
            print("")
        else:
            #课程名入数组
            courses.append(count)
        return courses
    #对所有课程进行评估
    def assess_course(self,courses):
        #遍历
        for course in courses:
            self.driver.get(url)
            course_tr=self.driver.find_element_by_xpath("//td[@class='pageAlign']/table/tbody/tr["+str(course)+"]")
            course_tr.find_element_by_xpath("td[last()]/img").click()
            trs=self.driver.find_elements_by_xpath("//table[@class='fieldsettop']/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr")
            count=1
            for tr in trs:
                if count%2==0:
                    #进行点击
                    input_radio=tr.find_element_by_xpath("td/input[1]")
                    input_radio.click()
                    #ActionChains(self.driver).move_to_element(input_radio).click(input_radio).perform()
                count=count+1
            #填写主管评价
            self.driver.find_element_by_xpath("//textarea[@name='zgpj']").send_keys("老师讲的非常好，我收获很大")
            #提交
            self.driver.find_element_by_xpath("//table[@class='fieldsettop']/tbody/tr/td/table[4]/tbody/tr/td/img[1]").click()
            print("评价成功")