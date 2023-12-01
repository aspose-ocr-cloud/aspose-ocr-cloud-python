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


class DsrConfidence(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Region filtering threshold. Filtering by the algorithm confidence scale. Higher mode - more aggressive filtering. Default == Medium
    """
    
    @schemas.classproperty
    def DEFAULT(cls):
        return cls("Default")
    
    @schemas.classproperty
    def LOW(cls):
        return cls("Low")
    
    @schemas.classproperty
    def LOW_MID(cls):
        return cls("LowMid")
    
    @schemas.classproperty
    def MID(cls):
        return cls("Mid")
    
    @schemas.classproperty
    def MID_HIGH(cls):
        return cls("MidHigh")
    
    @schemas.classproperty
    def HIGH(cls):
        return cls("High")
    
    @schemas.classproperty
    def ULTRA(cls):
        return cls("Ultra")
    
    @schemas.classproperty
    def ALL(cls):
        return cls("All")
