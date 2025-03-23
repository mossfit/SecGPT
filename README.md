# SecGPT

SecGPT is an AI-assisted security tool for vulnerability scanning and recommendations. It combines a command-line interface with modular components for scanning and analysis. Inspired by PentestGPT, this project is designed to be extended and integrated with advanced AI functionalities.

## Modules

- **CLI:** Handles user input and parses command-line arguments.
- **Scanner:** Contains functions to perform vulnerability scanning on target IPs/domains.
- **Analyzer:** Processes scanning results and provides recommendations (potentially using AI).

## Getting Started

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the tool:
    ```bash
    python main.py -t example.com -p 80,443 --verbose
    ```

## Tests

Run tests using:
```bash
pytest tests/
