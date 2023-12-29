# coding: utf-8

"""
    Aspose OCR Cloud 5.0 API

    Aspose OCR Cloud 5.0 API  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from aspose_ocr_cloud import schemas  # noqa: F401


class ResultTypeTable(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Result document type for Table OCR process
    """


    class MetaOapg:
        enum_value_to_name = {
            "Text": "TEXT",
            "Excel": "EXCEL",
            "Csv": "CSV",
            "CsvAndExcel": "CSV_AND_EXCEL",
        }
    
    @schemas.classproperty
    def TEXT(cls):
        return cls("Text")
    
    @schemas.classproperty
    def EXCEL(cls):
        return cls("Excel")
    
    @schemas.classproperty
    def CSV(cls):
        return cls("Csv")
    
    @schemas.classproperty
    def CSV_AND_EXCEL(cls):
        return cls("CsvAndExcel")