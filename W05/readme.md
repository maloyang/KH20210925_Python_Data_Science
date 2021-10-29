
# Week 05

## Pandas: 常用的資料科學工具介紹
- 方便的資料處理語法
- 方便的視覺化工具

## IoT
- MQTT 

## WEB API: 分享你整理完的資料
- 打造一個API分享你的資料

----
## 補充教材 (W04延伸)

- 排程+line notify

- 排程的cron參數
    - year (int|str) – 西元年
    - month (int|str) – 1~12月
    - day (int|str) – 1~31日
    - hour (int|str) – 0~23時
    - minute (int|str) – 0~59分
    - second (int|str) – 0~59秒
    - start_date (datetime|str) – 開始日(包含)
    - end_date (datetime|str) – 結束日(包含)

- 排程時間控制的範例
    ``` python
    # 每5分鐘執行一次
    scheduler.add_job(job_function1, 'cron', minute='*/5')

    # 每小時的10分、20分、50分執行一次
    scheduler.add_job(job_function2, 'cron', minute='10, 20, 50')

    # 每天的1點1分執行一次
    scheduler.add_job(job_function3, 'cron', hour='1', minute='1')

    # 每年的1,2,3,10,11,12月的早上6:30分，執行一次
    scheduler.add_job(job_function4, 'cron', month='1,2,3,10,11,12', hour='6', minute='30')

    # 一直到2021-10-31的早上6:30，執行程式一次
    scheduler.add_job(job_function5, 'cron', hour='6', minute='30', end_date='2021-10-31')
    ```
    