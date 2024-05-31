from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
        {
        'id': 1,
        'title': 'House Help',
        'location': 'Monrovia, Liberia',
        'salary': 'USD. 3,000'
        },
        {
        'id': 2,
        'title': 'Teacher',
        'location': 'Accra, Ghana',
        'salary': 'USD. 2,000'
        },
        {
        'id': 3,
        'title': 'Gate Men',
        'location': 'Lagos, Nigeria',
        'salary': 'USD. 3,000'
        ,
    }
]
@app.route("/")
def Hire_Africa():
    return render_template('home.html', jobs=JOBS,
                          company_name='Hire_Africa')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


