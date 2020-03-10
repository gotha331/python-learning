# io.StringIO

import io

s = "hello,sust"
sio = io.StringIO(s)
print(sio)
print(sio.getvalue())
sio.seek(7)  # 让指针移动到sio的指定位置
sio.write('BBBBB')
print(sio.getvalue())   # hello,sBBBBB
