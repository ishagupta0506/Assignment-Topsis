import os
import re
import smtplib
import pandas as pd
from email.message import EmailMessage
from flask import Flask, request, render_template_string

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

#  CHANGE THESE TWO LINES
SENDER_EMAIL = "igupta1_be23@thapar.edu"
APP_PASSWORD = "USE_YOUR_APP_PASSWORD_HERE"

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>TOPSIS Web Service</title>
</head>
<body>
    <h2>TOPSIS Web Service</h2>
    <form method="POST" enctype="multipart/form-data">
        <label>Upload CSV file:</label><br>
        <input type="file" name="file" required><br><br>

        <label>Weights (comma separated):</label><br>
        <input type="text" name="weights" required><br><br>

        <label>Impacts (comma separated):</label><br>
        <input type="text" name="impacts" required><br><br>

        <label>Email ID:</label><br>
        <input type="email" name="email" required><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        # ---------- Validation ----------
        weight_list = weights.split(",")
        impact_list = impacts.split(",")

        try:
            weight_list = [float(w) for w in weight_list]
        except ValueError:
            return "<h3>Error: Weights must be numeric.</h3>"

        if len(weight_list) != len(impact_list):
            return "<h3>Error: Number of weights must equal number of impacts.</h3>"

        for i in impact_list:
            if i not in ["+", "-"]:
                return "<h3>Error: Impacts must be '+' or '-'.</h3>"

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            return "<h3>Error: Invalid email format.</h3>"

        # ---------- Save input file ----------
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)

        # ---------- TOPSIS ----------
        data = pd.read_csv(input_path)
        numeric_data = data.iloc[:, 1:].apply(pd.to_numeric)

        matrix = numeric_data.values
        norm = (matrix ** 2).sum(axis=0) ** 0.5
        weighted = (matrix / norm) * weight_list

        ideal_best = []
        ideal_worst = []

        for j in range(len(weight_list)):
            if impact_list[j] == "+":
                ideal_best.append(weighted[:, j].max())
                ideal_worst.append(weighted[:, j].min())
            else:
                ideal_best.append(weighted[:, j].min())
                ideal_worst.append(weighted[:, j].max())

        dist_best = ((weighted - ideal_best) ** 2).sum(axis=1) ** 0.5
        dist_worst = ((weighted - ideal_worst) ** 2).sum(axis=1) ** 0.5

        data["Topsis Score"] = dist_worst / (dist_best + dist_worst)
        data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

        output_path = os.path.join(RESULT_FOLDER, "result.csv")
        data.to_csv(output_path, index=False)

        # ---------- EMAIL ----------
        try:
            msg = EmailMessage()
            msg["Subject"] = "TOPSIS Result File"
            msg["From"] = SENDER_EMAIL
            msg["To"] = email
            msg.set_content("Please find attached the TOPSIS result CSV file.")

            with open(output_path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename="result.csv"
                )

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(SENDER_EMAIL, APP_PASSWORD)
                server.send_message(msg)

        except Exception as e:
            return f"<h3>Email sending failed: {e}</h3>"

        return """
        <h3>SUCCESS </h3>
        <p>TOPSIS result has been emailed successfully.</p>
        """

    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(debug=True)

