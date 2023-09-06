from flask import Flask, render_template, request, redirect, url_for, flash
from luhn_validate import validador

app = Flask(__name__, template_folder='templates')
app.secret_key = 'eusouonumeroquatro'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/processar', methods=['POST'])
def processar_form():
    card_number = request.form['numero_cartao']
    exp_date = request.form['data_expi']
    cvv = request.form['cvv']
    if validador(card_number, exp_date, cvv):
        flash('Dados válidos', 'success')
        return redirect(url_for('index'))
    else:
        flash('Dados inválidos', 'error')
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
