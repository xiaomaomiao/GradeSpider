class CountGpa(object):
    #初始化传入课程成绩的字典
    # #[{'score':'xx',''credit'xx,}]
    def __init__(self,grades):
        self.grades=grades
    #计算单门课程成绩所对应的绩点
    def singleGpa(self,grade):
        try:
            if int(grade)<60:
                return 0
            if int(grade) in range(60,65):
                return 2.0
            if int(grade) in range(65,70):
                return 2.5
            if int(grade) in range(70,75):
                return 3.0
            if int(grade) in range(75,80):
                return 3.5
            if int(grade) in range(80,85):
                return 4.0
            if int(grade) in range(85,90):
                return 4.5
            if int(grade)>=90:
                return 5.0
        except:
            if grade=='优秀':
                return 5.0
            if grade=='良好':
                return 4.5
            if grade=='中等':
                return 3.5
            if grade=='及格':
                return 2.0
            if grade=='不及格':
                return 0


    #计算绩点
    def count_Gpa(self):
        allCredit=0
        getCredit=0
        for grade in self.grades:
            #所有课程学分相加
            allCredit+=grade['credit']
            #计算学生总共得到的学分
            getCredit+=grade['credit']*self.singleGpa(grade['score'])
        #返回绩点
        return round(getCredit/allCredit,2)
