from flask import request, redirect, url_for

from model.inicialModel import InicialModel
from dao.inicialDao import InicialDao

class InicialController:
    def __init__(self):
        self.inicialDao = InicialDao()

    def insert(self):
        descricao = request.form['descricao']

        inicial = InicialModel(
            None,
            descricao
        )

        self.inicialDao.insert(inicial)

        return redirect(url_for('inicial'))

    def listar(self):
        return self.inicialDao.listar()

    def update(self, idInicial):
        descricao = request.form['descricao']

        inicial = InicialModel(
            idInicial,
            descricao
        )

        self.inicialDao.update(inicial)

        return redirect(url_for('inicial'))

    def delete(self, idInicial):
        self.inicialDao.delete(idInicial)

        return redirect(url_for('inicial'))