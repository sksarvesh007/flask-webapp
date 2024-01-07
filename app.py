from flask import Flask, render_template , jsonify

app = Flask(__name__)

JOBS=[
    {
        'id': 1,
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'description': 'Work on Google Search'
    },
    {
        'id': 2,
        'title': 'Quant Analyst',
        'company': 'Facebook',
        'location': 'Menlo Park, CA',
        'description': 'Work on Facebook Ads'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'company': 'Apple',
        'location': 'Cupertino, CA',
        'description': 'Work on Apple Watch'
    },
    {
        'id': 4,
        'title': 'ML Engineer',
        'company': 'Amazon',
        'location': 'Seattle, WA',
        'description': 'Work on Amazon Web Services'
    },
    {
        'id': 5,
        'title': 'Cloud Engineer',
        'company': 'Microsoft',
        'location': 'Redmond, WA',
        'description': 'Work on Microsoft Azure'
    }
]

@app.route('/')
def index():
    return render_template('index.html' , jobs=JOBS , company_name = "SHINOMORI")
    for job in JOBS:
        print(job['title'])
        print(job['company'])
        
@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
