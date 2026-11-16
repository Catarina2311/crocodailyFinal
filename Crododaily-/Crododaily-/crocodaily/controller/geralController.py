from flask import request, redirect, url_for

from model.geralModel import GeralModel
from dao.geralDao import GeralDao

class GeralController:
    def __init__(self):
        self.geralDao = GeralDao()

    def insert(self):
        descricao = request.form['descricao']

        geral = GeralModel(
            None,
            descricao
        )

        self.geralDao.insert(geral)

        return redirect(url_for('geral'))

    def listar(self):
        return self.geralDao.listar()

    def update(self, idGeral):
        descricao = request.form['descricao']

        geral = GeralModel(
            idGeral,
            descricao
        )

        self.geralDao.update(geral)

        return redirect(url_for('geral'))

    def delete(self, idGeral):
        self.geralDao.delete(idGeral)

        return redirect(url_for('geral'))