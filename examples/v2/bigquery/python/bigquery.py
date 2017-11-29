# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Creates a cloud BigQuery dataset and table within the dataset"""

def GenerateConfig(context):
  """Generate YAML resource configuration."""
  deployment_name = context.env['deployment'].replace('-','_')
  table = deployment_name + '_table'
  dataset = deployment_name + '_dataset'

  resources = [{
      'name': dataset,
      'type': 'gcp-types/bigquery-v2:datasets',
      'properties': {
          'datasetReference': {
              'datasetId': dataset
          }
      }
  }, {
      'name': table,
      'type': 'gcp-types/bigquery-v2:tables',
      'properties': {
          'datasetId': '$(ref.' + dataset + '.datasetReference.datasetId)',
          'tableReference': {
              'tableId': table
          },
      }
  }]
  return {
      'resources':resources
  }
