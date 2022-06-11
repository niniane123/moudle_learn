import time

# 元组(struct_time)共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同
# mac上:time.struct_time(tm_year=2020, tm_mon=4, tm_mday=10, tm_hour=2, tm_min=53, tm_sec=15, tm_wday=2,tm_yday=100, tm_isdst=o)

# time.localtime([secs]):将一个时间戳转换为当前时区的struct_time(元组类类型)。若secs参数未提供，则以当前时间为准。
localtime = time.localtime()
# <class 'time.struct_time'>
print(type(localtime))

# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=10, tm_hour=18, tm_min=57, tm_sec=37, tm_wday=4, tm_yday=161, tm_isdst=0)
print(localtime)
