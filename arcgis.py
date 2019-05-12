import shutil,os
from tqdm import tqdm
import re


#处理
def getInt(str):
    ss = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", str[1:])
    return int(ss,16)

#拷贝文件 zxy目录结构
def getTileFile(sourceDir,targetDir):
    #创建目标目录文件
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
        print("............创建目标文件夹...............")
    for (index, file) in enumerate(os.listdir(sourceDir)):
        levelPath = targetDir + os.path.sep+ str(int(file[1:]))  # 各等级目录
        # 创建等级目录
        if not os.path.exists(levelPath):
            os.makedirs(levelPath)

        #处理各个等级下的文件
        rowDirPath = sourceDir+os.path.sep+file
        for rowfile in tqdm(os.listdir(rowDirPath)):
            y = getInt(rowfile)
            #处理该个等级下row文件
            colDirPath = rowDirPath+os.path.sep+rowfile
            for colfile in os.listdir(colDirPath):
                x = getInt(colfile.split(".")[0])
                #创建x目录
                xpath = levelPath+os.path.sep+str(x)
                if not os.path.exists(xpath):
                    os.mkdir(xpath)
                #拷贝文件
                if not os.path.exists(os.path.join(xpath,(str(y)+".png"))):
                    shutil.copy(os.path.join(colDirPath,colfile),os.path.join(xpath,(str(y)+".png")))
        print(end="\r")
        print("...................%d等级文件拷贝完成..................." % (index))
    print('................全部下载转换完成.....................')
    return


# zyx目录结构
def getZYX(sourceDir,targetDir):
    # 创建目标目录文件
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
        print("............创建目标文件夹...............")
    for (index, file) in enumerate(os.listdir(sourceDir)):
        levelPath = targetDir + os.path.sep + str(int(file[1:]))  # 各等级目录
        # 创建等级目录
        if not os.path.exists(levelPath):
            os.makedirs(levelPath)

        # 处理各个等级下的文件
        rowDirPath = sourceDir + os.path.sep + file
        for rowfile in tqdm(os.listdir(rowDirPath)):
            y = getInt(rowfile)
            #创建y目录
            ypath = levelPath + os.path.sep+ str(y)
            if not os.path.exists(ypath):
                os.mkdir(ypath)
            # 处理该个等级下row文件
            colDirPath = rowDirPath + os.path.sep + rowfile
            for colfile in os.listdir(colDirPath):
                x = getInt(colfile.split(".")[0])
                # 拷贝文件
                if not os.path.exists(os.path.join(ypath, (str(x) + ".png"))):
                    shutil.copy(os.path.join(colDirPath, colfile), os.path.join(ypath, (str(x) + ".png")))
        print(end="\r")
        print("...................%d等级文件拷贝完成..................." % (index))
    print('................全部下载转换完成.....................')
    return

    # print(level)


if __name__ == '__main__':
    # getFile("E:\\NodeLearning\\apache-tomcat-8.0.52-gis-8081\\webapps\\geoserver\\data\\data\\Tile\\webgis_nl3857","E:\\mapdata\\nanle\\tb")
    getTileFile("C:\\arcgisserver\\directories\\arcgiscache\\nanle_dlbtpng\\图层\\_alllayers","E:\\mapdata\\nanle\\testarcgis")
    #getZYX("C:\\arcgisserver\\directories\\arcgiscache\\nanle_dlbtpng\\图层\\_alllayers","E:\\mapdata\\nanle\\testarcgiszyx")