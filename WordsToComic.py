# will need to install these packages, and then for gis follow the instructions in the URL below
# https://pypi.org/project/Google-Images-Search/
from google_images_search import GoogleImagesSearch
import cv2
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
pathToDir = os.path.dirname(os.path.abspath(__file__))

def GenerateComic(word1, word2, word3, phr1, phr2, phr3):
    gis = GoogleImagesSearch('AIzaSyC5Nd7La6m8_NABAuFex3OneBfKEQwOzwc', 'f24b6ddc7bc034296')

    _search_params = {
        'q': '...',
        'num': 1,
        'fileType': 'jpg',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'safe': 'safeUndefined',  ##
        'imgType': 'imgTypeUndefined',  ##
        'imgSize': 'imgSizeUndefined',  ##
        'imgDominantColor': 'imgDominantColorUndefined',
        ##
        'imgColorType': 'imgColorTypeUndefined'  ##
    }
    _search_params['q'] = word1
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir,
               custom_image_name=word1)
    _search_params['q'] = word2
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir,
               custom_image_name=word2)
    _search_params['q'] = word3
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir,
               custom_image_name=word3)

    # add text to images
    addWords(word1, phr1)
    addWords(word2, phr2)
    addWords(word3, phr3)

    # search done. now concatenate images
    img1 = cv2.imread(word1 + '.jpg')
    img2 = cv2.imread(word2 + '.jpg')
    img3 = cv2.imread(word3 + '.jpg')

    os.remove(word1 + '.jpg')
    os.remove(word2 + '.jpg')
    os.remove(word3 + '.jpg')
    os.remove(word1 + word1 + '.jpg')
    os.remove(word2 + word2 + '.jpg')
    os.remove(word3 + word3 + '.jpg')

    comicpictures = cv2.hconcat([img1, img2, img3])
    cv2.imwrite('comicpictures.jpg', comicpictures)


def addWords(word, phrase):
    img1 = Image.open(word + '.jpg')
    draw = ImageDraw.Draw(img1)
    font = ImageFont.truetype("impact.ttf", 20)

    textX = 10
    textY = 10

    draw.text((textX - 2, textY - 2), phrase, (0, 0, 0), font=font)
    draw.text((textX + 2, textY - 2), phrase, (0, 0, 0), font=font)
    draw.text((textX + 2, textY + 2), phrase, (0, 0, 0), font=font)
    draw.text((textX - 2, textY + 2), phrase, (0, 0, 0), font=font)
    draw.text((textX, textY), phrase, (255, 255, 255), font=font)
    img1.save(word + word + '.jpg')
