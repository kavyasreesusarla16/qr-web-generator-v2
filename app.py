from flask import Flask, render_template, request, send_from_directory
import qrcode
import os
import time

app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists("static"):
    os.makedirs("static")


# -----------------------------------
# HOME PAGE (Generate QR)
# -----------------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    qr_filename = None

    if request.method == "POST":
        data = request.form.get("data")

        if data:
            # Unique file name using timestamp
            qr_filename = f"qr_{int(time.time())}.png"
            file_path = os.path.join("static", qr_filename)

            # Create QR without logo
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save(file_path)

    return render_template("index.html", qr_filename=qr_filename)


# -----------------------------------
# QR DOWNLOAD ROUTE
# -----------------------------------
@app.route("/download/<filename>")
def download_qr(filename):
    return send_from_directory("static", filename, as_attachment=True)


# -----------------------------------
# QR HISTORY PAGE
# -----------------------------------
@app.route("/history")
def history():
    files = os.listdir("static")
    image_files = [f for f in files if f.endswith(".png")]
    return render_template("history.html", images=image_files)


# -----------------------------------
# RUN APP
# -----------------------------------
if __name__ == "__main__":
    app.run(debug=True)