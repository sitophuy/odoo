from passlib.handlers.md5_crypt import apr_md5_crypt
from odoo import models, fields, api,exceptions
class Patient(models.Model):
    _inherit = 'res.partner'
    is_patient = fields.Boolean("Là bệnh nhân", default=True)
    address = fields.Char('Địa chỉ',compute='_address',default="Địa chỉ")
    idpatient = fields.Char('Mã bệnh nhân',required=False,default ="00000000")
    dantoc = fields.Char('Dân tộc', default = 'Kinh')
    quoctich = fields.Char('Quốc tịch', default ="Việt Nam")
    maxidpatient =fields.Integer("Số tối đa",default=lambda self: self.env['ir.sequence'].next_by_code('idpatient'))
    image = fields.Binary("Hình ảnh")
    quanhe = fields.Many2many(comodel_name="res.partner", relation="moiquanhe", column1="name", column2="address", string="Dịa chỉ", )
    insurrance = fields.One2many(comodel_name="benhnhan.insurrance", inverse_name="id_patient", string="Bảo hiểm", required=False, )
    _sql_constraints = [('idpatient_unique','unique(idpatient)','Mã Nhân viên là duy nhất')]
    @api.multi
    @api.depends("street", "city","state_id","country_id","street2")
    def _address(self):
        for ad in self:
            if ad.address is False:
                ad.address =""
            if ad.street:
                ad.address =str(ad.address) + str(ad.street)
            if ad.street2:
                ad.address =str(ad.address) + " - "+str(ad.street2)
            if ad.city:
                ad.address =str(ad.address) + " - "+str(ad.city)
            if ad.state_id:
                ad.address =str(ad.address) + " - "+str(ad.state_id.name)
            if ad.country_id:
                ad.address = str(ad.address) + " - "+str(ad.country_id.name)
            # ad.address = str(ad.street) + str(ad.street2) + str(ad.city) + str(ad.state_id) + ad.country_id