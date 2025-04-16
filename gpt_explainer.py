import os
from openai import OpenAI


def query_gpt(question: str, matches: list, stream=False) -> str:
    """
    Queries GPT-4.1 with the developer's question and the relevant code snippets,
    then returns the generated explanation.
    
    Args:
        question: The developer's question
        matches: List of code snippet matches
        stream: If True, returns a stream object instead of a string
    """
    if not matches:
        return "No code snippets found to generate an explanation."

    # Combine all matches into a formatted string
    code_context = "\n\n".join(
        [
            f"File: {match['file']} (Line {match['line_number']}):\n{match['code']}"
            for match in matches
        ]
    )

    # Create the GPT-4.1 prompt
    system_message = "You are a helpful coding assistant that explains code based on provided snippets."
    user_message = f"""A developer asked the following question:
"{question}"

Here are the relevant code snippets:
{code_context}

Based on the code snippets, answer the question clearly and concisely.
"""

    # Load API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "Error: OPENAI_API_KEY environment variable is not set."

    # Create an OpenAI client using the API key
    client = OpenAI(api_key=api_key)

    try:
        if stream:
            # Return the stream object for the caller to process
            return client.responses.create(
                model="gpt-4.1",
                input=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                stream=True,
            )
        else:
            # Return the complete response as a string
            response = client.responses.create(
                model="gpt-4.1",
                input=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
            )
            return response.output_text.strip()
    except Exception as e:
        return f"Error generating explanation: {e}"
