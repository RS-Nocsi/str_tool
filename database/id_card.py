from id_validator import validator

def check(num):
    #校检身份证号码合法性
    if validator.is_valid(num):
        print("身份证通过校检！！！以下是身份证的信息：")
        info(num)
        if validator.get_info(num)["sex"] == 1:
            print("性别：男")
        elif validator.get_info(num)["sex"] == 2:
            print("性别：女")
    else:
        print("身份证校检失败！！！")
        
def info(num):
    #输出身份证信息
    if validator.get_info(num) == False:
        print("身份证输入有误！！！")
    else:
        print("地址：",validator.get_info(num)["address"])
        print("生日：",validator.get_info(num)["birthday_code"])
        print("生肖：",validator.get_info(num)["chinese_zodiac"])
        print("星座：",validator.get_info(num)["constellation"])