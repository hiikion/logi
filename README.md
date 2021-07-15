# logi
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

```python
from logi import logi

log = logi(path='C:/file path' timestamp=True)
log.info('info log')
log.warning('warning log')
log.error('Error log')
log.custom('custom log' cust='custom')
```

## log example

```
15:54:11 | info | info log
15:54:58 | Warning | warning log
15:55:08 | Error | Error log
16:05:14 | custom | custom log
```
