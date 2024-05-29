import argparse
import fugashi
from googletrans import Translator

# This is our sample text.
# "Fugashi" is a Japanese snack primarily made of gluten.
#text = "空にある何かを見つめてたら12cars"
# The Tagger object holds state about the dictionary. 

#空にある何かを見つめてたらそれは星だって君がおしえてくれたまるでそれは僕らみたいに
def parse_arguments():
    parser = argparse.ArgumentParser(description="Splits a sentence into multiple chunks")
    parser.add_argument('query', type=str, help='The sentence to split')

    args = parser.parse_args()

    return args.query.strip()

def translate_japanese_to_korean(sentence):
    translator = Translator()
    translation = translator.translate(sentence, src='ja', dest='ko')
    return translation.text

if __name__ == "__main__":
    query = parse_arguments()

    tagger = fugashi.Tagger()

    words = [word for word in tagger(query)]

    splitter = ['助詞', '助動詞', '動詞'] #조사, 조동사
    chuncks = ['']
    slice_next = False
    for i, word in enumerate(words):
        if word.feature.pos1 in splitter:
            if word.feature.pos1 == '動詞':
                chuncks.append(word.surface)
            else:
                chuncks[-1] += word.surface
            slice_next  =  True
        else:
            if slice_next:
                chuncks.append(word.surface)
                slice_next = False
            else:
                chuncks[-1] += word.surface

    print(chuncks)
    #print(translate_japanese_to_korean(query))