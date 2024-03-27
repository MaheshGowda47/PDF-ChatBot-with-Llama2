from flask import Flask, render_template, jsonify, request
from source.run_chain import chain_link

application = Flask(__name__)
app = application

load = chain_link()
chain = load.load()
print(chain)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/chatbot', methods=["POST"])
def chatbotResponse():
    if request.method == 'POST':
        user_input = request.form['question']
        print(user_input)

        result = chain({'query': user_input})
        print(f"Answer: {result['result']}")
    return jsonify({"response": str(result['result'])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
