# -*- coding: utf-8 -*-
from pymongo import Connection


class Persistencia():

    def __init__(self):
        self.conn = Connection()  # Conexion local por defecto
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
