import rule_config

test_num=rule_config.test_num

for T in range(1,test_num+1):
    rule_config.Generate(open(str(T)+".in","w"))