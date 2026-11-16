from flask import render_template, request, redirect, url_for

from model.socialModel import SocialModel

from dao.socialDao import SocialDao

class SocialController:
    def __init__(self):
        self.socialDao = SocialDao()

    #Inserir
    def insert(self):
        avaliacao = request.form['avaliacao']
        social = SocialModel(
            None,
            avaliacao
        )
        self.socialDao.insert(social)

        return redirect(url_for('social'))

    #listar 
    def listar(self):
        return self.socialDao.listar()

    
    # UPDATE
    def update(self, idSocial):
        avaliacao = request.form['avaliacao']

        social = SocialModel(
            idSocial,
            avaliacao
        )

        self.socialDao.update(social)

        return redirect(url_for('social'))

    # DELETE
    def delete(self, idSocial):
        self.socialDao.delete(idSocial)

        return redirect(url_for('social'))
