from PIL import Image
import glob


'''
glob方法（返回列表）：
glob模块的主要方法就是glob,该方法返回所有匹配的文件路径列表（list）；该方法需要一个参数用来指定匹配的路径字符串（字符串可以为绝对路径也可以为相对路径），其返回的文件名只包括当前目录里的文件名，不包括子文件夹里的文件。

比如：

glob.glob(r’c:*.txt’)

我这里就是获得C盘下的所有txt文件

glob.glob(r’E:\pic**.jpg’)

获得指定目录下的所有jpg文件

使用相对路径：

glob.glob(r’../*.py’)
'''