# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_non_resource_attributes import V1NonResourceAttributes


class TestV1NonResourceAttributes(unittest.TestCase):
    """ V1NonResourceAttributes unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NonResourceAttributes(self):
        """
        Test V1NonResourceAttributes
        """
        model = kubernetes.client.models.v1_non_resource_attributes.V1NonResourceAttributes()


if __name__ == '__main__':
    unittest.main()
