from flask import Flask, request
import comparer

app = Flask('app')

@app.route("/", methods=['POST'])
def home():

    data_a_text = request.form['data_a']
    data_b_text = request.form['data_b']
    result = comparer.compare(data_a_text,data_b_text)

    return str(result)

app.run()
