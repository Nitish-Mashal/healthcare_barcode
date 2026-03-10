import frappe
import barcode
from barcode.writer import ImageWriter
import base64
from io import BytesIO


def generate_sample_barcode(doc, method):

    if not doc.name:
        return

    CODE128 = barcode.get_barcode_class("code128")
    code = CODE128(str(doc.name), writer=ImageWriter())

    buffer = BytesIO()
    code.write(buffer)

    barcode_base64 = "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()

    frappe.db.set_value(
        "Sample Collection",
        doc.name,
        "custom_barcode_html",
        barcode_base64
    )