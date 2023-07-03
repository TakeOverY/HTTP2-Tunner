<h1 align="center">Chương Trình HTTP2 Tunner</h1>

<p align="center">
  Chương trình hỗ trợ trên centos ubuntu windowns
</p>

<p align="center">
  <img src="https://github.com/DauDau432/HTTP2-Tunner/blob/main/IMG/IMG.png">
</p>

### Panel Ddos Layer 7

***Yêu cầu:***

`python` `nodejs`

***Cài đặt:***

trên `ubuntu`
```
apt install nodejs -y
apt install npm -y
apt install python3-pip -y
```
trên `centos`
```
yum install nodejs -y
yum install npm -y
yum install python3-pip -y
```
cài đặt các thư viện cần thiết 
```
npm i http http2 crypto tls fake-useragent randomstring request axios
```
***khởi động chương trình:***
```
cd HTTP2-Tunner && python3 main.py
```
---------------------------------------------------------------

>***Đặt proxy HTTP bên trong `proxy.txt` `http.txt` và useragent bên trong `ua.txt`***
