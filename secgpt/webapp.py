from flask import Flask, render_template, request, redirect, url_for, flash
import os
from secgpt.scanner import scan_target
from secgpt.analyzer import analyze_scan_results
from secgpt.reporter import generate_report
from secgpt.logger import setup_logger

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for flashing messages

# Initialize logger
logger = setup_logger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = request.form.get('target')
        ports_str = request.form.get('ports')
        verbose = True if request.form.get('verbose') == 'on' else False

        if not target or not ports_str:
            flash("Target and Ports are required!")
            return redirect(url_for('index'))
        
        try:
            ports = [int(port.strip()) for port in ports_str.split(',')]
        except ValueError:
            flash("Ports must be a comma-separated list of integers.")
            return redirect(url_for('index'))
        
        logger.info(f"Web scan initiated for target: {target} on ports: {ports}")
        
        # Module 3: Scanning
        scan_results = scan_target(target, ports, verbose=verbose)
        # Module 2: GPT Analysis
        recommendations = analyze_scan_results(scan_results, verbose=verbose)
        # Module 4: Reporting
        report_file = generate_report(scan_results, recommendations, verbose=verbose)
        
        flash(f"Scan complete! Report saved as {report_file}")
        return render_template('results.html', scan_results=scan_results, recommendations=recommendations, report_file=report_file)
    
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app on port 5000 and make it accessible externally.
    app.run(host='0.0.0.0', port=5000, debug=True)
