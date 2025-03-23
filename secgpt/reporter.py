import datetime

def generate_report(scan_results, recommendations, verbose=False):
    """
    Generates a Markdown report based on scan results and GPT recommendations.
    
    Args:
        scan_results (dict): The dictionary containing scan results.
        recommendations (str): The GPT-generated recommendations.
        verbose (bool): Enable verbose output.
        
    Returns:
        str: The filename of the generated report.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"scan_report_{now}.md"
    
    with open(filename, "w") as f:
        f.write("# Scan Report\n\n")
        f.write("## Scan Results\n")
        f.write(f"- **Target:** {scan_results.get('target')}\n")
        f.write("### Open Ports\n")
        for port in scan_results.get('open_ports', []):
            f.write(f"- {port}\n")
        f.write("\n### Closed Ports\n")
        for port in scan_results.get('closed_ports', []):
            f.write(f"- {port}\n")
        f.write("\n## Recommendations\n")
        f.write(recommendations)
    
    if verbose:
        print(f"[REPORT] Report generated: {filename}")
    
    return filename
