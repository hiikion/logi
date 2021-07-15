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
import
```python
from logi import logi
```
enter the path of the log in the ``` path ``` <br>
examples what dose the timestamp do are <a href='https://github.com/hiikion/logi#log-example'>here</a>
```python
log = logi(path='C:/file path' timestamp=True)
```
## log example
### with timestamp
```
15:54:11 | info | info log
15:54:58 | Warning | warning log
15:55:08 | Error | Error log
16:05:14 | custom | custom log
```
### without timestamp
