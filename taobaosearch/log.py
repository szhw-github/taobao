def log(str):
   import time
   logpath = 'log/log.txt'
   with open(logpath, 'at', encoding='utf-8') as f:
      f.write(str)
      f.write('\n')
      f.write('{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
      f.write('\n\n')
      f.close()
