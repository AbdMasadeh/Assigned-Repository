from flask import Flask, render_template, request

app = Flask(__name__)

def flip(s):
    return s[-1::-1]


def count(s, ch):
    return str(s.count(ch))

def words(s):
    return str(s.count(' ') + 1)


def sorting(s, m):
    s = list(s.replace(' ', ''))
    if m == 'D':
        s.sort(reverse=True)
        return ''.join(s)
    elif m == 'A':
        s.sort()
        return ''.join(s)

@app.route("/flip")
def flip_endpoint():
    input_string = request.args.get('string')
    return render_template('flip.html', flipped=flip(input_string))

@app.route("/count")
def count_endpoint():
    input_string = request.args.get('string')
    input_char = request.args.get('char')
    return render_template('letter-count.html', count_of_occurrence=count(input_string, input_char))

@app.route("/words")
def words_endpoint():
    input_string = request.args.get('string')
    return render_template('words-count.html', count=words(input_string))

@app.route("/sort")
def sort_endpoint():
    input_string = request.args.get('string')
    input_char = request.args.get('mode')
    return render_template('sorting-string.html', sorted=sorting(input_string, input_char))