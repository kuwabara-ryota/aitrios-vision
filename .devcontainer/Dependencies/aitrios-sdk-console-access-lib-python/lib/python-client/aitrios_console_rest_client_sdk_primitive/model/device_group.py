# coding: utf-8

"""
    AITRIOS | Console

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.1.0
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

from aitrios_console_rest_client_sdk_primitive import schemas  # noqa: F401


class DeviceGroup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            device_group_id = schemas.StrSchema
            device_type = schemas.StrSchema
            comment = schemas.StrSchema
            ins_id = schemas.StrSchema
            ins_date = schemas.StrSchema
            upd_id = schemas.StrSchema
            upd_date = schemas.StrSchema
            
            
            class devices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                device_id = schemas.StrSchema
                                place = schemas.StrSchema
                                comment = schemas.StrSchema
                                ins_id = schemas.StrSchema
                                ins_date = schemas.StrSchema
                                upd_id = schemas.StrSchema
                                upd_date = schemas.StrSchema
                                __annotations__ = {
                                    "device_id": device_id,
                                    "place": place,
                                    "comment": comment,
                                    "ins_id": ins_id,
                                    "ins_date": ins_date,
                                    "upd_id": upd_id,
                                    "upd_date": upd_date,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["place"]) -> MetaOapg.properties.place: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ins_id"]) -> MetaOapg.properties.ins_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ins_date"]) -> MetaOapg.properties.ins_date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["upd_id"]) -> MetaOapg.properties.upd_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["upd_date"]) -> MetaOapg.properties.upd_date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_id", "place", "comment", "ins_id", "ins_date", "upd_id", "upd_date", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["place"]) -> typing.Union[MetaOapg.properties.place, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ins_id"]) -> typing.Union[MetaOapg.properties.ins_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ins_date"]) -> typing.Union[MetaOapg.properties.ins_date, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["upd_id"]) -> typing.Union[MetaOapg.properties.upd_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["upd_date"]) -> typing.Union[MetaOapg.properties.upd_date, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_id", "place", "comment", "ins_id", "ins_date", "upd_id", "upd_date", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            device_id: typing.Union[MetaOapg.properties.device_id, str, schemas.Unset] = schemas.unset,
                            place: typing.Union[MetaOapg.properties.place, str, schemas.Unset] = schemas.unset,
                            comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
                            ins_id: typing.Union[MetaOapg.properties.ins_id, str, schemas.Unset] = schemas.unset,
                            ins_date: typing.Union[MetaOapg.properties.ins_date, str, schemas.Unset] = schemas.unset,
                            upd_id: typing.Union[MetaOapg.properties.upd_id, str, schemas.Unset] = schemas.unset,
                            upd_date: typing.Union[MetaOapg.properties.upd_date, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                device_id=device_id,
                                place=place,
                                comment=comment,
                                ins_id=ins_id,
                                ins_date=ins_date,
                                upd_id=upd_id,
                                upd_date=upd_date,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'devices':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "device_group_id": device_group_id,
                "device_type": device_type,
                "comment": comment,
                "ins_id": ins_id,
                "ins_date": ins_date,
                "upd_id": upd_id,
                "upd_date": upd_date,
                "devices": devices,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_group_id"]) -> MetaOapg.properties.device_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ins_id"]) -> MetaOapg.properties.ins_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ins_date"]) -> MetaOapg.properties.ins_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upd_id"]) -> MetaOapg.properties.upd_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upd_date"]) -> MetaOapg.properties.upd_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["devices"]) -> MetaOapg.properties.devices: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_group_id", "device_type", "comment", "ins_id", "ins_date", "upd_id", "upd_date", "devices", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_group_id"]) -> typing.Union[MetaOapg.properties.device_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_type"]) -> typing.Union[MetaOapg.properties.device_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ins_id"]) -> typing.Union[MetaOapg.properties.ins_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ins_date"]) -> typing.Union[MetaOapg.properties.ins_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upd_id"]) -> typing.Union[MetaOapg.properties.upd_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upd_date"]) -> typing.Union[MetaOapg.properties.upd_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["devices"]) -> typing.Union[MetaOapg.properties.devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_group_id", "device_type", "comment", "ins_id", "ins_date", "upd_id", "upd_date", "devices", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        device_group_id: typing.Union[MetaOapg.properties.device_group_id, str, schemas.Unset] = schemas.unset,
        device_type: typing.Union[MetaOapg.properties.device_type, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        ins_id: typing.Union[MetaOapg.properties.ins_id, str, schemas.Unset] = schemas.unset,
        ins_date: typing.Union[MetaOapg.properties.ins_date, str, schemas.Unset] = schemas.unset,
        upd_id: typing.Union[MetaOapg.properties.upd_id, str, schemas.Unset] = schemas.unset,
        upd_date: typing.Union[MetaOapg.properties.upd_date, str, schemas.Unset] = schemas.unset,
        devices: typing.Union[MetaOapg.properties.devices, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceGroup':
        return super().__new__(
            cls,
            *args,
            device_group_id=device_group_id,
            device_type=device_type,
            comment=comment,
            ins_id=ins_id,
            ins_date=ins_date,
            upd_id=upd_id,
            upd_date=upd_date,
            devices=devices,
            _configuration=_configuration,
            **kwargs,
        )
