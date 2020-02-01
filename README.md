
# [tsux.me](https://tsux.me/)

## tsux.me とは

尽@京大生エンジニア のポートフォリオサイト兼ブログです。
Django / HTML / CSS / JavaScript （ jQuery 含む） で開発しました。
プロダクション環境のインフラは
Nginx / Gunicorn / PostgreSQL の比較的よく使われ、安定している組み合わせで整えています。

## デプロイ時の流れ（ubuntu）

サーバー上で実行。

```bash
# ubuntu の更新
sudo apt update
sudo apt upgrade
sudo apt install update-manager-core
sudo do-release-upgrade -d
# 必要なパッケージインストール
sudo apt install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib nginx
sudo apt autoremove
# プロジェクトフォルダを用意・移動
cd ~
mkdir ~/project
cd ~/project
# git を設定
git init
git remote add origin https://github.com/tsux2000/tsux.me.git
git pull origin master
# python3 仮想環境の作成・アクティベート
python3 -m venv venv
. ./venv/bin/activate
# Python パッケージインストール
pip install --upgrade pip
pip install -r requirements.txt
pip install psycopg2 psycopg2-binary gunicorn
```

`sudo -u postgres psql` を実行して以下のように設定。

```sql
CREATE DATABASE db_tsux;
CREATE USER tsux WITH PASSWORD 'tsux';
ALTER ROLE tsux SET client_encoding TO 'utf8';
ALTER ROLE tsux SET default_transaction_isolation TO 'read committed';
ALTER ROLE tsux SET timezone TO 'UTC+9';
GRANT ALL PRIVILEGES ON DATABASE db_tsux TO tsux;
\q
```

`local.py` の用意。
また、 `SECRET_KEY` の作成は、以下でできる。

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

Django おきまりのやつ。

```bash
# Django の設定
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

`sudo vim /etc/systemd/system/gunicorn.service` で以下のように編集。

```bash
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/project
ExecStart=/home/ubuntu/project/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/project/project.sock project.wsgi:application

[Install]
WantedBy=multi-user.target
```

`sudo systemctl start gunicorn.service` で読み込みなど。
`sudo systemctl enable gunicorn` で自動起動設定も。

また、 `sudo vim /etc/nginx/sites-available/project` も編集。

```bash
server {
    listen 80;
    server_name tsux.me;

    location = /favicon.ico {access_log off; log_not_found off;}
    location /static/ {
        root /home/ubuntu/project;
    }
    location /media/ {
        root /home/ubuntu/project;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/project/project.sock;
    }
}
```

`sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled/` でリンクはる。
`sudo ufw allow 'Nginx Full'` でポート開ける。

以下で更新。

```bash
sudo systemctl restart nginx
sudo systemctl restart gunicorn
```

certbotなども設定し、 https 化する。
