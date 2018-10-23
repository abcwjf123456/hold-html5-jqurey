import logging

# 等级修改
logging.basicConfig(
    level=logging.DEBUG,
    filename='loger.log',#将日志写入到loger.log文件中去为追加模式
    filemode='w',#将追加模式改为写模式，
    format='%(asctime)s %(lineno)d %(message)s'#将日志内容改为时间格式为%()s添加内容




)
# 修改等级后输出
# DEBUG:root:debug
# INFO:root:info
# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical









# 默认等级为warning所以输出结果为（只会输出大于或者等于warning的值）
# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')





# 高级用法（与吸星大法相似不懂有演示图截图）
loger=logging.getLogger()#创建loger对象

sh=logging.FileHandler('loderr.log')#将日志传到文件
ch=logging.StreamHandler()#将日志传到屏幕

fm=logging.Formatter('%(asctime)s %(message)s')#设置日志输出形式

sh.setFormatter(fm)#将设置日志输出形式规则给sh
ch.setFormatter(fm)#将设置日志输出形式规则给ch


loger.addHandler(sh)#得到sh
loger.addHandler(ch)#得到ch
loger.setLevel('DEBUG')#设置等级


#-----------------
loger.debug('debug')
loger.info('info')
loger.warning('warning')
loger.error('error')
loger.critical('critical')