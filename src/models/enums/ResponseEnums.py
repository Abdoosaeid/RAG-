from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATION_SUCCESS = "file validation successful"
    FILE_TYPE_NOT_ALLOWED = "file type is not allowed"
    FILE_SIZE_EXCEEDS_LIMIT = "file size exceeds the maximum allowed size"  
    FILE_UPLOAD_SUCCESS = "file uploaded successfully"
    FILE_UPLOAD_FAILED = "file upload failed"
    FILE_PROCESSING_FAILED = "file processing failed"
    FILE_PROCESSING_SUCCESS = "file processed successfully"
    