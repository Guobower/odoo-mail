# -*- coding: utf-8 -*-
###############################################################################
#
#   email_template_header for OpenERP
#   Copyright (C) 2012 Akretion Florian da Costa <florian.dacosta@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp.osv import fields, orm

class MailMail(orm.Model):
    _inherit = 'mail.mail'

    def create(self, cr, uid, vals, context=None):
        if context.get('use_mail_header_id', False) \
                and vals.get('body_html', False):
            header_obj = self.pool['email.header']
            header = header_obj.browse(cr, uid,
                        context.get('use_mail_header_id'), context=context)
            body = header.header_footer_html.replace('#{body}', vals.get('body_html'))
            vals['body_html'] = body
        res = super(MailMail,self).create(cr, uid, vals, context)
        return res



