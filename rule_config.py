import random
test_num=25 #测试点数量设置

def Generate(outfile): #测试点生成规则，outfile是一个文件，把数据可以通过write的方式写入文件
    n=100000
    outfile.write(str(n)+"\n")
    s=""
    for i in range(1,int(n/5+1)):
        s=s+str(random.randint(1,1000000))+" "
    outfile.write(s+s+s+s+s)
    outfile.write("\n")
