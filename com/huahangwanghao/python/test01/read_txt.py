#coding:utf-8
import smtplib
from email.mime.text import  MIMEText
from email.header import  Header


'''
ASCII编码   A  65  10001010
GB2312   慕  课  网  中国的
shift_JIS           日本的
unicode编码: 包含了全世界所有的文字信息
    慕 62   (日本字) 是  32  不冲突
        ASCII编码        Unicode编码  
A        01000001        00000000 01000001


        ASCII编码        utf-8编码(8位来存储英文字符和常用的字符)  
A        01000001        01000001


这样看来使用utf-8存储可以最大的节省空间, 使用Unicode编码展示可以最大程度的兼容.


'''