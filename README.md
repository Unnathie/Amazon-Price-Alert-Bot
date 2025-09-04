# Amazon-Price-Alert-Bot
Tired of refreshing Amazon every day to check if your favorite item’s price dropped?  
Let this little Python bot do the stalking for you.  

It watches a product, and when the price sneaks below your chosen target — 💌 *you get an email alert*.  
No more impulse-buying at high prices. 😎  

---

## ✨ Features
- 🔎 Scrapes real-time Amazon prices (works with Indian Rupees ₹ by default)  
- 📧 Sends yourself an email the moment the price drops below your target  
- 🔒 Credentials are safely hidden in a `.env` file  
- 🐍 Lightweight and built with Python’s `requests`, `BeautifulSoup`, and `smtplib`  

---

## 🛠️ Requirements
- Python 3.7+  
- Install dependencies:bs4,requests
---

## ⚙️ Setup

1. **Clone this repo**

```bash
git clone https://github.com/Unnathie/Amazon-Price-Alert-Bot.git
cd Amazon-Price-Alert-Bot
```

2. **Create a virtual environment** (recommended, keeps things tidy 🧹):

```bash
python -m venv venv
# Activate it
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Add your secrets in `.env`** (never commit this file!):

```env
EMAIL=youremail@gmail.com
PASSWORD=your_app_password
```

👉 Gmail users: turn on **2FA** and generate an **App Password**.
👉 Using Outlook/Yahoo? Just swap out the SMTP settings in `main.py`.

4. **Update the product URL & target price in `main.py`**:

```python
URL = "https://www.amazon.in/some-product/"
TARGET_PRICE = 800
```

---

## ▶️ Usage

Run the bot:

```bash
python main.py
```

* If the price is right (≤ your target) → you’ll get a ✨ surprise email ✨
* If not, you’ll just see:

```
No alert, price still above target.
```

---

## 📂 Don’t Push Your Secrets

Here’s a `.gitignore` snippet you’ll want:

```
.env
__pycache__/
*.pyc
```

---

## 🚀 Future Upgrades

* ⏰ Run daily with cron / Task Scheduler
* 🗂 Track multiple products at once
* 📊 Log prices into a CSV for trend-watching nerds

---

## 📜 License

MIT License — because sharing is caring.

---

> ⚡ Fun fact: The book I tested this on was *cheaper than my last coffee*. ☕📖

```
