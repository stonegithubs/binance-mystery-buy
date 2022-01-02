[english](README.md) | [русский язык](README-RU.md)

# Программное обеспечение для быстрой покупки мистери боксов на Binance.

+ [Назначение ПО](#назначение-по)
+ [Установка и настройка](#установка-и-настройка)
+ [Мотивация](#мотивация)
+ [Спецификация](#спецификация)
+ [Дисклеймер](#дисклеймер)

## Назначение ПО

В момент распродажи на Binance купить мистери бокс "руками" становится почти невозможно. 
Для этого были написаны программы, как эта, которые генерируют большое количество запросов,
в указанное время, что значительно увеличивает ваши шансы на покупку бокса.

## Установка и настройка

### Windows

+ Скачать последнюю версию [Python](https://www.python.org/downloads), при установке необходимо указать 
>Add Python 3.? to PATH
+ Скачать [ChromeDriver](https://chromedriver.chromium.org/downloads), который подходит для вашей версии Google Chrome. 
Скачанный файл необходимо поместить в одну папку с программой.
+ Скачать [pip](https://pip.pypa.io/en/stable/installation)(Python Package Index)
+ Скачать [Visual C++](https://docs.microsoft.com/ru-ru/cpp/windows/latest-supported-vc-redist)
+ Подключить пакеты, выполните в cmd: 
  
        pip install requests
        pip install aiohttp
        pip install selenium
        pip install selenium-wire
        
+ Отредактируйте файл config.py перед запуском ПО.  
Параметры:
  + *requests_payload* -- Полезная нагрузка запроса покупки, можно менять значение *number* - количество боксов и productId - ID бокса(скрин ниже);
![ID бокса](/images/productId.jpg)  

  + *product_id* -- ID продукта аукциона маркетплейс, необходимо для обхода капчи, подойдет любой аукцион маркетплейс, где вы можете сделать ставку(скрин ниже);
![ID аукциона](/images/product_id.jpg)  

  + *sale_time* -- Время начала продажи боксов в формате Unix(скрин ниже);
![Время начала продаж](/images/sale_time.jpg)  

  + *requests_count* -- Количество запросов, лучше не ставить более 1200, могут забанить IP-адрес;  

+ Для запуска откройте *bot.py* в IDLE(скрины ниже)  

![Запуск IDLE](/images/IDLE%20%231.jpg)  

![Запуск IDLE](/images/IDLE%20%232.png)
        
+ Cледуйте инструкциям в IDLE

## Мотивация

В настоящий момент, рынок продажи ПО для Binance является очень закрытым и преступным. Людей 
обманывают и продают видео ролики с обещаниями. В текущий момент это единственная бесплатная и 
рабочая программа для покупки боксов. Давайте улучшать ее вместе 😎  

*Мои контакты можно найти на [странице GitHub](https://github.com/ell1s-m)*.

## Спецификация

ПО написано на Python.  

*Зависимости*:
1. [Python](https://www.python.org)
2. [Selenium](https://www.selenium.dev)
3. [Aiohttp](https://docs.aiohttp.org/en/stable)
4. [Visual C++](https://docs.microsoft.com/ru-ru/cpp/windows/latest-supported-vc-redist)
5. [Google Chrome](https://www.google.com/chrome)

Тестирование проводилось только на ОС семейства Windows. Компоненты ПО являются кроссплатформенными, но гарантировать 
работоспособность не могу.

## Дисклеймер

Я не являюсь автором данного программного обеспечения, и не несу ответственность за любые риски связанные с его исполнением.
Программое обеспечение предоставляется "Как есть", вы можете самостоятельно его дорабатывать и улучшать.