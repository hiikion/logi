# logi
### instolation
```
pip install logi
```
### examples

```python
from logi import logi

log = logi(path='C:/file path' timestamp=True)
log.info('info log')
log.warning('warning log')
log.error('Error log')
log.custom('custom log' cust='custom')
```
