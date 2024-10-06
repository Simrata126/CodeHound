# app.py
from flask import Flask, render_template, request
from scanner import run_sherlock, scan_ports, run_nuclei, run_sqlmap, run_osint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route for OSINT
@app.route('/osint')
def osint():
    return render_template('osint.html')

@app.route('/run_osint', methods=['POST'])
def run_osint():
    username = request.form['username']
    sherlock_results = run_sherlock(username)
    return render_template('osint_results.html', results=sherlock_results)


# Route for Scanning
@app.route('/scanning')
def scanning():
    return render_template('scanning.html')

@app.route('/run_scanning', methods=['POST'])
def run_scanning():
    target = request.form['target']
    nmap_results = scan_ports(target)
    nuclei_results = run_nuclei(target)
    return render_template('scanning_results.html', nmap=nmap_results, nuclei=nuclei_results)


# Route for Possible Remediations
@app.route('/remediation')
def remediation():
    return render_template('remediation.html')

# Route for Documentation
@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
