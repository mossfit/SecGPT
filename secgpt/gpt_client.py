import os
import openai

def get_analysis_recommendation(prompt, verbose=False):
    """
    Use GPT to analyze scan results and provide recommendations.
    
    Args:
      prompt (str): The prompt describing the scan results.
      verbose (bool): Whether to print debugging information.
    
    Returns:
      str: The analysis response from GPT.
    """
    openai_api_key = os.getenv("GPT_API_KEY")
    if not openai_api_key:
        raise ValueError("GPT API key not set. Please set the GPT_API_KEY environment variable.")

    openai.api_key = openai_api_key

    if verbose:
        print(f"[GPT] Sending prompt to GPT: {prompt}")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using GPT-3.5-turbo model
            messages=[
                {"role": "system", "content": "You are an expert security analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
            n=1,
            stop=None,
        )
        analysis = response.choices[0].message['content'].strip()
        if verbose:
            print(f"[GPT] Received response: {analysis}")
        return analysis
    except Exception as e:
        if verbose:
            print(f"[GPT] Error during GPT call: {e}")
        return "Error: Unable to get analysis from GPT."
