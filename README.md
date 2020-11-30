安裝套件
======
``` shell script
$ pip install -r requirements.txt
```

運行專案
=====
```shell script
$ python manage.py runserver
```

前往連結 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 須知
* tgee/templates 存放所有 html 模板
* 目前使用 jninja2 作為模板引擎，如果改回 django 內建模板連結語法 & 迴圈語法都要做修改
* staticiles/scss 存放樣式文件，專案裝有 sass 編譯，可在啟用 server 下修改 scss 檔案會自行編譯

## TODO
* 客製化下拉選單目前沒有綁定 input 只有簡單外觀示範，之後要撰寫 JS 來模擬原生下拉選單
* 電腦版/手機版的字體要再重新微調
* 確認所有跟表單有關的都要放在 form tag 裡面，之後移植才不會錯亂
