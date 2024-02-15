import openai

# Set your API key here
openai.api_key = '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'


# Path to your prompt file
prompt_path = '/home/shakeel/recruitment_website/bluesea_main/prompt'

# Read the prompt text from the file
with open(prompt_path, 'r') as file:
    prompt_text = file.read()

# Create a chat completion request
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text}
        ]
    )

    # Print the generated text
    if response.choices:
        print(response.choices[0].message['content'].strip())
    else:
        print("No response was generated.")
except Exception as e:
    print(f"An error occurred: {e}")