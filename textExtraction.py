from pypdf import PdfReader;
def extraction(pdfname):
    pdfname+=".pdf";
    reader = PdfReader(pdfname);
    text = ""
    for i in range(0,reader.get_num_pages()):
        page = reader.pages[i]
        text+=(page.extract_text());
    return text;
