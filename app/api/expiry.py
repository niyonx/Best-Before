from google.cloud import vision
import os
# import dateparser
# import datefinder
# from dateutil.parser import parse

from dateparser.search import search_dates


# set path to api key here
""" INPUT PATH TO JSON API KEY"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"

def detect_text(path):
    """Detects text in the file."""
    
    # path = 

    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:')

    out = texts[0].description

    # for text in texts:
    #     print('\n"{}"'.format(text.description))

    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                 for vertex in text.bounding_poly.vertices])

    #     print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return out

# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225640.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225652.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225703.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225750.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225759.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225824.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225846.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225945.jpg"))

# REGEX = (?:\d{2}(?:\d{2})?(?: *)[\/:\-,_.]?(?: *))?\d{2}(?: *)[\/:\-,_.]?(?: *)\d{2}(?:\d{2})?

string_with_dates = '''
    2021 MR04
BZ21008 Y

0044598AA
B.B./M.A.2021 MA 13

BEST BEFORE HEILLEUR AVANT
2021 MA 28

2021JL31
K4 20:06
BEST BEFORE/MEILLEUR AVANT

TOSRLSA3120235
REST BEFORE
2021 00 31
NEILLEUR AVANT

BB/MA 2021 OC 18 B

2021 AL14
16:10 M17

606) 05 MR
'''

# matches = datefinder.find_dates(string_with_dates)
# for match in matches:
#     print(match)

# print(parse("2021 MA 28", fuzzy_with_tokens=True))

# dates = search_dates('Central design committee session Tuesday 10/22 6:30 pm')
# print(dates)
