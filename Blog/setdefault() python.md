## [欢迎关注本人博客：云端筑梦师](http://www.cnblogs.com/Aurora-Twinkle/)

**描述**

Python 字典 setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。

**语法**

`dict.setdefault(key, default=None)`

**参数**

- key -- 要查找的关键字
- default -- 键不存在时，设置的默认键值

**返回值**

如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。

**实例**

示例代码：
``` python
#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7}

print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
print ("新字典为：", dict)
```
输出：
``` python
Age 键的值为 : 7
Sex 键的值为 : None
新字典为： {'Age': 7, 'Name': 'Runoob', 'Sex': None}
```