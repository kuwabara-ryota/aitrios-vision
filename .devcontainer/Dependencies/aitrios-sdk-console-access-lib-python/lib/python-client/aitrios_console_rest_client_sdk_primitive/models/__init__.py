# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from aitrios_console_rest_client_sdk_primitive.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from aitrios_console_rest_client_sdk_primitive.model.apply_command_parameter_file_to_device_json_body import ApplyCommandParameterFileToDeviceJsonBody
from aitrios_console_rest_client_sdk_primitive.model.apply_parameter_camera_file_to_device_json_body import ApplyParameterCameraFileToDeviceJsonBody
from aitrios_console_rest_client_sdk_primitive.model.cancel_command_parameter_file_json_body import CancelCommandParameterFileJsonBody
from aitrios_console_rest_client_sdk_primitive.model.cancel_parameter_camera_file_json_body import CancelParameterCameraFileJsonBody
from aitrios_console_rest_client_sdk_primitive.model.change_password_json_body import ChangePasswordJsonBody
from aitrios_console_rest_client_sdk_primitive.model.create_camera_custom_setup_file_json_body import CreateCameraCustomSetupFileJsonBody
from aitrios_console_rest_client_sdk_primitive.model.create_firmware_json_body import CreateFirmwareJsonBody
from aitrios_console_rest_client_sdk_primitive.model.deploy_configuration import DeployConfiguration
from aitrios_console_rest_client_sdk_primitive.model.deploy_device_app_json_body import DeployDeviceAppJsonBody
from aitrios_console_rest_client_sdk_primitive.model.deploy_history import DeployHistory
from aitrios_console_rest_client_sdk_primitive.model.device import Device
from aitrios_console_rest_client_sdk_primitive.model.device_app import DeviceApp
from aitrios_console_rest_client_sdk_primitive.model.device_app_deploy_history import DeviceAppDeployHistory
from aitrios_console_rest_client_sdk_primitive.model.device_group import DeviceGroup
from aitrios_console_rest_client_sdk_primitive.model.enroll_device_json_body import EnrollDeviceJsonBody
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.firmware import Firmware
from aitrios_console_rest_client_sdk_primitive.model.get_device_apps_response import GetDeviceAppsResponse
from aitrios_console_rest_client_sdk_primitive.model.get_device_apps_response_apps import GetDeviceAppsResponseApps
from aitrios_console_rest_client_sdk_primitive.model.get_device_apps_response_versions import GetDeviceAppsResponseVersions
from aitrios_console_rest_client_sdk_primitive.model.http_validation_error import HTTPValidationError
from aitrios_console_rest_client_sdk_primitive.model.import_camera_configuration_file_json_body import ImportCameraConfigurationFileJsonBody
from aitrios_console_rest_client_sdk_primitive.model.import_device_app_json_body import ImportDeviceAppJsonBody
from aitrios_console_rest_client_sdk_primitive.model.inference import Inference
from aitrios_console_rest_client_sdk_primitive.model.inference_result import InferenceResult
from aitrios_console_rest_client_sdk_primitive.model.model import Model
from aitrios_console_rest_client_sdk_primitive.model.model_project import ModelProject
from aitrios_console_rest_client_sdk_primitive.model.model_version import ModelVersion
from aitrios_console_rest_client_sdk_primitive.model.regist_command_parameter_body import RegistCommandParameterBody
from aitrios_console_rest_client_sdk_primitive.model.regist_command_parameter_file_body import RegistCommandParameterFileBody
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from aitrios_console_rest_client_sdk_primitive.model.train_model_create_project_image_regions_data_createprojectimageregionsindto_json_body import TrainModelCreateProjectImageRegionsDataCreateprojectimageregionsindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_import_base_model_data_importbasemodelindto_json_body import TrainModelImportBaseModelDataImportbasemodelindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_import_images_from_blob_folder_data_importimagesfromblobfolderindto_json_body import TrainModelImportImagesFromBlobFolderDataImportimagesfromblobfolderindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_import_images_from_files_data_importimagesfromfilesindto_json_body import TrainModelImportImagesFromFilesDataImportimagesfromfilesindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_import_images_from_scblob_data_importimagesfromscblobindto_json_body import TrainModelImportImagesFromScblobDataImportimagesfromscblobindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_update_base_model_version_data_updatebasemodelversionindto_json_body import TrainModelUpdateBaseModelVersionDataUpdatebasemodelversionindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_update_device_model_version_data_updatedevicemodelversionindto_json_body import TrainModelUpdateDeviceModelVersionDataUpdatedevicemodelversionindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_update_project_image_regions_data_updateprojectimageregionsindto_json_body import TrainModelUpdateProjectImageRegionsDataUpdateprojectimageregionsindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.train_model_update_project_tag_data_updateprojecttagindto_json_body import TrainModelUpdateProjectTagDataUpdateprojecttagindtoJsonBody
from aitrios_console_rest_client_sdk_primitive.model.update_command_parameter_body import UpdateCommandParameterBody
from aitrios_console_rest_client_sdk_primitive.model.update_command_parameter_file_body import UpdateCommandParameterFileBody
from aitrios_console_rest_client_sdk_primitive.model.update_dps_certificate_json_body import UpdateDpsCertificateJsonBody
from aitrios_console_rest_client_sdk_primitive.model.validation_error import ValidationError
