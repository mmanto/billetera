import hashlib

'''
    Funcionalidades de ayuda, conversión, encriptación, etc.
'''
class Util:
    
    '''
    Dado un objeto determinado retorna los datos de ese objeto
    como objeto diccionario.
    '''
    @classmethod
    def asDic(cls, object):
        return object.__dict__
   
    '''
    Genera un hash con estos datos
    nombre
    tipoEntidad
    correo
    operacion
    ''' 
    @classmethod
    def sha1(cls,nombre, tipoEntidad, correo, operacion):
        return hashlib.sha1(nombre + tipoEntidad + correo + operacion).hexdigest()
