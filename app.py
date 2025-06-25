from flask import Flask, render_template, request, redirect, url_for
import csv, os
from io import BytesIO
import base64
import japanize_matplotlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.ion()

app = Flask(__name__)

DATA_FILE = 'responses.csv'
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age', 'choice'])

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name   = request.form['name']
        age    = request.form['age']
        choice = request.form['choice']
        with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, age, choice])
        return redirect(url_for('results'))
    return render_template('form.html')

@app.route('/results')
def results():
    from collections import Counter
    choices = []
    with open(DATA_FILE, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            choices.append(row['choice'])

    counter = Counter(choices)
    labels, values = zip(*counter.items())

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title('アンケート選択肢の集計')
    ax.set_xlabel('選択肢')
    ax.set_ylabel('回答数')

    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_data = base64.b64encode(buf.read()).decode('ascii')
    plt.close(fig)

    return render_template('results.html', plot_data=img_data)

if __name__ == '__main__':
    app.run(debug=True)
