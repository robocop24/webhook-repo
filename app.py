from flask import Flask
from flask import json
from flask import request
import app_database

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/github', methods = ['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        my_info = request.json
        if "pull_request" in my_info.keys():
            id = my_info["pull_request"]["id"]
            author = my_info["pull_request"]["user"]["login"]
            action = "Pull Request"
            timestamp = my_info["pull_request"]["created_at"]
            print(id, author, action, timestamp)
        elif "pusher" in my_info.keys():
            id = my_info["commits"][0]["id"]
            author = my_info["commits"][0]["author"]["name"]
            action = "Push"
            timestamp = my_info["commits"][0]["timestamp"]
            print(id, author, action, timestamp)
        insert_data({"id":id, "author":author, "action":action, "timestamp":timestamp})
        print("-"*50)
        return render_template('index.html', my_info = {"id":id, "author":author, "action":action, "timestamp":timestamp})

if __name__ == "__main__":
    app.run(debug=True)
