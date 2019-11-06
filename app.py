from flask import Flask, render_template, jsonify, request
app = Flask(__name__, static_url_path="", static_folder="static")
@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/next', methods=['POST'])
def next():
    history = request.args.get('history', '')

    # Recommand according the history
    videostr = {'url': history[-1]+'1.mp4'}
    return jsonify(videostr)



if __name__ =='main':
    app.run(debug=True)
