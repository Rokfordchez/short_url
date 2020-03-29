## Описание

Сервис сокращения ссылки по алгоритму кодировки/декодировки ID к base62 и обратно к base10

### Установка

```bash
git clone https://github.com/Rokfordchez/short_url.git
```
виртуальное окружение

```bash
virtualenv -p python3 env
source env/bin/activate
cd short_url
pip install -r requirements.txt
```

### Запуск сервера
Из виртуального окружения:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000
```
### Код:
Логика в surl/models и surl/views, ajax реализация в templates/index.html
