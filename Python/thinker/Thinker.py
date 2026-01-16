from flask import Flask, request, render_template, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'notes.json'

def save_note_to_file(title, content):
    note = {"title": title, "content": content}
    with open(DATA_FILE, 'a') as file:
        file.write(json.dumps(note) + "\n")

def load_notes_from_file():
    notes = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            for line in file:
                notes.append(json.loads(line.strip()))
    return notes

def search_notes(keyword):
    notes = load_notes_from_file()
    results = [note for note in notes if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower()]
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    if title and content:
        save_note_to_file(title, content)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', '')
    results = search_notes(keyword)
    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
