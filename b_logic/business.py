# -*- coding: utf-8 -*-
from backend.mail_util import EMail
from b_logic.model import Solicitud
from backend.util import Util

'''
afadf
'''
class Billetera:
    '''
    Operaciones aceptadas.
    '''
    COBRAR = 'COBRAR'
    PAGAR = 'PAGAR'
    
    '''
    Entidades
    '''
    PERSONA = 'PERSONA'
    EMPRESA = 'EMPRESA'
    
    '''
    Datos del correo
    '''
    SERVIDOR_SMPT = 'smtp.gmail.com'
    PUERTO_SMTP = '587'
    CORREO_INFORMATIVO = 'CORREO_INFORMATIVO'
    CORREO_REMITENTE = 'prueba.mmanto@gmail.com'
    CORREO_PASSWORD = 'prueba.mmanto2k14'
    CORREO_A_VERIFICAR = 'CORREO_A_VERIFICAR'
    CORREO_A_INFORMAR = 'CORREO_A_INFORMAR'
    CORREO_PPT = 'info@paypertic.com.ar'
    
    '''
    Se genera una Solicitud de pago
    '''
    def generarSolicitudPago(self, form):
        # Armamos la solicitud con los datos del formulario
        solicitud = Solicitud(form)
        # El sistema registra la Solicitud
        persistencia.insert(Util.asDic(solicitud))
        
        # Info del pagador
        nombrePagador = request.form['nombre']
        correoPagador = request.form['email-pagador']
        
        # Info del cobrador
        nombreInstitucion = request.form['nombre-de-institucion']
        correoInstitucion = request.form['email-institucion']
        
        # El sistema genera hash para el pagador y el cobrador
        hashPagador = Util.sha1(nombrePagador, Billetera.PERSONA, correoPagador, Billetera.PAGAR)
        hashCobrador = Util.sha1(nombreInstitucion, Billetera.ENTIDAD, correoInstitucion, Billetera.COBRAR)
        
        # Aceptación de operación
        aceptacionOperacion = {'correoPagador':correoPagador, 
                               'hashPagador': hashPagador,
                               'confirmadoPagador':false,
                               'correoCobrador': correoCobrador,
                               'hashCobrador': hashCobrador,
                               'confirmadoCobrador': false}
        
        # El sistema almacena el documento de aceptación
        persistencia.inssert(aceptacionOperacion)                               
        
        # El sistema envía correo a el pagador, el cobrador y a PPT
        enviarCorreos(correoPagador, correoCobrador, Billetera.CORREO_PPT, Billetera-CORREO_A_CONFIRMAR)
        
    
    # Un usuario pagador recibe el correo y selecciona el enlace para aceptar 
    # la operación. 
    def procesarHash(self, hash):
        
        # Establece la confirmacion a true
        aceptarSolicitud(hash)
        
        # El sistema verifica si ambas aceptaciones se realizaron.
        verificaDobleConfirmacion(hash)
    
    def verificarDobleConfirmacion(hash):
        p = Persistencia('190.188.234.6', 'admin', 'admin2k14')
        
        
    def aceptarSolicitud(self, hash):
        tipoEntidad = obtenerTipoEntidad(hash)
        
        # Establecer confirmado a true para la entidad en cuestion
        
    def enviarCorreos(self, correoPagador, correoCobrador, correoPPT, tipoCorreo):
        # En caso de ser positivo
        # envía mail informativo a pagador, cobrador y PPT
         # email de paypertic
    
    
        # TODO: Incorporar los mails a un dispatcher
        # TODO: Incorporar manejo de tipo de correo
        
        # Enviamos al mail a la entidad cobradora
        emailEntidadCobradora = EMail(Billetera.SERVIDOR_SMTP, Billetera.SERVIDOR_PUERTO)
        emailEntidadCobradora.sendMailFromTemplate(Billetera.CORREO_REMITENTE,
                                                   correoCobrador,
                                                   '',
                                                   'Correo de confirmación',
                                                   'prueba.mmanto',
                                                   Billetera.CORREO_PASSWORD,
                                                   {'title': 'Por favor seleccione el enlace para confirmar su cuenta en MisPagos',
                                                    'contents': 'Este es el contenido',
                                                    'links': [{'url' : 'www.google.com','label' : 'Ir a google...'}]},
                                                    'frontend/mail_templates/mail.tmpl')
        # Enviamos el mail al pagador
        emailPagador = EMail(Billetera.SERVIDOR_SMTP, Billetera.SERVIDOR_PUERTO)
        emailPagador.sendMailFromTemplate(Billetera.CORREO_REMITENTE,
                                                   correoPagador,
                                                   '',
                                                   'Correo de confirmación',
                                                   'prueba.mmanto',
                                                    Billetera.CORREO_PASSWORD,
                                                   {'title': 'Por favor seleccione el enlace para confirmar su cuenta en MisPagos',
                                                    'contents': 'Este es el contenido',
                                                    'links': [{'url' : 'www.google.com','label' : 'Ir a google...'}]},
                                                    'frontend/mail_templates/mail.tmpl')

        # Enviamos el mail a PPT
        emailPPT=  EMail(Billetera.SERVIDOR_SMTP, Billetera.SERVIDOR_PUERTO)
        emailPPT.sendMailFromTemplate(Billetera.CORREO_REMITENTE,
                                                   Billetera.CORREO_PPT,
                                                   '',
                                                   'Correo de confirmación',
                                                   'prueba.mmanto',
                                                    Billetera.CORREO_PASSWORD,
                                                   {'title': 'Por favor seleccione el enlace para confirmar su cuenta en MisPagos',
                                                    'contents': 'Este es el contenido',
                                                    'links': [{'url' : 'www.google.com','label' : 'Ir a google...'}]},
                                                    'frontend/mail_templates/mail.tmpl')

    

    # Un usuario cobrador recibe el correo y selecciona el enlace para aceptar
    # la operación.
        # El sistema busca el documento de aceptación con el hash 
        # recibido desde el enlace del mail y establece confirmadoCobrador a verdadero
        # El sistema verifica si ambas aceptaciones se realizaron. En caso de ser positivo
        # envía mail informativo a pagador, cobrador y PPT
        
    # Pasado un tiempo determinado si no se realizaron ambas aceptaciones en vía un 
    # mail a ppt brindando info para contactarse.
        