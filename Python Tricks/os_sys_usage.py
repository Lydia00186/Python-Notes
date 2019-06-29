'''
os:   This module provides a portable way of using operating system dependent
      functionality.

sys:  This module provides access to some variables used or maintained by the
      interpreter and to functions that interact strongly with the interpreter.

glob: The glob module finds all the pathnames matching a specified pattern
      according to the rules used by the Unix shell, although results are
      returned in arbitrary order. No tilde expansion is done, but *, ?,
      and character ranges expressed with [] will be correctly matched.

from https://docs.python.org/3/library
'''

'''
os.remove() => delete the file
os.rename() => rename the file
os.chdir() => change the path to 
os.mkdir/makedirs 创建目录/多层目录
os.rmdir/removedirs 删除目录/多层目录
os.listdir() 列出指定目录的文件
os.getcwd() 取得当前工作目录
os.chmod() 改变目录权限
os.path.basename() 去掉目录路径，返回文件名
os.path.dirname() 去掉文件名，返回目录路径
os.path.join() 将分离的各部分组合成一个路径名
os.path.split() 返回( dirname(), basename())元组
os.path.splitext() 返回 (filename, extension) 元组
os.path.getatime\ctime\mtime 分别返回最近访问、创建、修改时间
os.path.getsize() 返回文件大小
os.path.exists() 是否存在
os.path.isabs() 是否为绝对路径
os.path.isdir() 是否为目录
os.path.isfile() 是否为文件
sys 常用方法
sys.argv 命令行参数List，第一个元素是程序本身路径
sys.modules.keys() 返回所有已经导入的模块列表
sys.exc_info() 获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
sys.exit(n) 退出程序，正常退出时exit(0)
sys.hexversion 获取Python解释程序的版本值，16进制格式如：0x020403F0
sys.version 获取Python解释程序的版本信息
sys.maxint 最大的Int值
sys.maxunicode 最大的Unicode值
sys.modules 返回系统导入的模块字段，key是模块名，value是模块
sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform 返回操作系统平台名称
sys.stdout 标准输出
sys.stdin 标准输入
sys.stderr 错误输出
sys.exc_clear() 用来清除当前线程所出现的当前的或最近的错误信息
sys.exec_prefix 返回平台独立的python文件安装的位置
sys.byteorder 本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
sys.copyright 记录python版权相关的东西
sys.api_version 解释器的C的API版本
总结：
os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;
sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境。
'''

import os,glob
import sys


def Programme_1():
    '''
    Find certain files of the folder
    Example: find csv files under the file location
    Similarly we can find figures, xlxs, word files in this way
    '''
    # os.chdir('D:/Uni due/Programming/Python/Python projects/Data Analysis/Douban-Movie-TOP250')
    os.chdir('D:/Uni due/Programming/Python/Python projects/Data Analysis')
    # os.chdir => change path to some folder
    for file in glob.glob('*/*.csv'): # find csv files under this folder
        print(file)

def Programme_2():
    '''
    create a new file
    '''
    pass




if __name__=='__main__':
    Programme_1()
