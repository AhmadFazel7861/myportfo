from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/work.html")
def work():
    return render_template("work.html")

@app.route("/works.html")
def works():
    return render_template("works.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('thankyou.html', sender_name=data.get("name"))
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

def write_to_csv(data):
    with open('database2.csv', mode='a', newline='', encoding='utf-8') as database2:
        name = data.get("name")
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Optional: Write headers only if file is empty
        if database2.tell() == 0:
            csv_writer.writerow(["name", "email", "subject", "message"])

        csv_writer.writerow([name, email, subject, message])

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
