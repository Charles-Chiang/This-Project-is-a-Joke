# will need to install these packages, and then for gis follow the instructions in the URL below
# https://pypi.org/project/Google-Images-Search/
from google_images_search import GoogleImagesSearch
import cv2

def main(word1, word2, word3):
    gis = GoogleImagesSearch('116837858877556455072', 'f24b6ddc7bc034296')

    _search_params = {
        'q': '...',
        'num': 1,
        'fileType': 'jpg',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'safe': 'active|high|medium|off|safeUndefined',  ##
        'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined',  ##
        'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined',  ##
        'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined',
        ##
        'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined'  ##
    }
    _search_params['q'] = word1
    gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500, custom_image_name=word1)
    _search_params['q'] = word2
    gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500, custom_image_name=word2)
    _search_params['q'] = word3
    gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500, custom_image_name=word3)

    # search done. now concatenate images
    img1 = cv2.imread(word1 + '.jpg')
    img2 = cv2.imread(word2 + '.jpg')
    img3 = cv2.imread(word3 + '.jpg')

    comicpictures = cv2.hconcat([img1, img2, img3])
    cv2.imwrite('comicpictures.jpg', comicpictures)



