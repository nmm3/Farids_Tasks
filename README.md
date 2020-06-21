### Git
`git add -A` - Добавить все файлы в папке в кэш
`git commit -am "<Сообщение>"` - Зафиксировать измения в коде
`git push origin master` - загрузить изменения на гитхаб
`git pull origin master` - скачать изменения с гитхаба

### Про зависимости.
Зависимости прописываются в requirements.txt. Зависимости - это код, когда-то кем-то написанный 
и размещенный на сервере (в данном случае pypi.org)
Чтобы установить зависимости нужно открыть терминал в папке проекта и написать 

`pip3 install -r requirements.txt`

### Если выдаст ошибку, что команда pip3 не найдена

`sudo apt-get install python3-pip`

### Если выдаст ошибку, что не был найден distutils.core, то выполнить команду

`sudo apt-get install python3-distutils`

Если при выполнении этой команды ругнется на недостающие зависимости, то выполнить

`sudo apt-get install -f`

А после этого опять

`sudo apt-get install python3-distutils`
