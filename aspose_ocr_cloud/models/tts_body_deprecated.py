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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from aspose_ocr_cloud.models.language_tts import LanguageTTS
from aspose_ocr_cloud.models.result_type_tts import ResultTypeTTS
from typing import Optional, Set
from typing_extensions import Self

class TTSBodyDeprecated(BaseModel):
    """
    Represents input text data with settings
    """ # noqa: E501
    text: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Gets or Sets text")
    language: LanguageTTS
    result_type: ResultTypeTTS = Field(alias="resultType")
    __properties: ClassVar[List[str]] = ["text", "language", "resultType"]

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
        """Create an instance of TTSBodyDeprecated from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TTSBodyDeprecated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "language": obj.get("language"),
            "resultType": obj.get("resultType")
        })
        return _obj


