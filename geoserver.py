import shutil,os
from tqdm import tqdm
#处理下划线命名
def handlePath(fileName):
    brr = []
    arr = fileName.split("_")
    brr.append(str(int(arr[0])))
    brr.append(str(int(arr[1].split(".")[0])))
    return brr
#拷贝文件
def getFile(sourceDir,targetDir):
    #创建目标目录文件
    if not os.path.isdir(targetDir):
        os.makedirs(targetDir)
        print("............创建目标文件夹...............")
    lastxpath =""
    # 第一级目录
    for (index, file) in enumerate(os.listdir(sourceDir)):
        itempath = targetDir +"\\"+str(int(file.split("_")[1]))  #各等级目录
        #创建等级目录
        if not os.path.isdir(itempath):
            os.makedirs(itempath)
        # 各个等级下的目录，既直接包含pbf的目录
        souritemdir = sourceDir+"\\"+file+"\\"+os.listdir(sourceDir+"\\"+file)[0]
        #遍历目录下的所有文件
        for childfile in tqdm(os.listdir(souritemdir)):
            #不是pdf文件格式的直接跳过
            if(childfile.split(".")[1] !="pbf"):
                continue
            #处理文件名。获取x,y
            rowN = handlePath(childfile)[0] #x序号
            colN = handlePath(childfile)[1] #y序号
            #创建x层目录
            xpath =itempath + "\\" + rowN  # x 目录
            if not os.path.isdir(xpath):
                os.makedirs(xpath)

            #处理拷贝文件 处理同一x层文件
            if(lastxpath == "" or lastxpath == rowN):
                shutil.copy(os.path.join(souritemdir,childfile),os.path.join(xpath,(colN+".pbf")))
                lastxpath = rowN
            #拷贝不同X层文件
            elif(lastxpath != rowN):
                shutil.copy(os.path.join(souritemdir,childfile),os.path.join(xpath,(colN+".pbf")))
                lastxpath = rowN
        print(end="\r")
        print("...................%d等级文件拷贝完成..................."%(index))

    # print(level)


if __name__ == '__main__':
    getFile("E:\\NodeLearning\\apache-tomcat-8.0.52-gis-8081\\webapps\\geoserver\\data\\data\\Tile\\webgis_DLTB_3857","E:\\mapdata\\geoserver\\xingyang1")
