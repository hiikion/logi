import os
import time

class logi:

    def __init__(self, path, timestamp, dbg):
        self.path = path
        self.timestamp = timestamp
        self.dbg = dbg

    def info(self, m):
        self.m = m
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if not os.path.exists(self.path):
            op = open(self.path, 'w')
            op.close()
        cg = open(self.path, 'r')
        content = cg.read()
        cg.close()
        with open(self.path, 'w') as log:
            if self.timestamp == True:
                log.write(content)
                log.write('\n' + current_time)
                log.write(' | info | ')
                log.write(self.m)
                log.close()
            else:
                log.write('| info | ')
                log.write(self.m)
                log.close()

    def error(self, m):
        self.m = m
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if not os.path.exists(self.path):
            op = open(self.path, 'w')
            op.close()
        cg = open(self.path, 'r')
        content = cg.read()
        cg.close()
        with open(self.path, 'w') as log:
            if self.timestamp == True:
                log.write(content)
                log.write('\n' + current_time)
                log.write(' | Error | ')
                log.write(self.m)
                log.close()
            else:
                log.write('| Error | ')
                log.write(self.m)
                log.close()

    def warning(self, m):
        self.m = m
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if not os.path.exists(self.path):
            op = open(self.path, 'w')
            op.close()
        cg = open(self.path, 'r')
        content = cg.read()
        cg.close()
        with open(self.path, 'w') as log:
            if self.timestamp == True:
                log.write(content)
                log.write('\n' + current_time)
                log.write(' | Warning | ')
                log.write(self.m)
                log.close()
            else:
                log.write('| Warning | ')
                log.write(self.m)
                log.close()

    def custom(self, m, cust):
        self.m = m
        self.cust = cust
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if not os.path.exists(self.path):
            op = open(self.path, 'w')
            op.close()
        cg = open(self.path, 'r')
        content = cg.read()
        cg.close()
        with open(self.path, 'w') as log:
            if self.timestamp == True:
                log.write(content)
                log.write('\n' + current_time)
                log.write(' | ')
                log.write(self.cust)
                log.write(' | ')
                log.write(self.m)
                log.close()
            else:
                log.write(' | ')
                log.write(self.cust)
                log.write(' | ')
                log.write(self.m)
                log.close()

    def clear_all(self):
        try:
            with open(self.path, 'w') as log:
                log.write('')
                log.close()
        except:
            print('logi error: file does not exist')

    def debug(self, m):
        self.m = m
        if self.dbg == True:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            if not os.path.exists(self.path):
                op = open(self.path, 'w')
                op.close()
            cg = open(self.path, 'r')
            content = cg.read()
            cg.close()
            with open(self.path, 'w') as log:
                if self.timestamp == True:
                    log.write(content)
                    log.write('\n' + current_time)
                    log.write(' | Debug | ')
                    log.write(self.m)
                    log.close()
                else:
                    log.write('| Debug | ')
                    log.write(self.m)
                    log.close()
