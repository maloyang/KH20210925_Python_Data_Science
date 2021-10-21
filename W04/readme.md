
## Week 04
2021/10/21 修改為：

### IDE工具介紹
- 以下都是Python程式開發用的IDE編輯器，可以選一個自己習慣的就好，沒有想法，可以直接選用VSCode
    - [VSCode](https://code.visualstudio.com/)
    - [pyscripter](https://sourceforge.net/projects/pyscripter/) : 我個人目前是使用3.6或以前的版本，目前已出4.1版
    - [NotePad++](https://notepad-plus-plus.org/downloads/)
    - [Sublime](https://www.sublimetext.com/)
    - [pycharm](https://www.jetbrains.com/pycharm/)

### Python地圖網頁應用
- 以Heroku實作地圖應用網頁
- 有Heroku上傳問題的同步處理....


### Heroku開啟一個新的專案 or 進入下一步，用上星期的成果直接改就可以
- `git init`
- `git add .`
- `heroku apps:create malo-flask-map`，回應如下，算是完成
```
 »   Warning: heroku update available from 7.54.0 to 7.59.0.
Creating ⬢ malo-flask-map... done
https://malo-flask-map.herokuapp.com/ | https://git.heroku.com/malo-flask-map.git
```
- `git commit -am "v1"`
- `git push heroku master`
- 到這邊都完成了，就表示你的專案佈署成功

### TODO: 請以你的W01做出來的成果，從colab上下載下來，放到 ./static/ 中
- copy W04中 flask-map-01 資料夾的檔案出來用
- 使用`git commit -am "v1"`更版、再使用`git push heroku master`佈署程式
- 以我們目前的flask-map_01為例，你可以在以下的網頁看到成果
- 若是以靜態檔案提供服務：以`https://malo-flask-map.herokuapp.com/W01-6.html`可以看到我們之前完成的成果
- 或是以我們設定的url提供服務：`https://malo-flask-map.herokuapp.com/map/w01-6`

### TODO: 以W01的新北市腳踏車為例，提供即時的停車資訊
- ref: flask-map_02
- 若是加上zoom的功能，可以利用網址上的參數來處理

----
### cron: 排程
- 使用 apscheduler 進行排程工作
- TODO: 將line notify警報加入排程

----
### 資料庫: mysql or mariadb
