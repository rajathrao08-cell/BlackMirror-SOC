import ollama


def generate_ai_analysis(alert):

    prompt = f"""
    Analyze this cybersecurity alert.

    Alert:
    {alert}

    Give:
    1. Threat summary
    2. Possible impact
    3. MITRE ATT&CK behavior
    4. Recommended action
    """

    try:

        response = ollama.chat(
            model="tinyllama",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI Error: {str(e)}"