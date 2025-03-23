from secgpt.gpt_client import get_analysis_recommendation

def analyze_scan_results(results, verbose=False):
    """
    Analyze scan results using GPT for detailed recommendations.
    
    Args:
      results (dict): The scan results dictionary.
      verbose (bool): Whether to print debugging information.
    
    Returns:
      str: GPT-based analysis recommendation.
    """
    # Create a prompt for GPT based on the scan results.
    prompt = (
        "You are a security expert. Analyze the following scan results "
        "and provide detailed recommendations for improving security:\n\n"
        f"{results}"
    )
    
    recommendation = get_analysis_recommendation(prompt, verbose=verbose)
    return recommendation
