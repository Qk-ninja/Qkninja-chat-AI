import openai
from flask import Flask, jsonify, request

# Set your API key
openai.api_key = "YOUR_API_KEY"

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the endpoint
@app.route('/gpt3', methods=['POST'])
def generate_text():
    # Get the prompt from the request
    prompt = request.json['prompt']
    
    # Generate text
    completions = openai.Completion.create(engine="text-davinci-002",
                                      prompt=prompt,
                                      max_tokens=1024,
                                      n=1,
                                      stop=None,
                                      temperature=0.5)

    # Get the generated text
    text = completions.choices[0].text
    
    # Return the generated text as a JSON response
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)

    
