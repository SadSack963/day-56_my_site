from flask import Flask, render_template


app = Flask(__name__)

# url_for('static', filename='/css/styles.css')
# url_for('static', filename='/images/fun ride.css')

@app.route('/')
def home_page(name=None):
    return render_template('./my_site/index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

