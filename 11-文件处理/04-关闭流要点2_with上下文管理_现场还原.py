# with关键字（上下文管理器）可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，并且可以在代码块执行完毕后自动还原进入该代码块时的现场。

with open(r"d.txt", "a") as f:
    f.write('shuaishuai aini ')
