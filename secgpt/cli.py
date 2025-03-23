import argparse
from secgpt.scanner import scan_target
from secgpt.analyzer import analyze_scan_results

def parse_arguments():
    """
    Parse command-line arguments:
    - target: The target IP address or domain.
    - ports: Comma-separated ports to scan (default: 80,443).
    - verbose: Enable verbose output.
    """
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
    
    # Call the scanning module
    scan_results = scan_target(target, ports, verbose=args.verbose)
    
    # Call the analyzer module
    recommendations = analyze_scan_results(scan_results, verbose=args.verbose)
    
    # Display final results
    print("Scan Results:", scan_results)
    print("Recommendations:", recommendations)
