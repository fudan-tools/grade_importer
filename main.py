import login
import requests;
import json;
import time;

cookie = login.get_session();
s = requests.session()
s.cookies = requests.utils.cookiejar_from_dict(cookie);
s.get("https://fdjwgl.fudan.edu.cn/student/home");
res = s.get("https://fdjwgl.fudan.edu.cn/student/for-std/grade/sheet");
uid = res.url.split("/")[-1];
semester = "504";
with open("grades.json","r",encoding="utf-8") as f:
    courses = json.load(f);
while(1):
    url = "https://fdjwgl.fudan.edu.cn/student/for-std/grade/sheet/info/%s?semester=%s"%(uid,semester);
    res = s.get(url);
    data = res.json()["semesterId2studentGrades"][semester];
    for i in data:
        if(not(i["courseName"] in courses)):
            print("课程:",i["courseName"],"，等级：",i["gaGrade"],",绩点：",i["gp"]);
            courses[i["courseName"]] = [i["gaGrade"],i["gp"]];
            with open("grades.json", "w", encoding="utf-8") as f:
                json.dump(courses,f);
    time.sleep(300);
