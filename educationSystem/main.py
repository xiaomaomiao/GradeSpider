from educationSystem import spider
#打印4班所有人成绩
id='1506010502'
while(int(id)<1506010535):
    spider.GetHhuGrade(id,id)
    id=str(int(id)+1)