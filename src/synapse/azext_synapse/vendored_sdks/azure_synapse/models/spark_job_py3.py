# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SparkJob(Model):
    """SparkJob.

    :param state:
    :type state: str
    :param name:
    :type name: str
    :param submitter:
    :type submitter: str
    :param compute:
    :type compute: str
    :param spark_application_id:
    :type spark_application_id: str
    :param livy_id:
    :type livy_id: str
    :param timing:
    :type timing: list[str]
    :param spark_job_definition:
    :type spark_job_definition: str
    :param pipeline:
    :type pipeline: list[~azure.synapse.models.SparkJob]
    :param job_type:
    :type job_type: str
    :param submit_time:
    :type submit_time: datetime
    :param end_time:
    :type end_time: datetime
    :param queued_duration:
    :type queued_duration: str
    :param running_duration:
    :type running_duration: str
    :param total_duration:
    :type total_duration: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'submitter': {'key': 'submitter', 'type': 'str'},
        'compute': {'key': 'compute', 'type': 'str'},
        'spark_application_id': {'key': 'sparkApplicationId', 'type': 'str'},
        'livy_id': {'key': 'livyId', 'type': 'str'},
        'timing': {'key': 'timing', 'type': '[str]'},
        'spark_job_definition': {'key': 'sparkJobDefinition', 'type': 'str'},
        'pipeline': {'key': 'pipeline', 'type': '[SparkJob]'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'submit_time': {'key': 'submitTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'queued_duration': {'key': 'queuedDuration', 'type': 'str'},
        'running_duration': {'key': 'runningDuration', 'type': 'str'},
        'total_duration': {'key': 'totalDuration', 'type': 'str'},
    }

    def __init__(self, *, state: str=None, name: str=None, submitter: str=None, compute: str=None, spark_application_id: str=None, livy_id: str=None, timing=None, spark_job_definition: str=None, pipeline=None, job_type: str=None, submit_time=None, end_time=None, queued_duration: str=None, running_duration: str=None, total_duration: str=None, **kwargs) -> None:
        super(SparkJob, self).__init__(**kwargs)
        self.state = state
        self.name = name
        self.submitter = submitter
        self.compute = compute
        self.spark_application_id = spark_application_id
        self.livy_id = livy_id
        self.timing = timing
        self.spark_job_definition = spark_job_definition
        self.pipeline = pipeline
        self.job_type = job_type
        self.submit_time = submit_time
        self.end_time = end_time
        self.queued_duration = queued_duration
        self.running_duration = running_duration
        self.total_duration = total_duration