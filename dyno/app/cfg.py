# -*- coding: utf-8 -*-

# Licensed to Elasticsearch B.V. under one or more contributor
# license agreements. See the NOTICE file distributed with
# this work for additional information regarding copyright
# ownership. Elasticsearch B.V. licenses this file to you under
# the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations

class Config(object):
    """
    Values for the application configuration
    """
    CORS_ORIGINS=['http://localhost:9000', 'http://localhost:5000']
    API_PREFIX='/api'

class ProductionConfig(Config):
    """For use in production"""


class DevelopmentConfig(Config):
    """For use in development"""
    DEBUG = True


class TestingConfig(Config):
    """For use in testing"""
    DEBUG = True
    TESTING = True
