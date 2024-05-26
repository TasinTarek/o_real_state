# -*- coding: utf-8 -*-
# from odoo import http


# class ORealState(http.Controller):
#     @http.route('/o_real_state/o_real_state', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o_real_state/o_real_state/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('o_real_state.listing', {
#             'root': '/o_real_state/o_real_state',
#             'objects': http.request.env['o_real_state.o_real_state'].search([]),
#         })

#     @http.route('/o_real_state/o_real_state/objects/<model("o_real_state.o_real_state"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o_real_state.object', {
#             'object': obj
#         })

