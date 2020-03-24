''' 读取xml文件，分别生成trainval.txt,train.txt,test.txt,val.txt'''

import os
import random

trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'data/Annotations'  # xml文件
txtsavepath = 'data/ImageSets'  # 生成的训练集，测试集，验证集位置
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data/ImageSets/trainval.txt', 'w')
ftest = open('data/ImageSets/test.txt', 'w')  # 生成测试集
ftrain = open('data/ImageSets/train.txt', 'w')  # 生成训练集
fval = open('data/ImageSets/val.txt', 'w')  # 生成验证集

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()