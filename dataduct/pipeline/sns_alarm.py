"""
Pipeline object class for sns
"""

from ..config import Config
from ..utils import constants as const
from .pipeline_object import PipelineObject

config = Config()
SNS_TOPIC_ARN_FAILURE = config.etl.get('SNS_TOPIC_ARN_FAILURE', const.NONE)
ROLE = config.etl['ROLE']


class SNSAlarm(PipelineObject):
    """SNS object added to all pipelines
    """

    def __init__(self,
                 id,
                 pipeline_name=None,
                 my_message=None,
                 topic_arn=None,
                 failure=True,
                 **kwargs):
        """Constructor for the SNSAlarm class

        Args:
            id(str): id of the object
            pipeline_name(str): frequency type for the pipeline
            my_message(str): Message used in SNS,
            **kwargs(optional): Keyword arguments directly passed to base class
        """

        if not pipeline_name:
            pipeline_name = "None"

        if failure:
            if not my_message:
                my_message = '\n'.join([
                    'Identifier: ' + pipeline_name,
                    'Object: #{node.name}',
                    'Object Scheduled Start Time: #{node.@scheduledStartTime}',
                    'Error Message: #{node.errorMessage}',
                    'Error Stack Trace: #{node.errorStackTrace}'
                ])
            subject = 'Data Pipeline %s failed' % pipeline_name
        else:
            if not my_message:
                my_message = '\n'.join([
                     'Identifier: ' + pipeline_name,
                     'Object: #{node.name}',
                     'Object Scheduled Start Time: #{node.@scheduledStartTime}',
                     'Object Actual Start Time: #{node.@actualStartTime}',
                     'Object End Time: #{node.@actualEndTime}'
               ])
            subject = 'Data Pipeline %s succeeded ' % pipeline_name


        if topic_arn is None:
            topic_arn = SNS_TOPIC_ARN_FAILURE

        super(SNSAlarm, self).__init__(
            id=id,
            type='SnsAlarm',
            topicArn=topic_arn,
            role=ROLE,
            subject=subject,
            message=my_message,
        )
