import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='-cR57pDRHtkYXX69bT4SKZ2s1e2DUlOK1-vd3eY6qkkj')

with open('./image2.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='DefaultCustomModel_1565289978').get_result()
print(json.dumps(classes, indent=2))