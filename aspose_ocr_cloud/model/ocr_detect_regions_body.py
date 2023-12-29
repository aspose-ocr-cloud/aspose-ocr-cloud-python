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


class OCRDetectRegionsBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "image",
            "settings",
        }
        
        class properties:
            image = schemas.StrSchema
        
            @staticmethod
            def settings() -> typing.Type['OCRSettingsDetectRegions']:
                return OCRSettingsDetectRegions
            __annotations__ = {
                "image": image,
                "settings": settings,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    image: MetaOapg.properties.image
    settings: 'OCRSettingsDetectRegions'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'OCRSettingsDetectRegions': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["image"], typing_extensions.Literal["settings"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> 'OCRSettingsDetectRegions': ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["image"], typing_extensions.Literal["settings"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, str, ],
        settings: 'OCRSettingsDetectRegions',
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OCRDetectRegionsBody':
        return super().__new__(
            cls,
            *_args,
            image=image,
            settings=settings,
            _configuration=_configuration,
        )

from aspose_ocr_cloud.model.ocr_settings_detect_regions import OCRSettingsDetectRegions
