from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location': 'Surabaya, Indonesia',
    'salary':'Rp. 10,000,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp. 15,000,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary':'$120,000'
   
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Singapore',
    'salary': '$150,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS, 
                        company_name='Mentari')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
