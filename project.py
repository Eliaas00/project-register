from flask import Flask, render_template, request

# a linha abaixo cria a classe
class Aluno:
    def __init__(self, ra, nome, idade, email):
        self.ra_aluno = ra
        self.nome_aluno = nome
        self.idade_aluno = idade
        self.email_aluno = email

# As 3 proximas linhas instancia alunos
aluno01 = Aluno('97351', 'Elias Santana', '24', 'email@email.com')
aluno02 = Aluno('1002', 'Mathues', '20', 'gmail@gmail.com')
aluno03 = Aluno('2002', 'Neymar Marquezine Biancardi', '33', 'job@pai.com')

    # A LINHA ABAIXO CRIA UMA LISTA DE ALUNOS
lista_alunos_cadastrados = [aluno01, aluno02, aluno03]


#a linha abaixo cria a variavel de aplicação
app = Flask(__name__)

# a linha abaixo cria uma rota
@app.route('/hello')
def ola():
    return "<h2>Iniciando projeto com flask<h2>"

@app.route("/lista")
def lista_alunos():
    

  return render_template("lista.html", titulo = "Unifecaf", alunos = lista_alunos_cadastrados)

# A partir daqui tratamos a tela "cadastro.html"
@app.route('/cadastrar')
def cadastrar_aluno():
    return render_template('cadastro.html')

@app.route('/add_aluno', methods=['POST',])
def adiciona_aluno():
    ra_recebido = request.form['ra']
    nome_recebido = request.form['nome']
    idade_recebida = request.form['idade']
    email_recebido = request.form['email']

     # A linha abaixo instancia 
    novo_aluno = Aluno(ra_recebido, nome_recebido, idade_recebida, email_recebido)

    # A linha abaixo adiciona o novo aluno na lista
    lista_alunos_cadastrados.append(novo_aluno)

    return render_template("lista.html", titulo = "Unifecaf", alunos = lista_alunos_cadastrados)


# a liinha abaixo deve ser a ultima linha do projeto
app.run(debug=True)