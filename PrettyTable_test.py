import prettytable as pt
import time
## 按行添加数据
tb = pt.PrettyTable()
tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
tb.add_row(["Adelaide",1295, 1158259, 600.5])
tb.add_row(["Brisbane",5905, 1857594, 1146.4])
tb.add_row(["Darwin", 112, 120900, 1714.7])
tb.add_row(["Hobart", 1357, 205556,619.5])

print(tb)

##
time.sleep(1)
tb.add_column('index',[1,2,3,4])
print(tb)

## 使用不同的输出风格
time.sleep(1)
tb.set_style(pt.MSWORD_FRIENDLY)
#print('--- style：MSWORD_FRIENDLY -----')
#print(tb)

#time.sleep(1)
## 可以只获取指定列或行
#s = tb.get_string(fields=["City name", "Population"],start=1,end=4)
#print(s)

## 自定义表格输出样式
### 设定左对齐
#tb.align = 'l'
### 设定数字输出格式
#tb.float_format = "2.2"
### 设定边框连接符为'*"
#tb.junction_char = "*"
### 设定排序方式
#tb.sortby = "City name"
### 设定左侧不填充空白字符
#tb.left_padding_width = 0

## 不显示边框
#tb.border = 0
#print(tb)

## 修改边框分隔符
#tb.set_style(pt.DEFAULT)
#tb.horizontal_char = '&'
#print(tb)

## prettytable也支持输出HTML代码
s = tb.get_html_string()
print(s)
