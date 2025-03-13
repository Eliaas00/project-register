from flask import Flask, render_template # Importando biblioteca

# Criando variavel de aplicação
app = Flask(__name__)

# Criando uma rota
@app.route('/hello')
def ola():
  return "<h2> Iniciando projeto com flask</h2>"

@app.route("/lista")
def lista_alunos():

  #Criando uma lista
  lista_alunos_cadastrados = ['Elias', 'Fulano',
                            'Ciclano', 'Neymar']

  return render_template("lista.html", titulo = "UniFECAF", alunos = lista_alunos_cadastrados)

# Ultima linha do projeto
app.run()