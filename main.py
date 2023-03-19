from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
     'id': 1,
    'title': 'Software Engineer',
    'location': 'Chicago, USA',
    'salary': '$. 98,000'
  
  }, 
  {
    'id': 2,
    'title': 'Back-End Engineer',
    'location': 'Remote',
    'salary':  '$. 87,000'
  
  },
  {
    'id': 3,
    'title': 'Data Base Web Dev',
    'location': 'Toronto, CA',
    'salary': '$. 105,000'
  
  },
  {
    'id': 4,
    'title': 'Data Scientist ',
    'location': 'Montreal, CA',
    'salary': '$. 69,000'
  
  }
]


@app.route("/")
def hello_hashir():
  return render_template("home.html", jobs=JOBS, company_name='Hashir')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
