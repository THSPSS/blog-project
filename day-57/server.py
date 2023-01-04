from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
AGIFY_ENDPOINT = "https://api.agify.io"
GENDERIZE_ENDPOINT = "https://api.genderize.io"





@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.date.today().year
    #**kwargs
    return render_template("index.html", num = random_number, year=current_year )

@app.route('/guess/<name>')
def guess(name):
    name_param= {
        "name": name,
    }
    response_age = requests.get(AGIFY_ENDPOINT, params=name_param)
    age_data = response_age.json()
    age= age_data["age"]
    response_gender = requests.get(GENDERIZE_ENDPOINT, params=name_param)
    gender_data = response_gender.json()
    gender= gender_data["gender"]
    return render_template("guess.html", g_name=name,g_age=age,g_gender=gender)


@app.route('/blog/<number>')
def get_blog(number):
    print(number)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)


