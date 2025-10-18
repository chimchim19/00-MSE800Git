"""
Week 12 - Activity 2 - Develop an initial Web APP
Develop a Wb Application to have Hyper link and load an image (from end user input) using Flask.
"""
from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

# Define the root route
@app.route('/')
def index():
    return render_template('index.html')

# Define the Hyperlink page route
@app.route('/hyperlink', methods = ['GET', 'POST'])
def hyperlink():
    if request.method == 'POST':
        # form for user input of image url
        image_url = request.form.get('image_url')
        # image url is passed to show_image.html
        return render_template('show_image.html', image_url = image_url)
    return render_template('hyperlink.html')


if __name__ == '__main__':
    # run the app
    app.run(debug=True)
