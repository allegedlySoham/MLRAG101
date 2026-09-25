from chunking import chunking;
from textExtraction import extraction;
from similarity import cosine_similarity;
from embedding import embed;
text = extraction("cn_introductionv1");
chunks = [c for c in chunking(text) if c];
embeddedChunks = [embed(c)for c in chunks];
print(len(chunks))
print(len(embeddedChunks));
