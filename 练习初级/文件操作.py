fs=open("E:/Python合/账单.txt","r",encoding="UTF-8")
fc=open("E:/Python合/账单COPY.txt","w",encoding="UTF-8")
for line in fs:
    line=line.strip()
    #print(line)
    if line.strip(",")[4]=="测试":
        continue
    fc.write(line)
    fc.write("\n")
    print(line)
fs.close()
fc.close()



