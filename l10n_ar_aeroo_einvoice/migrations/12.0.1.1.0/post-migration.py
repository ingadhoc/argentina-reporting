from openupgradelib import openupgrade
from odoo.modules.module import get_module_resource
import base64


@openupgrade.migrate()
def migrate(env, version):
    aeroo_report = env.ref('l10n_ar_aeroo_einvoice.action_aeroo_report_ar_einvoice', raise_if_not_found=False)
    if aeroo_report:
        default_reports = ['l10n_ar_aeroo_einvoice/einvoice_with_footer.odt', 'l10n_ar_aeroo_einvoice/einvoice.odt']
        if aeroo_report.tml_source == 'file' and aeroo_report.report_file in default_reports:
            new_background = get_module_resource('l10n_ar_aeroo_einvoice', 'einvoice.png')
            file_content = open(new_background, 'rb').read()
            aeroo_report.background_image = base64.b64encode(file_content)
