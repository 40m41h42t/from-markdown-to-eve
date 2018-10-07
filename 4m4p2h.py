# -*- coding:utf-8 -*-


FILEPATH = 'samples/test.md'
with open(FILEPATH, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        # 对每一行进行分析
        print(line)