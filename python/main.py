from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/index")
def hello():
    return render_template('stickinotes4.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')