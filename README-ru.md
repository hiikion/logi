# logi v1.2
## <a>eng</a>
- <a href='https://github.com/hiikion/logi#instolation'>установка</a>
- <a href='https://github.com/hiikion/logi#examples'>примеры</a>
- <a href='https://github.com/hiikion/logi#log-example'>примеры логов</a>
## установка
библиотека работает на всех версиях питона 3x и выше
```
pip install logi
```
or
```
pip3 install logi
```
## примеры
импорт
```python
from logi import logi
```
путь может быть только в таком формате (C:/logi/logi/test.log) <br>
примеры за что отвечает ```timestamp``` <a href='https://github.com/hiikion/logi#without-timestamp'>здесь</a>
```python
log = logi(path='C:/file path', timestamp=True, dbg=True)
```
инфо лог
```python
log.info('info log')
```
лог с предупреждением
```python
log.warning('warning log')
```
лог с ошибкой
```python
log.error('Error log')
```
кастомный лог <br>
 ```cust``` отвечает за название кастомного лога к примеру hardware
```python
log.custom('custom log' cust='hardware')
```
дебаг лог <br>
будет логироватся только если dbg = True
```python
log.debug('debug log')
```
очистка <br>
очищает весь файл
```python
log.clear_all()
```

## примеры логов
### с timestamp
```
15:54:11 | info | info log
15:54:58 | Warning | warning log
15:55:08 | Error | Error log
16:05:14 | hardware | custom log
16.06.14 | Debug | debug log
```
### без timestamp
```
| info | info log
| Warning | warning log
| Error | Error log
| hardware | custom log
| Debug | debug log
```
### <a href='https://github.com/hiikion/logi#logi'>на верх</a>
