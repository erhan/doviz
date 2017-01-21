# Cli döviz

Komut satırı üzerinden usd, eur, gbp  kurlarının değerlerini takip etmenizi sağlar.


## Kurulum

    $ sudo pip install git+https://github.com/erhan/doviz.git
    
    
## Bağımlılıklar
    
    lxml
    Click
    requests
    bs4
    
## Renkler 

    Yeşil : Kur değeri artmış
    Kırmızı : Kur değeri azalmış
    Mavi : Kur değeri değişmemiş

## Kullanım 

### Tüm kurlar (doviz.com)

    $ doviz
    
![Alt hepsi](/images/hepsi.png "doviz")
   
### İstediğiniz site için parametre verebilirsiniz.(DOV, PDOV)

    $ doviz --site PDOV

![Alt site](/images/site.png "doviz")

### İstediğiniz kur için parametre verebilirsiniz.(ALL, USD, EUR, GBP)

    $ doviz --kur USD

![Alt kur](/images/kur.png "doviz")
    
### Yardım

    $ doviz --help
    
![Alt help](/images/help.png "doviz")