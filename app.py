from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Set your OpenAI API key
client = OpenAI(
    api_key='Use your API key here'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    # Get the input text from the form
    text = request.form.get('text')
    if not text:
        return 'Error: Text field is missing in the request', 400
    print(f'Input text: {text}')
# Call the OpenAI API
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": text}],
    )
    print(f'Output text: {response.choices[0]}')
 # Extract the output text from the API response
    output_text = response.choices[0].message.content

    print(f'Output text: {output_text}')

    # Return the output text JSON in index.html
    return jsonify({'text': output_text, 'completed_text': output_text } )

if __name__ == '__main__':
    app.run(debug=True)
