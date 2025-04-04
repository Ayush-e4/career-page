from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Banglore',
        'salary': 10000
    },
    {
        'id': 2,
        'title': 'Frontend Engg.',
        'location': 'Delhi'
    },
    {
        'id': 3,
        'title': 'Backend Engg.',
        'location': 'Kolkata',
        'salary': 56000
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
