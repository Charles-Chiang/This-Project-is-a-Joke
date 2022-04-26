# will need to install these packages, and then for gis follow the instructions in the URL below
# https://pypi.org/project/Google-Images-Search/
from google_images_search import GoogleImagesSearch
import cv2


def main(word1, word2, word3):
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
    gis.search(search_params=_search_params, width=500, height=500)
    image1 = gis.results()[0]
    _search_params['q'] = word2
    gis.search(search_params=_search_params, width=500, height=500)
    image2 = gis.results()[0]
    _search_params['q'] = word3
    gis.search(search_params=_search_params, width=500, height=500)
    image3 = gis.results()[0]

    # search done. now concatenate images
    #img1 = cv2.imread(word1 + '.jpg')
    #img2 = cv2.imread(word2 + '.jpg')
    #img3 = cv2.imread(word3 + '.jpg')

    comicpictures = cv2.hconcat([image1, image2, image3])
    cv2.imwrite('comicpictures.jpg', comicpictures)


# if __name__ == "__main__":
#     main('cat', 'dog', 'fish')
main('cat', 'dog', 'fish')
