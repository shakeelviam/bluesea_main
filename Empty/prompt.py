import openai

# Set your API key here
openai.api_key = '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'

# Path to your prompt file
prompt_path = '/home/recruitment_website/bluesea_main/Empty/prompt'

# Read the prompt text from the file
with open(prompt_path, 'r') as file:
    prompt_text = file.read()

# Create a completion request to GPT-3.5 Turbo
response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=prompt_text,
    max_tokens=150,
    temperature=0.7,
    top_p=1.0,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the generated text
print(response.choices[0].text.strip())

