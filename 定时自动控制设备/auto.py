# -*- coding: utf-8 -*-
import datetime
import json
import time
import requests
import schedule

# 自动处理cookie，下一次请求会带上前一次的cookie,保持会话状态
session = requests.session()
# headers头部标识
headers = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}
# 传参
data = {
    'username': '111',  # 运行前请修改账号密码
    'password': '111'  # 运行前请修改账号密码
}
# 自动处理的网址
url = '#'  # 运行前请填写url
# 利用session 的post请求将参数传到URL中，
esp = session.post(url, data=data, headers=headers)
# 打印登录成功
print(esp.text)

# 所有需要控制的设备ID
list_id = {
    '245dfc6469f847cd8a47cadcaaac101021',
    '245dfc6469f347cd8abcca6b2fac101021',
    '245dfc6469f947cd8a47821b2aac101021',
    '245dfc646d5747cd8afd4fe5ceac101021',
    '245dfc6469f447cd8abcc7a10bac101021',
    '245dfc6469f747cd8ac11724b8ac101021',
    '245dfc63f87e47cd8abcc8ceddac101021'
}
# 开机状态
data = {
    'terminalIds': list_id,
    'password': '0',
    'power': '1'
}
# 休眠状态
data2 = {
    'terminalIds': list_id,
    'password': '0',
    'power': '2'
}


# 定义函数工作时
def working():
    work_url = '#'  # 运行前请填写url
    work = session.post(work_url, data=data)  # 将执行开机状态
    print("上班啦")


# 定义函数下班时
def closed_off():
    closed_url = '#'  # 运行前请填写url
    closed = session.post(closed_url, data=data2)  # 将执行休眠状态
    print("下班啦")


# 定义函数放假时
def holidays():
    holidays_url = '#'  # 运行前请填写url
    hd = session.post(holidays_url, data=data2)  # 将执行休眠状态
    print("放假啦")


def time_conlose():
    # 放假时间列表
    f = open('data.txt')
    file = f.read()
    print(file)
    # 当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    # 判断当前日期时候为 上方 week列表中，存在则执行holidays放假，不存在则执行working上班
    if now in file:
        print("放假时间")
        return holidays()
    else:
        print("上班啦！")
        return working()


# 主函数启动
if __name__ == '__main__':

    time_conlose()
    # 定时器，每天指定时间执行指定函数
    schedule.every().day.at('08:50').do(working)

    schedule.every().day.at('12:00').do(closed_off)

    schedule.every().day.at('13:30').do(working)

    schedule.every().day.at('20:00').do(closed_off)

    while True:
        schedule.run_pending()
        time.sleep(2)
