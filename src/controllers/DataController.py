from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import  ResponseSignal
import os
import re

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes

    def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_ALLOWED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDS_LIMIT.value

        return True, ResponseSignal.FILE_VALIDATION_SUCCESS.value

    def generate_unique_filepath(self, filename: str,project_id: str) -> str:

        random_filename =  self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_filename = self.get_clean_filename(filename=filename)

        new_filename = os.path.join(project_path,"_"+random_filename+"_"+cleaned_filename)

        while os.path.exists(new_filename):
            random_filename =  self.generate_random_string()
            new_filename = os.path.join(project_path,"_"+random_filename+"_"+cleaned_filename)
        
        return new_filename, random_filename + "_" + cleaned_filename
    
    def get_clean_filename(self, filename: str) -> str:
        
        cleaned_filename = re.sub(r'[^\w.-]', ' ', filename)
        cleaned_filename = cleaned_filename.replace(' ', '_')

        return cleaned_filename
    
    
