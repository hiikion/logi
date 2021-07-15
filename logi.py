import os

class logi:

    def __init__(self, path, timestamp):
        self.path = path
        self.timestamp = timestamp

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

    def Error(self, m):
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

    def Warning(self, m):
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
