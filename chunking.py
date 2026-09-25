def chunking(text):
    length = len(text);
    chunkSize = 500;
    overlap = 50;
    chunk = [];
    if(length>chunkSize):
        start = 0;
        while(start<length):
            chunk.append(text[start:start+chunkSize])
            start +=chunkSize-overlap
    else: chunk.append(text[0:length])
    chunk = [c for c in chunk if c != ""];
    return chunk;
