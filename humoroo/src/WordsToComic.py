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
    gis = GoogleImagesSearch('AIzaSyBGMs0t-CExOqJ7IVQvL_k8Z65l26kaViI', 'f24b6ddc7bc034296')

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
    print(pathToDir)
    _search_params['q'] = word1
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir)
    print(gis.results()[0])
    word1Loc = gis.results()[0].path.split('\\')[-1]

    _search_params['q'] = word2
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir)
    print(gis.results()[0])
    word2Loc = gis.results()[0].path.split('\\')[-1]

    _search_params['q'] = word3
    gis.search(search_params=_search_params, width=500, height=500, path_to_dir=pathToDir)
    print(gis.results()[0])
    word3Loc = gis.results()[0].path.split('\\')[-1]

    # add text to images
    addWords(word1Loc, phr1, '1')
    addWords(word2Loc, phr2, '2')
    addWords(word3Loc, phr3, '3')

    # search done. now concatenate images
    img1 = cv2.imread('1.png')
    img2 = cv2.imread('2.png')
    img3 = cv2.imread('3.png')

    os.remove(word1Loc)
    os.remove(word2Loc)
    os.remove(word3Loc)
    os.remove('1.png')
    os.remove('2.png')
    os.remove('3.png')

    comicpictures = cv2.hconcat([img1, img2, img3])
    cv2.imwrite('comicpictures.jpg', comicpictures)

#shamelessly stolen from https://blog.lipsumarium.com/caption-memes-in-python/
def addWords(word, phrase, num):
    img = Image.open(word)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("impact.ttf", 50)

    textX = 10
    textY = 10

    draw.text((textX - 2, textY - 2), phrase, (0, 0, 0), font=font)
    draw.text((textX + 2, textY - 2), phrase, (0, 0, 0), font=font)
    draw.text((textX + 2, textY + 2), phrase, (0, 0, 0), font=font)
    draw.text((textX - 2, textY + 2), phrase, (0, 0, 0), font=font)
    draw.text((textX, textY), phrase, (255, 255, 255), font=font)
    # print("wrote words successfully!")
    img.save(num + '.png')

#GenerateComic("samoyed","cat","steak","it's a dog","it's a cat","roasty toasty")
