from flask import render_template
from . import main

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page
    '''
    name = 'MyBlog'
    return render_template('index.html' , name = name)