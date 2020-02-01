
# [tsux.me](https://tsux.me/)

## tsux.me とは

尽@京大生エンジニア のポートフォリオサイト兼ブログです。
Django / HTML / CSS / JavaScript （ jQuery 含む） で開発しました。
プロダクション環境のインフラは
Nginx / Gunicorn / PostgreSQL の比較的よく使われ、安定している組み合わせで整えています。

## デプロイ時の流れ（ubuntu）



```bash
# ubuntu の更新
sudo apt update
sudo apt upgrade
sudo apt install update-manager-core
sudo do-release-upgrade -d
# 必要なパッケージインストール
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
sudo apt autoremove
# プロジェクトフォルダを用意・移動
cd ~
mkdir ~/project
cd ~/project
# git を設定
git init
git remote add origin https://github.com/tsux2000/tsux.me.git
git pull origin master
echo python3 仮想環境の作成・アクティベート
python3 -m venv venv
. ./venv/bin/activate
# Python パッケージインストール
pip install --upgrade pip
pip install -r requirements.txt
pip install psycopg2 psycopg2-binary gunicorn
# Django の設定
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
# デアクティベート
deactivate
```
