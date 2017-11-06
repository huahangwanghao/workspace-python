import re
#正则表达式
f=open("re.txt",'r',encoding='utf-8')
for line in f.readlines():
    if line.startswith("immoc") and line[:-1].endswith("immoc"):
#        print(line)
        i=1

str1='immoc python'
print(str1.find("o"))
#print(str1.startswith("immoc"))

pa=re.compile(r"o")
result=pa.match(str1)





ma=re.match(r"immoc","immoc python")
print("group",ma.group())


ma=re.match(r"(immoc)","immoc python")
print("groups",ma.groups())



#-------------------------------------------------------------
rm=re.match(r"{.}",'{d}')
print(rm.group())

rm=re.match(r"{[abc]}","{c}")
if rm != None:
    print(rm.group())









