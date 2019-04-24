import shutil,os

#处理下划线命名
def handlePath(fileName):
    brr = []
    arr = fileName.split("_")
    brr.append(str(int(arr[0])))
    brr.append(str(int(arr[1].split(".")[0])))
    return brr
#拷贝文件
def getFile(sourceDir,targetDir):
    lastxpath =""
    # 第一级目录
    for file in os.listdir(sourceDir):
        itempath = targetDir +"\\"+str(int(file.split("_")[1]))  #新文件子目录
        #创建目录
        if not os.path.isdir(itempath):
            os.makedirs(itempath)
        souritemdir = sourceDir+"\\"+file+"\\"+os.listdir(sourceDir+"\\"+file)[0]   #源文件目录
        for childfile in os.listdir(souritemdir):
            if(childfile.split(".")[1] !="pbf"):
                continue
            rowN = handlePath(childfile)[0] #x序号
            colN = handlePath(childfile)[1] #y序号
            xpath =itempath + "\\" + rowN  # x 目录
            if not os.path.isdir(xpath):
                os.makedirs(xpath)

            #处理拷贝文件
            if(lastxpath == "" or lastxpath == rowN):
                shutil.copy(os.path.join(souritemdir,childfile),os.path.join(xpath,(colN+".pbf")))
                lastxpath = rowN
            elif(lastxpath != rowN):
                shutil.copy(os.path.join(souritemdir,childfile),os.path.join(xpath,(colN+".pbf")))
                lastxpath = rowN

    # print(level)


if __name__ == '__main__':
    getFile("E:\\NodeLearning\\apache-tomcat-8.0.52-gis-8081\\webapps\\geoserver\\data\\data\\Tile\\webgis_DLTB_3857","E:\\mapdata\\geoserver\\xingyang")