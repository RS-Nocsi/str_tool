#导入库
import random
import string
import sys
from time import *
import math
import re
from database import id_card
#欢迎界面
print("欢迎进入文本操作工具，这是一个可以进行文本相关操作的工具")
print("作者：Abyss")
print("文本操作工具-v3.0")
print("最后更新于：2020/8/30")
print("现在进入功能选择界面……")
sleep(1)

#功能选择
print("")
Function_selection = input("生成随机字符输入1\n生成随机数字输入2\n生成高强度密码输入3\n生成随机浮点数输入4\n列出一个范围内的素数输入5\n过滤特定文本输入6\n校检身份证号码输入7\n查看帮助输入help\n退出输入exit：")

#主判断

#主循环
while True:

    #生成随机字符部分
    if Function_selection == "1":
        print("")
        print("现在是生成随机字符模式")
        Random_character_length = input("请输入随机字符的长度(必须为整数)：")
        print("正在生成，请等待……")
        Random_character = ''.join(random.sample(string.ascii_letters + string.digits, int(Random_character_length)))
        sleep(1)
        print("生成完毕！")
        print("随机字符为：",Random_character)
        sleep(1)
        print("")

    #生成随机数字部分
    elif Function_selection == "2":
        print("")
        print("现在是生成随机数字模式")
        n_min = input("请输入随机数字的最小值(必须为整数)：")
        n_max = input("请输入随机数字的最大值(必须为整数)：")
        print("正在生成，请等待……")
        n_random = random.randint(int(n_min),int(n_max))
        sleep(1)
        print("生成完毕！")
        print("随机数字为：",n_random)
        sleep(1)
        print("")

    #生成高强度密码部分
    elif Function_selection == "3":
        print("")
        print("现在是生成高强度密码模式")
        pwl = input("请输入密码长度（必须为整数，建议8-16位，由于是不规则的，所以建议把密码记下来！）：")
        print("正在生成，请等待……")
        pw = ''.join(random.sample(["A","B","C","D","E","F","G","H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%","^","&","*","(",")","0","1","2","3","4","5","6","7","8","9"], int(pwl)))
        sleep(1)
        print("生成完毕！")
        print("高强度密码为：",pw)
        sleep(1)
        print("")

    #生成随机浮点数部分
    elif Function_selection == "4":
        print("")
        print("现在是生成随机浮点数模式")
        fp_min = input("请输入随机浮点数的最小值(必须为整数)：")
        fp_max = input("请输入随机浮点数的最大值(必须为整数)：")
        print("正在生成，请等待……")
        fp_random = random.uniform(int(fp_min), int(fp_max))
        sleep(1)
        print("生成完毕！")
        print("随机数字为：",fp_random)
        sleep(1)
        print("")

    #列出一个范围内的素数
    elif Function_selection == "5":
        print("")
        print("现在是列出一个范围内的素数模式")
        range_max = input("请输入一个数字作为范围最大值（用于从0到这个数字中的素数）：")
        p_n=[]
        for x in range(int(range_max)):
            if x<2:
                continue
            for i in range(2,x):
                if x%i==0:
                    break
            else:
                p_n.append(x)
        print(range_max,"以内的全部素数有：",p_n)
        sleep(1)
        print("")

    #过滤特定文本部分
    elif Function_selection == "6":
        print("")
        print("现在是过滤特定文本模式，请选择子模块")
        sleep(1)
        #子模块部分

        print("从字符串中提取汉字输入1\n从字符串中提取数字输入2\n从字符串中提取字母输入3\n退出此模块输入exit")
        sub_m = input("请选择子模块：")
        #子循环
        while True:

        #子判断

            #保留汉字部分
            if sub_m == "1":
                print("")
                print("现在是保留汉字模式")
                text = input("请输入文本：")
                cn_text = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", text)
                print(cn_text)
                sleep(1)
                print("")
                print("从字符串中提取汉字输入1\n从字符串中提取数字输入2\n从字符串中提取字母输入3\n退出此模块输入exit")
                sub_m = input("请选择子模块：")

            #保留数字部分
            elif sub_m == "2":
                print("")
                print("现在是保留数字模式")
                text = input("请输入文本：")
                num_text = re.sub("\D", "", text) 
                print(num_text)
                sleep(1)
                print("")
                print("从字符串中提取汉字输入1\n从字符串中提取数字输入2\n从字符串中提取字母输入3\n退出此模块输入exit")
                sub_m = input("请选择子模块：")

            #保留字母部分
            elif sub_m == "3":
                print("")
                print("现在是保留字母模式")
                text = input("请输入文本：")
                en_text = ''.join(re.findall(r'[A-Za-z]', text)) 
                print(en_text)
                sleep(1)
                print("")
                print("从字符串中提取汉字输入1\n从字符串中提取数字输入2\n从字符串中提取字母输入3\n退出此模块输入exit")
                sub_m = input("请选择子模块：")

            #退出
            elif sub_m == "exit":
                print("正在退出模块")
                print("")
                sleep(1)
                Function_selection = "0"
                break

            #无法理解
            else:
                print("无法理解你输入的内容，仔细检查一下是不是输入错了？")
                sleep(1)
                print("")
                print("从字符串中提取汉字输入1\n从字符串中提取数字输入2\n从字符串中提取字母输入3\n退出此模块输入exit")
                sub_m = input("请选择子模块：")

    #校检身份证号码部分
    elif Function_selection == "7":
        print("")
        print("现在是校检身份证号码模式")
        card = input("请输入身份证号码：")
        id_card.check(card)
        sleep(1)
        print("")

    #help部分
    elif Function_selection == "help":
        print("")
        print("现在是帮助模式")
        print("#生成随机字符的功能：生成一个随机大写字母、随机小写字母和随机整数的组合，长度由用户自定义")
        print("#生成随机数字的功能：生成一个随机整数，范围由用户自定义")
        print("#生成高强度密码的功能：生成一个由随机大写字母、随机小写字母、随机整数、随机符号组成的字符串，范围由用户自定义，非常适合用来当密码（当然你自己要记下来）")
        print("#生成随机浮点数部分：生成一个随机小数，范围由用户自定义")
        print("#列出一个范围内的素数部分：计算一个范围内的全部素数，范围由用户自定义")
        print("#过滤特定文本部分：提取一段文本当中的特定字符（目前支持汉字、数字以及英文字母），文本由用户自定义")
        print("#校检身份证号码：校检用户输入的身份证号码是否正确，目前只支持校检第二代18位身份证")
        print("！！！注意：以上模块在要求输入数字时，请不要输入过大的数字，容易崩溃！目前还没有技术进行优化，抱歉！！！")
        print("")
        print("作者：Abyss，我会在我的博客公布源代码和打包后的exe文件，持续更新，更新内容请留意我的博客！")
        print("当前版本号：v3.0")
        print("“文本操作工具”博客专栏：https://blog.nocsi.xyz/category/str_tool")
        print("本次更新内容：身份证校检模块的部分始终让我不满意，在制作v3.0时，我花费了大量的时间和精力去研究，最后只好选择了最懒（也是最有效）的方法——调库。我使用了id_validator，根据库的功能自己修改了一下id_card库的代码\n目前支持18位身份证和15位身份证（港澳台的也行）的校检和提取身份证信息")
        print("")
        print("感谢支持！有问题请在博客内反馈！")
        sleep(1)
        print("")

    #退出程序
    elif Function_selection == "exit":
        print("正在退出程序……")
        sleep(1)
        break

    #重定
    elif Function_selection == "0":
        break

    #无法判断
    else:
        print("无法理解你输入的内容，仔细检查一下是不是输入错了？")
        sleep(1)
        print("")

    #重新进行功能选择
    Function_selection = input("生成随机字符输入1\n生成随机数字输入2\n生成高强度密码输入3\n生成随机浮点数输入4\n列出一个范围内的素数输入5\n过滤特定文本输入6\n校检身份证号码输入7\n查看帮助输入help\n退出输入exit：")

#感谢支持！！！