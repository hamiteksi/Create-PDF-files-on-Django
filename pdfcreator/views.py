from __future__ import unicode_literals

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

from .models import Donation

@login_required
def donation_receipt(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id, user=request.user)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "inline; filename={date}-{name}-donation-receipt.pdf".format(
        date=donation.created.strftime('%Y-%m-%d'),
        name=slugify(donation.donor_name),
    )
    html = render_to_string("donations/receipt_pdf.html", {
        'donation': donation,
    })

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response

# def letter_pdf(request, letter_id):
#     letter = get_object_or_404(Letter, pk=letter_id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = (
#         'inline; '
#         f'filename={letter.created:%Y-%m-%d}-letter.pdf'
#     )
#     COMPONENTS = [
#         'letters/pdf/cover.html',
#         'letters/pdf/page01.html',
#         'letters/pdf/page02.html',
#         'letters/pdf/page03.html',
#     ]
#     documents = []
#     font_config = FontConfiguration()
#     for template_name in COMPONENTS:
#         html = render_to_string(template_name, {
#             'letter': letter,
#         })
#         document = HTML(string=html).render(font_config=font_config)
#         documents.append(document)
#
#     all_pages = [page for document in documents for page in document.pages]
#     documents[0].copy(all_pages).write_pdf(response)
#
#     return response