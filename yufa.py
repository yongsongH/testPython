'''
Created on 2016-4-15

@author: hys mac
'''
#coding:utf8

word='abcdefg' 
a=word[2] 
print ('a is: '+a) 
b=word[1:3] 
print ("b is: "+b) # index 1 and 2 elements of word. 
c=word[:2] 
print ("c is: "+c) # index 0 and 1 elements of word. 
d=word[0:] 
print ("d is: "+d) # All elements of word. 
e=word[:2]+word[2:] 
print ("e is: "+e) # All elements of word. 
f=word[-1] 
print ("f is: "+f) # The last elements of word. 
g=word[-4:-2] 
print ("g is: "+g) # index 3 and 4 elements of word. 
h=word[-2:] 
print ("h is: "+h) # The last two elements. 
i=word[:-2] 
print ("i is: "+i) # Everything except the last two characters 
l=len(word) 
print ("Length of word is: "+ str(l)) 


#中文和英文的字符串长度是否一样? 

#复制代码 代码如下:


#! /usr/bin/python 

s=input("输入你的中文名,按回车继续"); 
print ("你的名字是 : " +s) 
l=len(s) 
print ("你中文名字的长度是:"+str(l)) 
print( )


test_D = {a,d,c,f,'PapayaWhip'}

print ('PapayaWhip' in test_D)
print( )
print('x' in test_D  or 'y' in test_D )#运算符or的优先级高于运算符in，所以这里不需要添加括号。

    