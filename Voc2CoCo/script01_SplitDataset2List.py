# coding: utf-8
#splits data into test and training sets
import os
import math
import random
import shutil

def main():
    '''
    按照比例，将数据集拆分成训练集、验证集和测试集
    '''
    print('Split train val and test sets')
    image_path = os.path.join("JPEGImages")
    Annotations_path = os.path.join("Annotations")
    train_path = os.path.join("Train2007")
    test_path = os.path.join("Test2007")
    val_path = os.path.join("Val2007")
    imageArr = [x for x in os.listdir(image_path) if x.endswith('.jpg')]
    random.shuffle(imageArr)
    
    #shuffle array
    random.shuffle(imageArr)
    percentageTrain = 0.85
    percentageVal = 0.05
    percentageTest = 0.1

    trainFileNumber = int(len(imageArr) * percentageTrain)
    valFileNumber = int(len(imageArr) * percentageVal)
    #testFileNumber = int(len(imageArr) * percentageTest)

    fdTrain = open("list_train.txt",'w')
    fdTest = open("list_test.txt",'w')
    fdVal = open("list_val.txt",'w')

    for i in range(len(imageArr)):
        if i < trainFileNumber:
            fdTrain.write('%s\n' %(imageArr[i]))
            shutil.move(os.path.join(image_path, imageArr[i]), train_path)
            shutil.move(os.path.join(Annotations_path, imageArr[i].replace("jpg","xml")), train_path)
        elif i >= trainFileNumber and i <trainFileNumber+valFileNumber: 
            fdVal.write('%s\n' %(imageArr[i])) 
            shutil.move(os.path.join(image_path, imageArr[i]), val_path)
            shutil.move(os.path.join(Annotations_path, imageArr[i].replace("jpg","xml")), val_path)
        else: 
            fdTest.write('%s\n' %(imageArr[i]))  
            shutil.move(os.path.join(image_path, imageArr[i]), test_path) 
            shutil.move(os.path.join(Annotations_path, imageArr[i].replace("jpg","xml")), test_path) 
    fdTrain.close()
    fdVal.close()  
    fdTest.close()

main()
