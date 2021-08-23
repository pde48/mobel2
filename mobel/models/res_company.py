# -*- coding: utf-8 -*-

from datetime import timedelta, datetime, date
import calendar
from dateutil.relativedelta import relativedelta

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError, RedirectWarning
from odoo.tools.misc import format_date
from odoo.tools.float_utils import float_round, float_is_zero
from odoo.tests.common import Form


class ResCompany(models.Model):
    _inherit = "res.company"

    is_company_managment_sales_mobel = fields.Boolean(string='Mobel Sales Magento',default=False )
    is_company_managment_purchase_mobel = fields.Boolean(string='Mobel Purchases Magento',default=False )
