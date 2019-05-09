#  geoserverToTMS-ZXY目录结构

 1、 把geoserver的服务切片编号规则，转成通用的zxy目录层级，方便脱离geoserver离线部署。（pbf文件）

 2、 geoserver服务切片编号规则如下图：
![image](https://github.com/JerckyLY/geoserverToTMS/blob/master/images/1.png)

 3、 使用方式
修改geoserver.py中的文件地址为自己的文件目录地址。

 4、 运行结果
![image](https://github.com/JerckyLY/geoserverToTMS/blob/master/images/2.png)

 5、 nginx代理，用mapbox加载显示效果
![image](https://github.com/JerckyLY/geoserverToTMS/blob/master/images/4.png)

 6、 代码新增进度条
