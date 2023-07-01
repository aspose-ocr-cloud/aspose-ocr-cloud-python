![](https://img.shields.io/badge/api-v5.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-ocr-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-ocr-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-ocr-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-ocr-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-ocr-cloud/aspose-ocr-cloud-python)](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-ocr-Cloud/aspose-ocr-cloud-python)

# Python Cloud REST API for OCR
Aspose OCR Cloud Android SDK is a simple OCR technology, which you can use in your application to convert image to text.
[Aspose.OCR Cloud](https://products.aspose.cloud/ocr/cloud) is a simple SDK used to add text recognition to your app with merely a few lines of code.
In detail, it's a set of SDKs for optical character recognition and document scanning in our Cloud. It supports reading and recognizing text from most commonly used raster image formats. Just pass a specific image to the Aspose.OCR Cloud API, and it will return a response with recognized text.

It is easy to get started with Aspose.OCR Cloud, and there is nothing to install. Create an account at Aspose Cloud and get your application information, then you are ready to use [SDKs](#asposeocr-cloud-sdks)

## Try Online
[Image to Text](https://products.aspose.app/ocr/scan-image) | [Image to Searchable PDF](https://products.aspose.app/ocr/ocr-to-pdf) | [PDF OCR](https://products.aspose.app/ocr/pdf-ocr)| [Receipt Scanner](https://products.aspose.app/ocr/scan-receipt)
:---: | :---: | :---:| :---:
[![Scan Image](https://products.aspose.app/ocr/scan-image/img/ocr-recognize-48.png)](https://products.aspose.app/ocr/scan-image) | [![Image to Searchable PDF](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-4-48.png)](https://products.aspose.app/ocr/ocr-to-pdf) | [![PDF OCR](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-2-48.png)](https://products.aspose.app/ocr/pdf-ocr) | [![Receipt Scanner](https://products.aspose.app/ocr/scan-image/img/aspose-scan-receipt-48.png)](https://products.aspose.app/ocr/scan-receipt) 

## What was changed in version 23.6.0

A summary of recent changes, enhancements and bug fixes in **Aspose.OCR Cloud SDK for Python 23.6.0** release:

Key | Summary | Category
--- | ------- | --------
OCR-2893 | Detecting fonts and styles in scans or photographs. | New feature
OCR-3454 | Extracting text from photographed signboards, price tags, plates, food labels, and similar images. | New feature
n/a | Conversion of DjVu files to PDF documents. | New feature
n/a | Image processing APIs were made easier and more consistent: <ul><li>[Skew correction](https://docs.aspose.cloud/ocr/deskew-image/);</li><li>[Dewarping](https://docs.aspose.cloud/ocr/dewarp-image/);</li><li>[Upsampling](https://docs.aspose.cloud/ocr/upsample-image/);</li><li>[Binarization](https://docs.aspose.cloud/ocr/binarize-image/).</li></ul> | Enhancement
n/a | Reworked [text-to-speech conversion](https://docs.aspose.cloud/ocr/text-to-speech/) API. | Enhancement

REST API changes:

- https://releases.aspose.cloud/ocr/release-notes/2023/aspose-ocr-cloud-23-5-0-release-notes/
- https://releases.aspose.cloud/ocr/release-notes/2023/aspose-ocr-cloud-23-6-0-release-notes/

### Deprecation warning

Updated image processing and text-to-speech conversion APIs are not backward compatible. To make code updates easier, previous APIs remain fully functional. All of your existing code will continue to work and you can even make minor updates to it, but be aware that all deprecated endpoints are planned to be removed in upcoming releases in favor of the new API.
## Features
- Automated skew correction
- Automated and manual document layout detection
- Recognize documents with complex layouts in fully automatic mode or with manual corrections.
- Extract and recognize text from images via OCR
- Supports multiple international languages
- High speed with no hardware resources
- Receipt recognition
- Table image recognition
- Supports PDF Recognition
- Text correction using spell checking algorithms
- Various output formats: Text, Searchable PDF, hOCR, Excel for tables.

## Recognize text of different languages
Aspose.OCR Cloud supports 38 languages including English, German, French, Italian, Spanish, Portuguese, Polish, Slovene, Slovak, Netherlands, Lithuanian, Latvian, Danish, Norwegian, Finnish, Serbian, Croatian, Czech, Swedish, Estonian, Romanian, Chinese, Arabic, Hindi, Russian, Ukrainian, Bengali, Tibetan, Thai, Urdu, Turkish, Korean, Indonesian, Hebrew, Javanese, Greek, Japanese, Persian and a lot of other works too.

## Save OCR As
TXT, PDF, HOCR

## Read OCR Formats
BMP, JPG, GIF, PNG, TIFF

## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we have provided and support [SDKs](#asposeocr-cloud-sdks) in many development languages to make it easier to integrate with us.

## OCR in Python

```python
# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).

	
    with aspose_ocr_cloud.ApiClient(config) as api_client:
        # Create an instance of the API class
        api_instance = recognize_image_api.RecognizeImageApi(api_client)

        # Read image file and conver it into base64 string
        image_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../samples/latin.png')

        # Create request body
        body = OCRRecognizeImageBody(
            image=utils.file_to_base64(image_file_path),
            settings=OCRSettingsRecognizeImage(
                language=Language("English"),
                makeSkewCorrect=False,
                makeBinarization=False,
                makeSpellCheck=False,
                makeContrastCorrection=False,
                makeUpsampling=False,
                dsrMode=DsrMode("NoDsrNoFilter"),
                dsrConfidence=DsrConfidence("Default"),
                resultType=ResultType("Text")
            ),
        )
        try:
            # Step 1: perform post request
            task_id_response = api_instance.post_recognize_image(
                body=body,
            )
            task_id = task_id_response.body
            print(f'Your task ID is {task_id}')

            # Step 2: perform get result request
            task_response : OCRResponse = api_instance.get_recognize_image(
                query_params={'id':task_id}
            )
            assert task_response.response.status == 200
            assert task_response.body['taskStatus'] == 'Completed'
            recognized_text_raw = task_response.body['results'][0]['data']
            recognized_text = bytearray(base64.b64decode(str(recognized_text_raw))).decode('utf-8')
            print (f'Recognized text:\n{recognized_text}')
            print (f'Task completed.Press Enter to continue')
            input()

        except aspose_ocr_cloud.ApiException as e:
            print("Exception when calling RecognizeImageApi: %s\n" % e)
```
_________________________

## Quickstart

Make your solution using [SDK](#asposeocr-cloud-sdks), follow these steps:

#### 1. Get API keys if you haven't

Make a personal account on [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/) and click _Get Keys_. These keys are useful for all Aspose Cloud products. If you have any trouble, look at this [detailed manual](https://docs.aspose.cloud/total/create-new-app-and-get-app-key-and-sid/).

#### 2. Run Demo

  * Checkout the SDK or get from [pip](https://pypi.org/project/aspose-ocr-cloud/) (pip install aspose-ocr-cloud)
  * Set Your AppSid & AppKey
  * Run Python console [Demo](./Example/run.py)


<p align="center">
  <a title="Download ZIP" href="https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/archive/master.zip">
     <img src="testdata/download.png" />
  </a>
</p>

---------------------------

### Structure

This project includes:   
- Python console demo application - "[./example](./example/run.py)"
- Module "asposeocrcloud" - this is SDK located in "[./asposeocrcloud](asposeocrcloud)". You can integrate it in your application.
- Module "test" - "[./test](./test)" UnitTest. You can take a look at them to see various code examples.
- Folder "docs" - "[./docs](./docs)" Full documentation for Aspose.OCR SDK in HTML format.

### Dependencies
- [See requirements.txt](./requirements.txt)
_________________________


## Aspose.OCR Cloud SDKs

||||||
|--------------|----------|-------|---------|---------|
|[.NET & Core](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-dotnet)|[Java](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-java)|[Python](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python)|[Node.js](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs)|[Android](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-android)


[Product Page](https://products.aspose.cloud/ocr/) | [Documentation](https://docs.aspose.cloud/display/ocrcloud/Home) | [API Reference](https://apireference.aspose.cloud/ocr/) | [Code Samples](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs) | [Blog](https://blog.aspose.cloud/category/ocr/) | [Free Support](https://forum.aspose.cloud/c/ocr) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
