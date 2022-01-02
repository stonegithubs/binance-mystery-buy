[english](README.md) | [русский язык](README-RU.md)

# Software for quick purchase of mystery boxes on Binance.

+ [Purpose](#purpose)
+ [Installation & setup](#installation--setup)
+ [Motivation](#motivation)
+ [Specification](#specification)
+ [Disclaimer](#disclaimer)

## Purpose

At the time of the sale on Binance, it is almost impossible to buy a mystery box with "hands". For this, programs 
were written that generate a large number of requests at a specified time, which significantly increases your 
chances of buying a box.

## Installation & setup

+ Download the latest version of [Python](https://www.python.org/downloads), during installation, you must specify
>Add Python 3.? to PATH
+ Download [ChromeDriver](https://chromedriver.chromium.org/downloads), which is suitable for your version of Google Chrome. 
The downloaded file must be placed in the same folder with the program.
+ Download [pip](https://pip.pypa.io/en/stable/installation)(Python Package Index)
+ Download [Visual C++](https://docs.microsoft.com/ru-ru/cpp/windows/latest-supported-vc-redist)
+ Include packages, run in cmd: 
  
        pip install requests
        pip install aiohttp
        pip install selenium
        pip install selenium-wire
        
+ Edit the config.py file before running the software.    
Parameters:
  + *requests_payload* -- Payload of the purchase request, you can change the value *number* - the number of boxes and productId - the ID of the box (screen below);
![Box ID](/images/productId.jpg)  

  + *product_id* -- Product ID of the marketplace auction, you need to bypass the captcha, any marketplace auction where you can place a bid will do (screen below);
![Auction ID](/images/product_id.jpg)  

  + *sale_time* -- The start time of the sale of boxes in Unix format (screen below);
![Sales start time](/images/sale_time.jpg)  

  + *requests_count* -- The number of requests, it is better not to set more than 1200, can ban the IP address;  

+ To run, open *bot.py* in IDLE (screenshots below)  

![IDLE run](/images/idle1.jpg)  

![IDLE run](/images/idle2.jpg)
        
+ Follow the instructions in IDLE

## Motivation

At the moment, the market for selling software for Binance is very closed and criminal. People
cheat and sell video clips with promises. It is currently the only free and
working program for buying boxes. Let's improve it together 😎

*My contacts can be found on the [GitHub page] (https://github.com/ell1s-m)*.

## Specification

The software is written in Python.

*Dependencies*:
1. [Python] (https://www.python.org)
2. [Selenium] (https://www.selenium.dev)
3. [Aiohttp] (https://docs.aiohttp.org/en/stable)
4. [Visual C ++] (https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)
5. [Google Chrome] (https://www.google.com/chrome)

Testing was carried out only on Windows operating systems. The software components are cross-platform, but guaranteed
working capacity can not.

## Disclaimer

I am not the author of this software, and I am not responsible for any risks associated with its execution.
The software is provided "As is", you can modify and improve it yourself.
