通过Python3编写的出OI题用的测试点生成器

运行在Linux/macOS等unix平台下

其它平台需在answer_make.py修改代码

修改rule_config.py中的生成规则并将标准程序写入std.cpp

然后执行

python3 -u answer_make.py

生成测试数据为 .in/.out

在answer_make.py第15行中可以修改编译参数
这是转载于
