import asposeocrcloud.api.storage_api
from asposeocrcloud.configuration import Configuration
from asposeocrcloud.api.ocr_api import OcrApi
from asposeocrcloud.models import OCRRect, OCRRegion, OCRRequestData, OCRRequestDataStorage, LanguageGroup


def ocr_from_url(configuration):
    # Instantiate API Class
    api = OcrApi(configuration)
    params = Parameters(LanguageGroup.ENGLISH, ResultType.Text, False, False, DSRPipeline.DsrNoFilter,
                        DSRConfidence.Mid, False)
    # Send request (Only English language supported for this request type)
    res = api.post_recognize_from_url("https://upload.wikimedia.org/wikipedia/commons/2/2f/Book_of_Abraham_FirstPage.png", params)
    print(res.text)


def ocr_send_file(configuration):
    # Instantiate API Class
    api = OcrApi(configuration)
    params = Parameters(LanguageGroup.ENGLISH, ResultType.Text, False, False, DSRPipeline.DsrNoFilter,
                        DSRConfidence.Mid, False)
    # Send request (Only English language supported for this request type)
    res = api.post_recognize_from_content(r"..\testdata\de_1.jpg",params)
    print(res.text)


def ocr_from_aspose_storage(configuration):
    # Instantiate Storage API Class

    api_storage = asposeocrcloud.api.storage_api.StorageApi(configuration)
    # Upload file to storage
    api_storage.upload_file("5.png", r"..\testdata\5.png")
    params = Parameters(LanguageGroup.ENGLISH, ResultType.Text, False, False, DSRPipeline.DsrNoFilter,
                        DSRConfidence.Mid, False)
    # Instantiate OCR API Class
    api_ocr = OcrApi(configuration)
    # Send request (Only English language supported for this request type)
    res = api_ocr.get_recognize_from_storage("5.png",params)
    print(res.text)


def ocr_regions_from_url(configuration):
    # choose url of image to recognize
    url = "https://iili.io/JP2HFf.png"
    # setup regions of image to recognize
    regions = [
        OCRRegion(OCRRect(243, 308, 2095, 964), 0),
        OCRRegion(OCRRect(240, 1045, 2108, 1826), 1),
        OCRRegion(OCRRect(237, 1916, 2083, 3180), 2),
    ]
    # Set options: Regions, Recognition language and Skew corrector
    request_data = OCRRequestData(regions=regions,
                                  language=LanguageGroup.ENGLISH,
                                  make_skew_correct=False)
    # Instantiate OCR API Class
    api_ocr = OcrApi(configuration)
    # Send request
    res = api_ocr.post_recognize_regions_from_url(request_data, url)  # type: OcrResponse
    print(res.text)


def ocr_regions_of_local_file(configuration):
    # Instantiate Storage API Class
    api_storage = asposeocrcloud.api.storage_api.StorageApi(configuration)
    # Upload file to storage
    api_storage.upload_file("5.png", r"..\testdata\5.png")

    # setup regions of image to recognize
    regions = [
        OCRRegion(OCRRect(243, 308, 2095, 964), 0),
        OCRRegion(OCRRect(240, 1045, 2108, 1826), 1),
        OCRRegion(OCRRect(237, 1916, 2083, 3180), 2),
    ]
    # Set options: Regions, Recognition language and Skew corrector
    request_data = OCRRequestDataStorage(regions=regions,
                                         language=LanguageGroup.ENGLISH,
                                         make_skew_correct=False,
                                         file_name="5.png")
    # Instantiate OCR API Class
    api_ocr = OcrApi(configuration)
    # Send request
    res = api_ocr.post_recognize_regions_from_storage(request_data)  # type: OcrResponse
    print(res.text)


def ocr_regions_using_apose_storage(configuration):
    # image to recognize
    file_path = r"..\testdata\5.png"
    # setup regions of image to recognize
    regions = [
        OCRRegion(OCRRect(243, 308, 2095, 964), 0),
        OCRRegion(OCRRect(240, 1045, 2108, 1826), 1),
        OCRRegion(OCRRect(237, 1916, 2083, 3180), 2),
    ]
    # Set options: Regions, Recognition language and Skew corrector
    request_data = OCRRequestData(regions=regions,
                                  language=LanguageGroup.ENGLISH,
                                  make_skew_correct=False)
    # Instantiate OCR API Class
    api_ocr = OcrApi(configuration)
    # Send request
    res = api_ocr.post_recognize_regions_from_content(request_data, file_path)  # type: OcrResponse
    print(res.text)


if __name__ == '__main__':
    # setup your APPSID & APPKEY
    configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                                  appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")
    ocr_from_url(configuration)
    ocr_send_file(configuration)
    ocr_from_aspose_storage(configuration)
    ocr_regions_from_url(configuration)
    ocr_regions_of_local_file(configuration)
    ocr_from_aspose_storage(configuration)
