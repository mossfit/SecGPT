import argparse
from secgpt.scanner import scan_target
from secgpt.analyzer import analyze_scan_results
from secgpt.reporter import generate_report

def parse_arguments():

    parser = argparse.ArgumentParser(
        description='SecGPT - AI Assisted Security Tool for vulnerability scanning and recommendations.'
    )
    parser.add_argument('-t', '--target', type=str, required=True,
                        help='Target IP address or domain to scan.')
    parser.add_argument('-p', '--ports', type=str, default='80,443',
                        help='Comma-separated list of ports to scan (default: 80,443).')
    parser.add_argument('--verbose', action='store_true',
                        help='Enable verbose output for debugging.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    target = args.target

    try:
        ports = [int(port.strip()) for port in args.ports.split(',')]
    except ValueError:
        print("Error: Ports must be a comma-separated list of integers.")
        exit(1)
    
    if args.verbose:
        print(f"[INFO] Target: {target}")
        print(f"[INFO] Ports to scan: {ports}")
    
    # Module 3: Scanning
    scan_results = scan_target(target, ports, verbose=args.verbose)
    
    # Module 2: GPT Analysis
    recommendations = analyze_scan_results(scan_results, verbose=args.verbose)
    
    # Module 4: Reporting
    report_file = generate_report(scan_results, recommendations, verbose=args.verbose)
    
    # Final output
    print("Scan Results:", scan_results)
    print("Recommendations:", recommendations)
    print(f"Report saved as: {report_file}")

if __name__ == '__main__':
    main()
