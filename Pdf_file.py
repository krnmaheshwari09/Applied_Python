import pypdf as py

new_pdf = open("ECS form.pdf", "rb")
reading_pdf = py.PdfReader(new_pdf)
print(reading_pdf._get_num_pages())
pdf_pages = reading_pdf._get_page(0)
print(pdf_pages.extract_text())
new_pdf.close()
