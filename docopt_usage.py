"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
-x
--xxx
[]
代表可选的元素，方括号内的元素可有可无

()
代表必须要有的元素，括号内的元素必须要有，哪怕是多个里面选一个。

|
互斥的元素，竖线两旁的元素只能有一个留下

…
代表元素可以重复出现，最后解析的结果是一个列表

[options]
 指定特定的选项，完成特定的任务。
"""
from docopt import docopt

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    print(arguments)

if __name__ == '__main__':
    cli()
