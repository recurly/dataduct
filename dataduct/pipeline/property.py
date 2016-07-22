"""
Pipeline object class for Property (http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-property.html)
"""
from ..config import Config
from ..s3 import S3LogPath
from ..utils import constants as const
from ..utils.exceptions import ETLInputError
from .pipeline_object import PipelineObject
from .schedule import Schedule


class Property(PipelineObject):
    def __init__(
            self,
            id,
            key=const.NONE,
            value=const.NONE,
            **kwargs):

        super(Property, self).__init__(
            id=id,
            key=key,
            type='Property',
            value=value
        )
