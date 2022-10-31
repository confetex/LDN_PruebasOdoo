# -*- coding: utf-8 -*-
# from odoo import http


# class PruebasGithub(http.Controller):
#     @http.route('/pruebas_github/pruebas_github/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pruebas_github/pruebas_github/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pruebas_github.listing', {
#             'root': '/pruebas_github/pruebas_github',
#             'objects': http.request.env['pruebas_github.pruebas_github'].search([]),
#         })

#     @http.route('/pruebas_github/pruebas_github/objects/<model("pruebas_github.pruebas_github"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pruebas_github.object', {
#             'object': obj
#         })
