# arcgisToTMS
用python把arcgis切片目录规则转成tms--zxy目录规则

## 使用说明
1、 在代码中，getTileFile()这个函数是把arcgis切片规则转成zxy目录层级， getZYX是转成zyx，两种转换方式，使用的时候注意加载顺序即可； 同时arcgis切片规则是按照google的tms规则的，切片源点是在左上角，所以用mapbox或者leaflet加载时，不要写成tms类型的。
