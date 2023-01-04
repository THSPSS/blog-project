from flask import Flask, render_template,request
import requests
import smtplib
from post import Post


my_email = "contentc082@gmail.com"
password = "bokmqyvrtuxuicnj"



posts = requests.get("https://api.npoint.io/00addcbbc982ed2e2971").json()

post_objects = []
for post in posts:
    post_obj = Post(post['id'],post['title'],post['subtitle'],post['body'],post['author'],post['dates'],
                    post['img_address'])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts= post_objects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data['name'],data['email'],data['phone'],data['message'])
        return render_template("contact.html",send_message=True)
    return render_template("contact.html",send_message=False)

def send_email(name,email,phone,message):
    email_msg = f"Subject:New Message\n\n name:{name}email:{email}phone:{phone}message:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(my_email, my_email,email_msg)



@app.route('/post/<int:id>')
def read_post(id):
    request_post = None
    for blog_post in post_objects:
        if blog_post.id == id:
            print(blog_post)
            request_post = blog_post
    return render_template("post.html", post=request_post)



if __name__ == "__main__":
    app.run(debug=True)
