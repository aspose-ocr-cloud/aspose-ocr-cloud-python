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


class OCRUpscaleImageBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Combines Image data and OCR processing settings
    """


    class MetaOapg:
        required = {
            "image",
        }
        
        class properties:
            image = schemas.StrSchema
            __annotations__ = {
                "image": image,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    image: MetaOapg.properties.image
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["image"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["image"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OCRUpscaleImageBody':
        return super().__new__(
            cls,
            *_args,
            image=image,
            _configuration=_configuration,
        )
