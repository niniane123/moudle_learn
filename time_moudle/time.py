import time

# 元组(struct_time)共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同
# mac上:time.struct_time(tm_year=2020, tm_mon=4, tm_mday=10, tm_hour=2, tm_min=53, tm_sec=15, tm_wday=2,tm_yday=100, tm_isdst=o)

# time.localtime([secs]):将一个时间戳转换为当前时区的struct_time(元组类类型)。若secs参数未提供，则以当前时间为准。
localtime = time.localtime()
# <class 'time.struct_time'>
print(type(localtime))

# time.time()返回当前时间的时间戳
print(time.time())

# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=10, tm_hour=18, tm_min=57, tm_sec=37, tm_wday=4, tm_yday=161, tm_isdst=0)
print(localtime)

# time.gmtime([secs]):和localtime()方法类似,gmtime()方法是将一个时间戳转换为UTC时区(O时区〉的struct_time。 time.time():返回当前时间的时间戳。
# 格林威治时间
print(time.gmtime())

# 将具体的日期元组转换为timestamp类型的时间戳
# time.mktime(t):将—个struct_time转化为时间戳。
print(time.mktime(localtime))

# 当前线程运行推迟指定的时间
# print(time.sleep(2))

print("Hello world")

# time.asctime([t]):把一个表示时间的元组或者struct_time表示为这种形式:‘Sun Oct 1 12:04:38 2019。如果没有参数，将会将time.localtime()作为参数传入。
# Sat Jun 11 14:10:04 2022，其实用的不多啊
print(time.asctime())

# time.ctime([secs]):把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
# Sat Jun 11 14:15:36 2022
print(time.ctime())

# ·time.strftime(formatl, t):把一个代表时间的元组或者struct_time(如由time.localtime()和time.gmtime()返回)转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。
# 重要：将时间元组转换为格式化的时间字符串
print(time.strftime("%y", time.localtime()))
print(time.strftime("%y-%m-%d-%h", time.localtime()))
print(time.strftime("%y-%m-%d-%h %H:%M", time.localtime()))

# time.strptime(stringl, format]):把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
# 举例: time.strptime('2017-10-3 17:54', "%Y-%m-%d %H:%M")#输出 time.struct_time(tm_year=2017,
# tm_mon=10, tm_mday=3, tm_hour=17, tm_min=54, tm_sec=0, tm_wday=1, tm_yday=276, tm_isdst=-1)
# %Y要大写不然报错是什么意思
print(time.strptime("2022/6/11 14:59", "%Y/%m/%d %H:%M"))
