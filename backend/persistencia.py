# -*- coding: utf-8 -*-
#from pymongo import Connection
from pymongo import MongoClient


class Persistencia():

    def __init__(self, url, user, password):
        #self.conn = Connection()  # Conexion local por defecto
        self.conn = MongoClient(url)
        self.conn.admin.authenticate(user, password)
        self.db = self.conn.PPT
        self.billetera = self.db.billetera

    def insert(self, aObject):
        self.billetera.insert(aObject)

    def update(self, aObject):
        self.billetera.update(aObject)

    def remove(self, aObject):
        self.billetera.remove(aObject)

    def find(self, aObject):
        return self.billetera.find(aObject)

    def findAll(self):
        response = self.billetera.find()
        return response

class Util:

    @classmethod
    def asDic(cls, object):
        return object.__dict__
