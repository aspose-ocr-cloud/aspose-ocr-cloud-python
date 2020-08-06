<img src="testdata/heading.png">

# Aspose OCR Cloud SDK for Python

Aspose OCR Cloud Python SDK is a simple OCR technology, which you can use in your application to convert image to text.

[Aspose.OCR Cloud](https://products.aspose.cloud/ocr/cloud) is a simple SDK used to add text recognition to your app with merely a few lines of code.

In detail, it's a set of SDKs for optical character recognition and document scanning in our Cloud. It supports reading and recognizing text from most commonly used raster image formats. Just pass a specific image to the Aspose.OCR Cloud API, and it will return a response with recognized text.

It is easy to get started with Aspose.OCR Cloud, and there is nothing to install. Create an account at Aspose Cloud and get your application information, then you are ready to use [SDKs](#asposeocr-cloud-sdks)

## Release 20.8:

We are glad to introduce this new Python SDK

## Features:

- Automatic skew correction
- Automatic and manual document layout detection
- Advanced automated image pre-processing
- Extract and recognize text from images via OCR
- Supports multiple international languages
- High speed with no hardware resources

## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we have provided and support [SDKs](#asposeocr-cloud-sdks) in many development languages to make it easier to integrate with us.

## Examples

```python
from asposeocrcloud.configuration import Configuration
from asposeocrcloud.api.ocr_api import OcrApi
configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")
api = OcrApi(configuration)

file_path = r"\your\file\path\5.png"
res = api.post_recognize_from_content(file_path)
print(res.text)
```
_________________________

## Quickstart

Make your solution using [SDK](#asposeocr-cloud-sdks), follow these steps:

#### 1. Get API keys if you haven't

Make a personal account on [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/) and click _Get Keys_. These keys are useful for all Aspose Cloud products. If you have any trouble, look at this [detailed manual](https://docs.aspose.cloud/display/totalcloud/Create+New+App+and+Get+App+Key+and+SID).

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

||||||||||
|--------------|----------|-------|-------|-------|---------|---------|----------|-------|
|[.NET & Core](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-dotnet)|[Java](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-java)|PHP|Ruby|[Python](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-python)|Node.js|[Android](https://github.com/aspose-ocr-cloud/aspose-ocr-cloud-android)|Objective-C|Perl|

## Resources

- **Website:** [https://www.aspose.cloud](https://www.aspose.cloud)
- **Product Home:** [Aspose.OCR Cloud](https://products.aspose.cloud/ocr/family)
- **Documentation:** [Aspose.OCR Cloud Documentation](https://docs.aspose.cloud/display/ocrcloud/Home)
- **Forum:** [Aspose.OCR Cloud Forum](https://forum.aspose.cloud/c/ocr)
- **Blog:** [Aspose.OCR Cloud Blog](https://blog.aspose.cloud/category/ocr/)
- **Pricing:** [Aspose Cloud Pricing](https://purchase.aspose.cloud/pricing)
- **Try out Aspose OCR online for free** [Aspose Image to Text](https://products.aspose.app/ocr/scan-image).