import openai

# Use the API key from your OpenAI account
openai.api_key = "YOUR_API_KEY"

# Define the prompt, or the text that you want GPT-3 to complete
prompt = "Write a chatbot for python 3"

# Use the completions() function to generate text
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# The generated text is stored in the message property
message = completions.choices[0].text

# Print the generated text
print(message)
