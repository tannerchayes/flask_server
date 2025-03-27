# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
import csv
from flask import render_template_string
from post import get_post
from post import get_about

app = Flask(__name__)

from flask import render_template

@app.route('/')
# @app.route('/hello/<name>')
def index(name=None):

    template_yes = """
        <a href="/posts/{{ id }}/" class="w-1/4">
            <div class="group relative h-[300px]">
                <img class="absolute inset-0 object-cover w-full h-full" src="/static/img/{{ image }}">
                <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                <div class="relative">
                <h2 class="text-gray-50 text-lg align-text-bottom">{{ title }}</h2>
                </div>
            </div>
        </a>    
        """
    with open('data.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        blog_post_html = ""
        for row in csv_reader:
            context = {
                'image': row['image'],
                'title': row['title'],
                'id': row['id'],
            }

            post_html = render_template_string(template_yes, **context)
            blog_post_html += post_html

    context = {
        'blog_posts': blog_post_html,
    }
    return render_template('index.html', person=name, **context)


@app.route('/posts/<post_id>/')
def post_detail(post_id):
    post = get_post(post_id)
    return render_template('post_detail.html', **post)


@app.route('/<about_id>/')
def about_page(about_id):
    about = get_about(about_id)
    return render_template('about_page.html', **about)
