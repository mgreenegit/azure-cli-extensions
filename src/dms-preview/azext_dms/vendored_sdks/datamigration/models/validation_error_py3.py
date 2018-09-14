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


class ValidationError(Model):
    """Description about the errors happen while performing migration validation.

    :param text: Error Text
    :type text: str
    :param severity: Severity of the error. Possible values include:
     'Message', 'Warning', 'Error'
    :type severity: str or ~azure.mgmt.datamigration.models.Severity
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'str'},
    }

    def __init__(self, *, text: str=None, severity=None, **kwargs) -> None:
        super(ValidationError, self).__init__(**kwargs)
        self.text = text
        self.severity = severity
