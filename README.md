# BMI計算器與高血壓判斷器

這是一個使用 Python Flask 製作的網站，包含：

1. BMI計算器
2. 高血壓判斷器

## 本機執行方式

```bash
pip install -r requirements.txt
python app.py
```

瀏覽器輸入：

```text
http://127.0.0.1:5000
```

## Render 部署設定

Build Command：

```bash
pip install -r requirements.txt
```

Start Command：

```bash
gunicorn app:app
```
