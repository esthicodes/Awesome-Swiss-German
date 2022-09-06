import os
import re
import sys
import codecs
import pandas as pd
from sox import Transformer

files = []
SAMPLE_RATE = 16000

source_dir = os.getcwd()
trans_filename = sys.argv[1]

ALLOWED_CHARS = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'ä', 'ö', 'ü',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ',
    #',', ';', ':', '.', '?', '!',
}
WHITESPACE_REGEX = re.compile(r'[ \t]+')

def preprocess_transcript_for_corpus(transcript):
    transcript = transcript.lower()
    transcript = transcript.replace('á', 'a')
    transcript = transcript.replace('à', 'a')
    transcript = transcript.replace('â', 'a')
    transcript = transcript.replace('ç', 'c')
    transcript = transcript.replace('é', 'e')
    transcript = transcript.replace('è', 'e')
    transcript = transcript.replace('ê', 'e')
    transcript = transcript.replace('í', 'i')
    transcript = transcript.replace('ì', 'i')
    transcript = transcript.replace('î', 'i')
    transcript = transcript.replace('ñ', 'n')
    transcript = transcript.replace('ó', 'o')
    transcript = transcript.replace('ò', 'o')
    transcript = transcript.replace('ô', 'o')
    transcript = transcript.replace('ú', 'u')
    transcript = transcript.replace('ù', 'u')
    transcript = transcript.replace('û', 'u')
    transcript = transcript.replace('ș', 's')
    transcript = transcript.replace('ş', 's')
    transcript = transcript.replace('ß', 'ss')
    transcript = transcript.replace('-', ' ')
    # Not used consistently, better to replace with space as well
    transcript = transcript.replace('–', ' ')
    transcript = transcript.replace('/', ' ')
    transcript = WHITESPACE_REGEX.sub(' ', transcript)
    transcript = ''.join([char for char in transcript if char in ALLOWED_CHARS])
    transcript = WHITESPACE_REGEX.sub(' ', transcript)
    transcript = transcript.strip()

    return transcript

with codecs.open(trans_filename, "r", "utf-8") as fin:
    next(fin)
    for line in fin:
        # Parse each segment line
        columns = line.strip().split('\t')
        client_id = columns[0]
        path = columns[1]
        transcript = columns[2]
        transcript = preprocess_transcript_for_corpus(transcript)

        # Convert corresponding FLAC to a WAV
        flac_file = os.path.join(source_dir, 'clips', path)
        wav_file = os.path.join(source_dir, 'clips', path.split('.')[0] + '.wav')

        if not os.path.exists(wav_file):
            tfm = Transformer()
            tfm.set_output_format(rate=SAMPLE_RATE)
            tfm.build(flac_file, wav_file)
            print('Converting flac file {} to wav format {}.'.format(flac_file, wav_file))

        wav_filesize = os.path.getsize(wav_file)
        files.append((client_id, os.path.abspath(wav_file), wav_filesize, transcript))

    df = pd.DataFrame(data=files, columns=["client id", "wav_filename", "wav_filesize", "transcript"])
    # Write sets to disk as CSV files
    df.to_csv(os.path.join(source_dir, trans_filename.split('.')[0]+".csv"), index=False)
