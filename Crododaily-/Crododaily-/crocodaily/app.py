
from datetime import timedelta
from functools import wraps

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
    flash
)

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    verify_jwt_in_request,
    set_access_cookies,
    unset_jwt_cookies
)

from flask_bcrypt import Bcrypt

from controller.carreiraController import CarreiraController
from controller.socialController import SocialController
from controller.geralController import GeralController
from controller.inicialController import InicialController

from dao.usuarioDao import UsuarioDao


app = Flask(__name__)
app.secret_key = "croco123"

# Configuração JWT
app.config["JWT_SECRET_KEY"] = "troque-por-uma-chave-secreta"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_CSRF_PROTECT"] = False

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

usuarioDao = UsuarioDao()


# Proteção das páginas
def login_obrigatorio(view):

    @wraps(view)
    def wrapper(*args, **kwargs):

        try:
            verify_jwt_in_request()

        except Exception:
            return redirect(url_for('login'))

        return view(*args, **kwargs)

    return wrapper


# LOGIN E CADASTRO

@app.route('/')
def inicial():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    erro = None

    if request.method == 'POST':

        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if not usuario or not senha:
            erro = "Preencha todos os campos."

        else:
            dados = usuarioDao.buscar_por_usuario(usuario)

            if dados and bcrypt.check_password_hash(dados[2], senha):

                token = create_access_token(identity=usuario)

                resposta = make_response(
                    redirect(url_for('home'))
                )

                set_access_cookies(resposta, token)

                return resposta

            erro = "Usuário ou senha inválidos."

    return render_template('inicial.html', erro=erro)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    erro = None

    if request.method == 'POST':

        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if not usuario or not senha:
            erro = "Preencha todos os campos."

        elif usuarioDao.buscar_por_usuario(usuario):
            erro = "Esse usuário já está cadastrado."

        else:
            senha_criptografada = bcrypt.generate_password_hash(
                senha
            ).decode('utf-8')

            usuarioDao.inserir(
                usuario,
                senha_criptografada
            )

            return redirect(url_for('login'))

    return render_template('cadastro.html', erro=erro)


# HOME

@app.route('/home')
@login_obrigatorio
def home():

    usuario = get_jwt_identity()

    return render_template('home.html', usuario=usuario)


# LOGOUT

@app.route('/logout')
def logout():

    resposta = make_response(
        redirect(url_for('login'))
    )

    unset_jwt_cookies(resposta)

    return resposta


# CARREIRA

@app.route('/carreira', methods=['GET', 'POST'])
@login_obrigatorio
def carreira():

    controller = CarreiraController()

    if request.method == 'POST':
        return controller.insert()

    dados = controller.listar()

    return render_template(
        'carreira.html',
        dados=dados
    )


@app.route('/listarCarreira')
@login_obrigatorio
def listarCarreira():

    controller = CarreiraController()
    dados = controller.listar()

    return render_template(
        'listarCarreira.html',
        dados=dados
    )


@app.route('/editar/<int:id>', methods=['POST'])
@login_obrigatorio
def editar(id):

    controller = CarreiraController()
    return controller.update(id)


@app.route('/deletar/<int:id>')
@login_obrigatorio
def deletar(id):

    controller = CarreiraController()
    return controller.delete(id)


# SOCIAL

@app.route('/social', methods=['GET', 'POST'])
@login_obrigatorio
def social():

    controller = SocialController()

    if request.method == 'POST':
        return controller.insert()

    dados = controller.listar()

    return render_template(
        'social.html',
        dados=dados
    )


@app.route('/listarSocial')
@login_obrigatorio
def listarSocial():

    controller = SocialController()
    dados = controller.listar()

    return render_template(
        'listarSocial.html',
        dados=dados
    )


@app.route('/editarSocial/<int:id>', methods=['POST'])
@login_obrigatorio
def editarSocial(id):

    controller = SocialController()
    return controller.update(id)


@app.route('/deletarSocial/<int:id>')
@login_obrigatorio
def deletarSocial(id):

    controller = SocialController()
    return controller.delete(id)


# GERAL

@app.route('/geral', methods=['GET', 'POST'])
@login_obrigatorio
def geral():

    controller = GeralController()

    if request.method == 'POST':
        return controller.insert()

    dados = controller.listar()

    return render_template(
        'geral.html',
        dados=dados
    )


@app.route('/listarGeral')
@login_obrigatorio
def listarGeral():

    controller = GeralController()
    dados = controller.listar()

    return render_template(
        'listarGeral.html',
        dados=dados
    )


@app.route('/editarGeral/<int:id>', methods=['POST'])
@login_obrigatorio
def editarGeral(id):

    controller = GeralController()
    return controller.update(id)


@app.route('/deletarGeral/<int:id>')
@login_obrigatorio
def deletarGeral(id):

    controller = GeralController()
    return controller.delete(id)


# INICIAL - REGISTROS

@app.route('/inicial', methods=['GET', 'POST'])
@login_obrigatorio
def telaInicial():

    controller = InicialController()

    if request.method == 'POST':
        return controller.insert()

    dados = controller.listar()

    return render_template(
        'inicialDados.html',
        dados=dados
    )


@app.route('/listarInicial')
@login_obrigatorio
def listarInicial():

    controller = InicialController()
    dados = controller.listar()

    return render_template(
        'listarInicial.html',
        dados=dados
    )


@app.route('/editarInicial/<int:id>', methods=['POST'])
@login_obrigatorio
def editarInicial(id):

    controller = InicialController()
    return controller.update(id)


@app.route('/deletarInicial/<int:id>')
@login_obrigatorio
def deletarInicial(id):

    controller = InicialController()
    return controller.delete(id)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)






# from flask import Flask, render_template, request, redirect, url_for
# from controller.carreiraController import CarreiraController
# from controller.socialController import SocialController
# from controller.geralController import GeralController
# from controller.inicialController import InicialController

# app = Flask(__name__)

# carreiracontroler = CarreiraController()
# socialcontroller = SocialController()

# @app.route('/')
# def inicial():
#     return render_template('inicial.html')



# ####Carreira

# @app.route('/carreira', methods=['GET', 'POST'])
# def carreira():
#     controller = CarreiraController()

#     if request.method == 'POST':
#         return controller.insert()

#     dados = controller.listar()

#     return render_template(
#         'carreira.html',
#         dados=dados
#     )

# @app.route('/listarCarreira')
# def listarCarreira():
#     controller = CarreiraController()
#     dados = controller.listar()

#     return render_template('listarCarreira.html', dados=dados)

# @app.route('/editar/<int:id>', methods=['POST'])
# def editar(id):
#     controller = CarreiraController()
#     return controller.update(id)


# @app.route('/deletar/<int:id>')
# def deletar(id):
#     controller = CarreiraController()
#     return controller.delete(id)



# ####Social

# @app.route('/social', methods=['GET', 'POST'])
# def social():
#     controller = SocialController()

#     if request.method == 'POST':
#         return controller.insert()

#     dados = controller.listar()

#     return render_template(
#         'social.html',
#         dados=dados
#     )

# @app.route('/listarSocial')
# def listarSocial():
#     controller = SocialController()
#     dados = controller.listar()

#     return render_template('listarSocial.html', dados=dados)

# @app.route('/editar/<int:id>', methods=['POST'])
# def editarSocial(id):
#     controller = SocialController()
#     return controller.update(id)


# @app.route('/deletar/<int:id>')
# def deletarSocial(id):
#     controller = SocialController()
#     return controller.delete(id)


# ### Geral

# @app.route('/geral', methods=['GET', 'POST'])
# def geral():
#     controller = GeralController()

#     if request.method == 'POST':
#         return controller.insert()

#     dados = controller.listar()

#     return render_template(
#         'geral.html',
#         dados=dados
#     )

# @app.route('/listarGeral')
# def listarGeral():
#     controller = GeralController()
#     dados = controller.listar()

#     return render_template(
#         'listarGeral.html',
#         dados=dados
#     )

# @app.route('/editarGeral/<int:id>', methods=['POST'])
# def editarGeral(id):
#     controller = GeralController()
#     return controller.update(id)

# @app.route('/deletarGeral/<int:id>')
# def deletarGeral(id):
#     controller = GeralController()
#     return controller.delete(id)

#     ### Inicial

# @app.route('/inicial', methods=['GET', 'POST'])
# def telaInicial():
#     controller = InicialController()

#     if request.method == 'POST':
#         return controller.insert()

#     dados = controller.listar()

#     return render_template(
#         'inicial.html',
#         dados=dados
#     )

# @app.route('/listarInicial')
# def listarInicial():
#     controller = InicialController()
#     dados = controller.listar()

#     return render_template(
#         'listarInicial.html',
#         dados=dados
#     )

# @app.route('/editarInicial/<int:id>', methods=['POST'])
# def editarInicial(id):
#     controller = InicialController()
#     return controller.update(id)

# @app.route('/deletarInicial/<int:id>')
# def deletarInicial(id):
#     controller = InicialController()
#     return controller.delete(id)

# if __name__ == "__main__":
#     app.run(debug=True)