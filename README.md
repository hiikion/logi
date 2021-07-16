# logi ## v1.2
- <a href='https://github.com/hiikion/logi#instolation'>instolation</a>
- <a href='https://github.com/hiikion/logi#examples'>examples</a>
- <a href='https://github.com/hiikion/logi#log-example'>log example</a>
## instolation
the lib works on python 3x versions
```
pip install logi
```
or
```
pip3 install logi
```
## examples
import
```python
from logi import logi
```
the path can only be in this (C:/logi/logi/test.log) format <br>
examples what dose the timestamp do are <a href='https://github.com/hiikion/logi#without-timestamp'>here</a>
```python
log = logi(path='C:/file path', timestamp=True, dbg=True)
```
info log
```python
log.info('info log')
```
warning log
```python
log.warning('warning log')
```
Error log
```python
log.error('Error log')
```
custom log <br>
enter the log title in ```cust``` for example hardware
```python
log.custom('custom log' cust='hardware')
```
debug log <br>
will log in to the file only if dbg is true
```python
log.debug('debug log')
```
clear all <br>
clears the log file
```
log.clear_all()
```
final code
```python
from logi import logi

log = logi(path='C:/file path', timestamp=True, dbg=True)
log.info('info log')
log.warning('warning log')
log.error('Error log')
log.custom('custom log' cust='hardware')
```
## log example
### with timestamp
```
15:54:11 | info | info log
15:54:58 | Warning | warning log
15:55:08 | Error | Error log
16:05:14 | hardware | custom log
```
### without timestamp
```
| info | info log
| Warning | warning log
| Error | Error log
| hardware | custom log
```
### <a href='https://github.com/hiikion/logi#logi'>return</a>
