#coding:utf-8
import smtplib
from email.mime.text import  MIMEText
from email.header import  Header
# pdfminer3k
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import  PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

#获取文档对象
fp=open("testpdf.pdf","rb")
#创建一个与文档关联的解释器
parser=PDFParser(fp)

#创建一个PDF对象
doc=PDFDocument()

#把这个俩个关联起来
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档
doc.initialize("")

#创建pdf资源管理器
resource=PDFResourceManager()

#参数分析器
laparam=LAParams()

#创建一个聚合器
device=PDFPageAggregator(resource,laparams=laparam)

#创建一个PDF页面解释器
interpreter=PDFPageInterpreter(resource,device)

#使用文档对象 在文档读取内容
for page in doc.get_pages():
    #使用页面解析器来读取
    interpreter.process_page(page)

    #使用聚合去获取内容
    layout=device.get_result()

    for out in layout:
        if hasattr(out,"get_text"):
            print(out.get_text())