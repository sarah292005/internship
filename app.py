from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with open('submissions.txt', 'a') as f:
            f.write(f"{name}, {email}, {message}\n")

        return render_template('form.html', success=True)

    return render_template('form.html', success=False)

if __name__ == "__main__":
    app.run(debug=True)
