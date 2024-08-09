# coding: utf-8

"""
    Aspose OCR Cloud 5.0 API

    Aspose OCR Cloud 5.0 API

    The version of the OpenAPI document: 5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from aspose_ocr_cloud.models.dsr_confidence import DsrConfidence
from aspose_ocr_cloud.models.dsr_mode import DsrMode
from aspose_ocr_cloud.models.language import Language
from aspose_ocr_cloud.models.ocr_region import OCRRegion
from aspose_ocr_cloud.models.result_type import ResultType
from aspose_ocr_cloud.models.result_type_table import ResultTypeTable
from typing import Optional, Set
from typing_extensions import Self

class OCRSettingsRecognizeLabel(BaseModel):
    """
    OCR Process setting for Image recognition
    """ # noqa: E501
    language: Optional[Language] = None
    make_skew_correct: Optional[StrictBool] = Field(default=False, description="Option to enable skew correction algorithm. True by default", alias="makeSkewCorrect")
    make_binarization: Optional[StrictBool] = Field(default=False, description="Option to enable binarization algorithm. False by default", alias="makeBinarization")
    make_spell_check: Optional[StrictBool] = Field(default=False, description="Option to enable spell checking and correction algorithm. False by default", alias="makeSpellCheck")
    make_contrast_correction: Optional[StrictBool] = Field(default=False, description="Option to enable image contrast correction algorithm. True by default", alias="makeContrastCorrection")
    make_upsampling: Optional[StrictBool] = Field(default=False, description="Option to enable image up-sampling algorithm to improve quality. True by default", alias="makeUpsampling")
    dsr_mode: Optional[DsrMode] = Field(default=None, alias="dsrMode")
    dsr_confidence: Optional[DsrConfidence] = Field(default=None, alias="dsrConfidence")
    result_type: Optional[ResultType] = Field(default=None, alias="resultType")
    rotate: Optional[StrictInt] = Field(default=None, description="Rotate image>", alias="Rotate")
    result_type_table: Optional[ResultTypeTable] = Field(default=None, alias="resultTypeTable")
    regions: Optional[List[OCRRegion]] = Field(default=None, description="Region on image to recognize in specific format. Aspose.Ocr.Cloud.Public.OCRRegion")
    __properties: ClassVar[List[str]] = ["language", "makeSkewCorrect", "makeBinarization", "makeSpellCheck", "makeContrastCorrection", "makeUpsampling", "dsrMode", "dsrConfidence", "resultType", "Rotate", "resultTypeTable", "regions"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OCRSettingsRecognizeLabel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in regions (list)
        _items = []
        if self.regions:
            for _item in self.regions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['regions'] = _items
        # set to None if regions (nullable) is None
        # and model_fields_set contains the field
        if self.regions is None and "regions" in self.model_fields_set:
            _dict['regions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OCRSettingsRecognizeLabel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language": obj.get("language"),
            "makeSkewCorrect": obj.get("makeSkewCorrect") if obj.get("makeSkewCorrect") is not None else False,
            "makeBinarization": obj.get("makeBinarization") if obj.get("makeBinarization") is not None else False,
            "makeSpellCheck": obj.get("makeSpellCheck") if obj.get("makeSpellCheck") is not None else False,
            "makeContrastCorrection": obj.get("makeContrastCorrection") if obj.get("makeContrastCorrection") is not None else False,
            "makeUpsampling": obj.get("makeUpsampling") if obj.get("makeUpsampling") is not None else False,
            "dsrMode": obj.get("dsrMode"),
            "dsrConfidence": obj.get("dsrConfidence"),
            "resultType": obj.get("resultType"),
            "Rotate": obj.get("Rotate"),
            "resultTypeTable": obj.get("resultTypeTable"),
            "regions": [OCRRegion.from_dict(_item) for _item in obj["regions"]] if obj.get("regions") is not None else None
        })
        return _obj


