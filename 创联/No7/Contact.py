#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import pymysql


def connect():  # 连接数据库
    global connect
    global cursor
    connect = pymysql.connect('localhost', '', '', '', charset='utf8')
    cursor = connect.cursor()


def close():  # 关闭数据库
    cursor.close()
    connect.close()


def viewAll():  # 查看全部联系人
    cursor.execute('SELECT * FROM CONTACTS')
    connect.commit()
    print("%-6s%-10s%-14s%-5s%-5s%-10s" % ("编号", "姓名", "电话", "年龄", "性别", "地址"))
    result = cursor.fetchall()
    for row in result:
        results = []
        for col in row:
            results.append(col)
        print("%-6s%-10s%-14s%-5s%-5s%-10s" % (results[0], results[1], results[2], results[3], results[4], results[5]))


def addContact():  # 增加联系人
    print('---添加联系人---')

    RUNNING = True
    while RUNNING:  # 输入姓名
        name = input('姓名(按Esc退出):')
        if name == 'Esc':
            return
        elif name == '':
            print('姓名不能为空')
        else:
            RUNNING = False

    RUNNING = True
    while RUNNING:  # 输入电话
        phone = input('电话(按Esc退出):')
        if phone == 'Esc':
            return
        elif phone == '':
            print('电话不能为空')
        else:
            RUNNING = False

    RUNNING = True
    while RUNNING:  # 年龄
        age = input('年龄(按Esc退出):')
        if age == 'Esc':
            return
        elif age == '' or int(age) < 0 or int(age) > 110:
            print('请输入正确的年龄')
        else:
            RUNNING = False

    RUNNING = True
    while RUNNING:  # 性别
        sex = input('性别(按Esc退出):')
        if sex == 'Esc':
            return
        elif sex != '男' and sex != '女':
            print('请输入正确的性别(男或女)')
        else:
            RUNNING = False

    RUNNING = True
    while RUNNING:  # 地址
        address = input('地址(按Esc退出):')
        if address == 'Esc':
            return
        elif address == '':
            print('地址不能为空')
        else:
            RUNNING = False

    ADD = True
    cursor.execute('select Cname from contacts')  # 检查姓名是否重复
    for names in cursor.fetchall():
        if name in names:
            print('此姓名已存在')
            ADD = False

    cursor.execute('select PhoneNumber from contacts')  # 检查号码是否重复
    for phones in cursor.fetchall():
        if phone in phones:
            print('此电话已存在')
            ADD = False

    if ADD == True:
        values = [name, phone, age, sex, address]
        cursor.execute('insert into contacts(Cname,PhoneNumber,Cage,Csex,Caddress)\
        values(%s,%s,%s,%s,%s)', values)
        connect.commit()
        print('该联系人已经成功添加')


def deleteContact():  # 删除联系人
    print('---删除联系人---')
    deleteName = input('请输入联系人姓名(按Esc退出):')
    if deleteName == 'Esc':
        return
    result = cursor.execute('delete from contacts where Cname=%s', deleteName)
    if result == 1:
        print('删除成功')
    elif result == 0:
        print('未找到该联系人')


def modify():  # 修改联系人
    print('---修改联系人---')
    modify = True
    name = input('请输入要修改的联系人姓名(按Esc退出):')
    if name == 'Esc':
        return
    cursor.execute('select * from contacts where Cname = %s', name)
    print('编号  姓名  电话  年龄  性别  地址  ')
    for row in cursor.fetchall():
        result = ''
        for col in row:
            result = result + '\t' + str(col)
        if result == '':
            print('此联系人不存在')
            return
        print(result)
    while modify == True:
        print('请选择需要修改的部分:')
        choose = input('1.姓名 2.电话 3.年龄 4.性别 5.地址 6.退出修改\n')
        if choose == '1':
            newName = input('请输入新姓名:')
            cursor.execute("update contacts set Cname='%s' where Cname='%s'" % (newName, name))
            connect.commit()
            print('修改成功')
        elif choose == '2':
            newPhone = input('请输入新电话:')
            cursor.execute("update contacts set PhoneNumber=%s where Cname=%s" % (newPhone, name))
            connect.commit()
            print('修改成功')

        elif choose == '3':
            newAge = input('请输入新年龄:')
            cursor.execute("update contacts set Cage='%s' where Cname='%s'" % (newAge, name))
            connect.commit()
            print('修改成功')

        elif choose == '4':
            newSex = input('请输入新性别:')
            cursor.execute("update contacts set Csex='%s' where Cname='%s'" % (newSex, name))
            connect.commit()
            print('修改成功')

        elif choose == '5':
            newAddress = input('请输入新地址:')
            cursor.execute("update contacts set Caddress='%s' where Cname='%s'" % (newAddress, name))
            connect.commit()
            print('修改成功')

        elif choose == '6':
            modify = False


def search():  # 搜索联系人
    print('查找联系人')
    print('请选择查找条件:')
    condion = input('1.姓名 2.电话 3.地址\n')
    if condion == '1':
        name = input('请输入姓名或其中部分:')
        cursor.execute("select * from contacts where Cname like '%%%s%%'" % name)
    elif condion == '2':
        phone = input('请输入电话或者其中部分:')
        cursor.execute("select * from contacts where PhoneNumber like '%%%s%%'" % phone)
    elif condion == '3':
        address = input('请输入地址或者其中部分:')
        cursor.execute("select * from contacts where Caddress like '%%%s%%'" % address)
    connect.commit()
    print('编号  姓名  电话  年龄  性别  地址  ')
    for row in cursor.fetchall():
        result = ''
        for col in row:
            result = result + '\t' + str(col)
        print(result)


def main():
    print('---简易通讯录---')
    connect()
    running = True
    while running:
        print('请选择操作:')
        operation = input('1.展示全部联系人 2.添加联系人 3.删除联系人 4.查找联系人 5.修改联系人 6.退出\n')
        if operation == '1':
            viewAll()
        elif operation == '2':
            addContact()
        elif operation == '3':
            deleteContact()
        elif operation == '4':
            search()
        elif operation == '5':
            modify()
        elif operation == '6':
            running = False
        else:
            print('请输入1-6的数字')
    close()
    print('****************')


if __name__ == "__main__":
    main()