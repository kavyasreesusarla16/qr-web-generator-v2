# 🔗 QR Code Generator Web App

A fast and simple QR Code Generator built using **Flask (Python)** and deployed live on Render.  
Users can generate QR codes from any text or URL, download them, and view QR history — all inside a clean UI.

🌐 **Live Demo:**  
https://qr-web-generator-v2.onrender.com

---

## 🚀 Features

- ✓ Generate QR codes from any text or link  
- ✓ Download QR as PNG  
- ✓ View QR History  
- ✓ Clean & responsive UI  
- ✓ Deployed and publicly accessible  
- ✓ Lightweight & fast

---

## 🛠️ Tech Stack

**Frontend:**  
- HTML  
- CSS  
- Jinja2 Templates  

**Backend:**  
- Python  
- Flask  

**QR Tools:**  
- qrcode  
- Pillow  

**Deployment:**  
- Render (Gunicorn + Production Server)  
- :contentReference[oaicite:1]{index=1} (Version Control)

---

## 📂 Project Structure
qr-web-generator/
│── app.py
│── requirements.txt
│── Procfile
│── static/
│ └── keep.txt
│── templates/
│ ├── index.html
│ └── history.html

---

## ⚙️ Run Locally

1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/qr-web-generator-v2.git
2️⃣ Move into the project folder
cd qr-web-generator-v2
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Start the server
python app.py
5️⃣ Open in browser
http://127.0.0.1:5000
🌍 Deployment (Render)

This project uses Render Web Service with this start command:

gunicorn app:app

Render automatically installs all dependencies from:

requirements.txt
🎯 Learning Outcomes

Flask backend development

Handling static & dynamic files

Using Jinja2 templates

Working with QR generation libraries

Debugging deployment issues

Deploying real apps on Render

Managing a repo on GitHub

🔮 Future Improvements

Dark Mode UI

Add custom QR colors

Add logo inside QR

Convert Web App into API

Store QR history in database

Add user login

👩‍💻 Author

Kavya Sree Susarla
B.Tech CSE (AI)
Aspiring Software Developer | Python & Flask Enthusiast 🚀

If you like this project ⭐ star the repo!
