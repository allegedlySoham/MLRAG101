from pypdf import PdfReader;
reader = PdfReader("cn_introductionv1.pdf");
page = reader.pages[0];
print(page.extract_text());