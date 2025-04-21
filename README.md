# # 📝 TODO List API

یک RESTful API ساده برای مدیریت لیست کارها (TODO List) با استفاده از Python، Flask و MongoDB.

## 🎯 ویژگی‌ها

- ایجاد کار جدید (Create)
- مشاهده‌ی همه کارها یا یک کار خاص (Read)
- ویرایش یک کار (Update)
- حذف یک کار (Delete)
- اتصال به دیتابیس MongoDB برای ذخیره‌سازی داده‌ها

---

## 🛠 تکنولوژی‌های استفاده شده

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [MongoDB](https://www.mongodb.com/)
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/)

---

## 🚀 نحوه اجرای پروژه

### 1. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

یا به صورت دستی:

```bash
pip install Flask flask-pymongo
```

### 2. اجرای برنامه

```bash
python app.py
```

سرور روی آدرس زیر اجرا می‌شود:

```
http://localhost:5000
```

---

## 📦 لیست Endpoints

| متد | آدرس | توضیح |
|------|--------|--------|
| GET | `/tasks` | نمایش همه‌ی کارها |
| GET | `/tasks/<id>` | نمایش یک کار خاص |
| POST | `/tasks` | ایجاد کار جدید |
| PUT | `/tasks/<id>` | ویرایش کار |
| DELETE | `/tasks/<id>` | حذف کار |

---

## 🧪 نمونه تست با `curl`

### ایجاد کار جدید:

```bash
curl -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title": "تمرین فلask", "description": "نوشتن API با MongoDB"}'
```

### نمایش همه‌ی کارها:

```bash
curl http://localhost:5000/tasks
```

---

## 🎥 ویدیو دمو

[مشاهده در یوتیوب](https://youtu.be/WGo7hoA-btQ)

---

## 📁 ریپازیتوری

کد کامل پروژه در این ریپازیتوری قرار دارد:  
[GitHub Repo](https://github.com/manixahmadi/tamrin2tarahiweb)

---

## 👤 توسعه‌دهنده

- **نام:** مانی احمدی  

---