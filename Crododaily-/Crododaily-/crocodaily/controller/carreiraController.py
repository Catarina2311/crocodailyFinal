from flask import render_template, request, redirect, url_for

from model.carreiraModel import CarreiraModel

from dao.carreiraDao import CarreiraDao

class CarreiraController:
    def __init__(self):
        self.carreiraDao = CarreiraDao()

    #Inserir
    def insert(self):
        avaliacao = request.form['avaliacao']
        carreira = CarreiraModel(
            None,
            avaliacao
        )
        self.carreiraDao.insert(carreira)

        return redirect(url_for('carreira'))

    #listar 
    def listar(self):
        return self.carreiraDao.listar()

    
    # UPDATE
    def update(self, idCarreira):
        avaliacao = request.form['avaliacao']

        carreira = CarreiraModel(
            idCarreira,
            avaliacao
        )

        self.carreiraDao.update(carreira)

        return redirect(url_for('carreira'))

    # DELETE
    def delete(self, idCarreira):
        self.carreiraDao.delete(idCarreira)

        return redirect(url_for('carreira'))
