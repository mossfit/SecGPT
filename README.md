# SecGPT

SecGPT is an AI-assisted security tool for vulnerability scanning and recommendations. It combines a command-line interface with modular components for scanning and analysis. Inspired by PentestGPT, this project is designed to be extended and integrated with advanced AI functionalities.

## Modules

- **CLI:** Handles user input and parses command-line arguments.
- **Scanner:** Contains functions to perform vulnerability scanning on target IPs/domains.
- **Analyzer:** Processes scanning results and provides recommendations (potentially using AI).

## Getting Started

1. Clone the repository.
2. Install dependencies with
   `pip install -r requirements.txt`.
4. Run the tool:
    ```bash
    python main.py -t example.com -p 80,443 --verbose
    ```

## Tests

Run tests using:
```bash
pytest tests/
```
### Usage

Set Up Environment Variables:

For GPT integration, set your GPT API key:

```bash
export GPT_API_KEY="your_gpt_api_key_here"
```
Run the tool via the command line:

```bash
python main.py -t example.com -p 80,443 --verbose
```

*Web Interface*
Start the Flask web server to use the web interface:

```bash
python secgpt/webapp.py
```
**Then, open your browser and navigate to http://localhost:5000 to access the scan form and view results.**

Docker
Build the Docker Image:

```bash
docker build -t secgpt .
```
Run the Container:
```bash
docker run --rm -e GPT_API_KEY=your_gpt_api_key_here secgpt
```
Using Docker Compose
If you prefer Docker Compose, use the provided docker-compose.yml file:

```bash
docker-compose up --build
```
Continuous Integration
SecGPT includes a GitHub Actions workflow (.github/workflows/ci.yml) that automatically runs tests using pytest on each push or pull request. This helps maintain code quality and catch issues early.

Project Structure
```arduino
SecGPT/
├── .github/
│   └── workflows/
│       └── ci.yml
├── templates/
│   ├── index.html
│   └── results.html
├── tests/
│   └── test_cli.py
├── secgpt/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── cli.py
│   ├── dockerfile (Dockerfile)
│   ├── gpt_client.py
│   ├── logger.py
│   ├── reporter.py
│   ├── scanner.py
│   └── webapp.py
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── setup.py
