
# A very simple Flask Hello World app for you to get started with...
import json
from flask import Flask,render_template,request,jsonify
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open(f'{dir_path}/data.json', 'r') as f:
        data = f.read()
    return render_template("index.html", data=data)

@app.route('/lock', methods=['POST'])
def lock():
    if request.method == 'POST':
        d = request.args.get('user', '')
        if d == "":
            return redirect("/")

        with open(f'{dir_path}/data.json', 'r+') as f:
            data = json.load(f)
            data[d] = "enabled"
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        return 'Locked successfully'  # You can customize the response as needed

    else:
        pass


@app.route('/unlock', methods=['POST'])
def unlock():
    if request.method == 'POST':
        d = request.args.get('user', '')
        if d == "":
            return redirect("/")

        file_path = f'{dir_path}/data.json'

        with open(file_path, 'r') as file:
            data = json.load(file)

        key_to_remove = d

        if key_to_remove in data:
            del data[key_to_remove]
            print(f"The entry with key '{key_to_remove}' has been removed.")

            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
                print("JSON file updated successfully.")
        else:
            print(f"The key '{key_to_remove}' does not exist in the JSON data.")

        return 'Locked successfully'  # You can customize the response as needed

    else:
        pass

@app.route('/data', methods=['POST'])
def stuff():
    with open(f'{dir_path}/data.json', 'r') as f:
        data1 = f.read()

    return data1