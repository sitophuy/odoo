from passlib.handlers.md5_crypt import apr_md5_crypt
from odoo import models, fields, api,exceptions
class Insurrance(models.Model):
    _name = 'benhnhan.insurrance'
    sothe = fields.Char('Số thẻ')
    tungay = fields.Date('Từ ngày')
    denngay = fields.Date('Đến ngày')
    noicap = fields.Char('Nơi cấp')
    DKKCB = fields.Char('Nơi đăng kí')
    dungtuyen = fields.Boolean('Đúng tuyến')
    fieltest = fields.Char('test')
    loaibaohiem = fields.Selection([('bhyt', 'Bảo hiểm y tế'), ('bhdv', 'Bảo hiểm dịch vụ')],string="Loại bảo hiểm", default='bhyt')
    id_patient = fields.Many2one(comodel_name="res.partner", string="Bệnh nhân", required=False, )
