from flask import Flask, render_template, request, redirect
from entidades.jogoEntidade import Jogo
from modal.jogoModal import JogoModal

app = Flask(__name__)

jogoModal = JogoModal()

@app.route('/')
def index():
    return render_template('lista.html',titulo='jogos',listaJogos=jogoModal.getTodos())

@app.route('/apagar/<id_jogo>')
def apagar(id_jogo=0):
    jogoModal.apagarPorId(id_jogo)
    return redirect('/')

@app.route('/editar/<id_jogo>')
def editar(id_jogo):
    jogo = jogoModal.getPorId(id_jogo)
    return render_template('jogo.html', titulo='Editar Jogo', jogo=jogo)

@app.route('/novo')
def novo():
    jogo = Jogo(0,'','','')
    return render_template('jogo.html', titulo='Novo Jogo', jogo=jogo)

@app.route('/salvar', methods=['POST'])
def salvar():
    jogo = Jogo(
        int(request.form['id']),
        str(request.form['nome']),
        str(request.form['categoria']),
        str(request.form['console']))
    jogoModal.salvar(jogo)
    return redirect('/')

app.run(host='0.0.0.0',port=80,debug=True)