from chunking import chunking;
from textExtraction import extraction;

text = extraction("cn_introductionv1");
print(chunking(text));