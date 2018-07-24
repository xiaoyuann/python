# find() python

## [欢迎关注本人博客：云端筑梦师](http://www.cnblogs.com/Aurora-Twinkle)

**描述**
find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

**语法**

`str.find(str, beg=0, end=len(string))`

**参数**

- str -- 需要检索的字符串
- beg -- 起始索引，默认值为0
- end -- 结束索引，默认为字符串长度

**返回值**

如果找到子字符串则返回开始索引，否则返回-1

**实例**

示例代码：
``` python
#!/usr/bin/python3
 
str1 = "Runoob example....wow!!!"
str2 = "exam";
 
print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))
```
返回：

>7

>7

>-1

``` python
>>>info = 'abca'
>>> print(info.find('a'))      # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
0
>>> print(info.find('a', 1))   # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
3
>>> print(info.find('3'))      # 查找不到返回-1
-1
>>>
```