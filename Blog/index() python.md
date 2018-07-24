# index() python
## [欢迎关注本人博客：云端筑梦师](http://www.cnblogs.com/Aurora-Twinkle)

**描述**

index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

**语法**

`str.index(str, beg=0, end=len(string))`

**参数**

- str -- 指定要检索的字符串
- beg -- 起始索引，默认为0
- end -- 结束索引，默认为字符串长度

**返回值**

如果子字符串存在则返回第一个索引，否则报错

**实例**

示例代码：
``` python
#!/usr/bin/python3

str1 = "Runoob example....wow!!!"
str2 = "exam";

print (str1.index(str2))
print (str1.index(str2, 5))
print (str1.index(str2, 10))
```
输出：
``` python
7
7
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print (str1.index(str2, 10))
ValueError: substring not found
```