# logi docs
- <a href='https://github.com/hiikion/logi/blob/main/docs.md#home'>home</a>
- <a href='https://github.com/hiikion/logi/blob/main/docs.md#file-logging'>file logging</a>
- <a href='https://github.com/hiikion/logi/blob/main/docs.md#console-logging'>console logging</a>
- <a href='https://github.com/hiikion/logi/blob/main/docs.md#log-clear'>log clear</a>
- <a href='#'>log format</a>

## home

the import 
```python
from logi import logi
# or
from logi import *
```
otherwise it will not work

## file logging
the path can be only in this ```C:/logi/logi/test.log``` format <br>
NOT ```C:\logi\logi``` or ```C:\\logi\\logi```
examples what does the time stamp do are <a href='#'>here</a>
dbg turns <a href='#'>debug logs</a> on and off
```python
log = logi(path='C:/file path', timestamp=True, dbg=True)
```
#### info log
```python
log.info('info log')
```
#### warning log
```python
log.warning('warning log')
```
#### Error log
```python
log.error('Error log')
```
#### custom log
in custom log you can change the logs title <br>
and for example set it to hardware
```python
log.custom('custom log' cust='hardware')
```
#### debug log
logs in to the file only if dbg is true
```python
log.debug('debug log')
```
## console logging
its the same but the path can be what ever 
```python
log = logi(path='none', timestamp=True, dbg=True)
```
change the log type in ```type``` <br>
for example info, error, warning, debug etc (custom logs suported)
```python
log.console('console info log', type='info')
```
## log clear
clears the entire log file
```python
log.clear_all()
```
## log format
with timestamp
```
15:54:11 | info | info log
15:54:58 | Warning | warning log
15:55:08 | Error | Error log
16:05:14 | hardware | custom log
16.06.14 | Debug | debug log
```
without
```
| info | info log
| Warning | warning log
| Error | Error log
| hardware | custom log
| Debug | debug log
```
in the console its the same but *console*
### <a href='https://github.com/hiikion/logi/blob/main/docs.md#logi-docs'>back to top</a>
