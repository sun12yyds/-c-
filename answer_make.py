from rule_config import test_num #get config
import os,runpy

'''
on Linux/macOS
'''

print("Generate test data...",end="")

runpy.run_module("input_make")
print("Done")

print("Generate answer")

if(os.system("g++ std.cpp -o std.o")!=0): #Compile
    print("Compile Error")
    exit(-1)

ans={}

for T in range(1,test_num+1):
    if(os.system("time ./std.o > "+str(T)+".out < "+str(T)+".in")!=0): #run
        print("Runtime Error")
        exit(-1)
    else:
        ans[open(str(T)+".out","r").read()]=1

print("Success")
print()
print("Calculate the similarity of the standard answers: ")
print(str(len(ans))+"/"+str(test_num))
print("%.4f" % ((1-len(ans)/test_num)*100),end="")
exit(0)
