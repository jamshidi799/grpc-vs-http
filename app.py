from flask import Flask, request

# create the Flask app
app = Flask(__name__)

visit_count = 0


@app.route('/product', methods=['POST'])
def update():
    global visit_count
    visit_count += 1
    return {"visit_count": visit_count}
