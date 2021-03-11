from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    # return render_template('./my_site/index.html')
    # return render_template('./my_site/challenge.html')
    return render_template('./challenge2/index.html')



if __name__ == '__main__':
    app.run(debug=True)

