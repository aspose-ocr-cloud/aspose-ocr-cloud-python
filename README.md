![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-ocr-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-ocr-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-ocr-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-ocr-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-ocr-cloud/aspose-ocr-cloud-python)](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-ocr-Cloud/aspose-ocr-cloud-python)

# Python Cloud REST API for OCR
Aspose OCR Cloud Android SDK is a simple OCR technology, which you can use in your application to convert image to text.
[Aspose.OCR Cloud](https://products.aspose.cloud/ocr/cloud) is a simple SDK used to add text recognition to your app with merely a few lines of code.
In detail, it's a set of SDKs for optical character recognition and document scanning in our Cloud. It supports reading and recognizing text from most commonly used raster image formats. Just pass a specific image to the Aspose.OCR Cloud API, and it will return a response with recognized text.

It is easy to get started with Aspose.OCR Cloud, and there is nothing to install. Create an account at Aspose Cloud and get your application information, then you are ready to use [SDKs](#asposeocr-cloud-sdks)

## Try Online
[Image to Text](https://products.aspose.app/ocr/scan-image) | [Image to Searchable PDF](https://products.aspose.app/ocr/ocr-to-pdf) | [PDF OCR](https://products.aspose.app/ocr/pdf-ocr)| [Receipt Scanner](https://products.aspose.app/ocr/scan-receipt)
:---: | :---: | :---:| :---:
[![Scan Image](https://products.aspose.app/ocr/scan-image/img/ocr-recognize-48.png)](https://products.aspose.app/ocr/scan-image) | [![Image to Searchable PDF](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-4-48.png)](https://products.aspose.app/ocr/ocr-to-pdf) | [![PDF OCR](https://products.aspose.app/ocr/scan-image/img/ocr-to-pdf-2-48.png)](https://products.aspose.app/ocr/pdf-ocr) | [![Receipt Scanner](https://products.aspose.app/ocr/scan-image/img/aspose-scan-receipt-48.png)](https://products.aspose.app/ocr/scan-receipt) 


## Release 21.09
Added new recognition languages: Bengali, Tibetan, Thai, Urdu, Turkish, Korean, Indonesian, Hebrew, Javanese, Greek, Japanese, Persian


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

	ocr_api = asposeocrcloud.OcrApi('MY_CLIENT_SECRET', 'MY_CLIENT_ID')

	file_path = r"\your\file\path\sample.png"
	res = ocr_api.post_recognize_from_content(file_path)
	print(res.text)
```
_________________________

## Quickstart

Make your solution using [SDK](#asposeocr-cloud-sdks), follow these steps:

#### 1. Get API keys if you haven't

Make a personal account on [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/) and click _Get Keys_. These keys are useful for all Aspose Cloud products. If you have any trouble, look at this [detailed manual](https://docs.aspose.cloud/total/create-new-app-and-get-app-key-and-sid/).

#### 2. Run Demo

  * Checkout the SDK or get from [pip](https://pypi.org/project/aspose-ocr-cloud/) (pip install aspose-ocr-cloud)
  * Set Your AppSid & AppKey
  * Run Python console [Demo](./demo/run.py) or [UnitTests](./test/test_ocr_api.py)


<p align="center">
  <a title="Download ZIP" href="https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python/archive/master.zip">
     <img src="testdata/download.png" />
  </a>
</p>

---------------------------

### Structure

This project includes:   
- Python console demo application - "[./demo](./demo/run.py)"
- Module "asposeocrcloud" - this is SDK located in "[./asposeocrcloud](asposeocrcloud)". You can integrate it in your application. It contains both OCR and [Aspose.Storage](https://github.com/aspose-storage-cloud/) API
- Module "test" - "[./test](./test)" UnitTest. You can take a look at them to see various code examples.
- Module "demo" - "[./demo](./demo)" Sample console demo project.
- Folder "docs" - "[./docs](./docs)" Full documentation for Aspose.OCR SDK in HTML format.

### Dependencies
- [See requirements.txt](./requirements.txt)
_________________________


## Aspose.OCR Cloud SDKs

||||||
|--------------|----------|-------|---------|---------|
|[.NET & Core](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-dotnet)|[Java](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-java)|[Python](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python)|[Node.js](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs)|[Android](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-android)


[Product Page](https://products.aspose.cloud/ocr/) | [Documentation](https://docs.aspose.cloud/display/ocrcloud/Home) | [API Reference](https://apireference.aspose.cloud/ocr/) | [Code Samples](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-nodejs) | [Blog](https://blog.aspose.cloud/category/ocr/) | [Free Support](https://forum.aspose.cloud/c/ocr) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
