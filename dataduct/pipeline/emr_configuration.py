"""
Pipeline object class for EmrConfiguration (http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-emrconfiguration.html)
"""
from ..config import Config
from ..s3 import S3LogPath
from ..utils import constants as const
from ..utils.exceptions import ETLInputError
from .pipeline_object import PipelineObject
from .schedule import Schedule
from IPython import embed


class EmrConfiguration(PipelineObject):
    def __init__(
            self,
            id,
            classification=const.NONE,
            properties=[],
            **kwargs):


        super(EmrConfiguration, self).__init__(
            id=id,
            type='EmrConfiguration',
            classification=classification,
            property=properties
        )
