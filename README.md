# logi v1.3.3

## instolation
the lib works on python 3x versions
```python
pip install logi
```

## examples
import
```python
import logi
```

```python
log = logger(path='C:/file path', timestamp=True, dbg=True)
```
info log
```python
log.info('info log')
```
final code
```python
from logi import logi
log = logi(path='C:/file path', timestamp=True, dbg=True)
log.info('info log')
# output: 15:54:11 | info | info log
```
## <a href='https://github.com/hiikion/logi/blob/main/DOCS.md'>full docs here</a>

## log example
### with timestamp
```
15:54:11 | info | info log
15:54:58 | Warning | warning log
15:55:08 | Error | Error log
16:05:14 | hardware | custom log
16.06.14 | Debug | debug log
```
### without timestamp
```
| info | info log
| Warning | warning log
| Error | Error log
| hardware | custom log
| Debug | debug log
```
### links 
<a href="https://pypi.org/project/logi/">pypi</a>
### <a href='https://github.com/hiikion/logi/blob/main/README.md#logi-v133'>return</a>
