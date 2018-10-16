Dataduct |build-status| |coverage-status|
-----------------------------------------
Dataduct is a wrapper built on top of AWS Datapipeline which makes it easy to
create ETL jobs. All jobs can be specified as a series of steps in a YAML file
and would automatically be translated into datapipeline with appropriate
pipeline objects.

**Documentation and Details**

Documentation and more details can be found at http://dataduct.readthedocs.org/en/latest/

**License**

Copyright [2014] [Coursera]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. |build-status|
   image:: https://travis-ci.org/coursera/dataduct.svg?branch=develop
    :target: https://travis-ci.org/coursera/dataduct

.. |coverage-status|
   image:: https://coveralls.io/repos/coursera/dataduct/badge.svg?branch=develop
    :target: https://coveralls.io/r/coursera/dataduct?branch=develop

**Installing dockerized dataduct**

install docker https://docs.docker.com/install/linux/docker-ce/ubuntu/

install docker-compose: https://docs.docker.com/compose/install/#install-compose

git clone git@github.com:recurly/dataplatform.git

cd dataplatform

clone dataduct inside the datapipeline directory

git clone git@github.com:recurly/dataduct.git

set up docker so it doesn't have to be run as root https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user

copy AWS creds: sudo cp ~task_runner/.aws/config aws_config

sudo chmod uog+r aws_config

docker-compose build --no-cache

docker network create recurly

docker-compose up -d

test that docker is working: docker exec -it dataplatform_pipelines-build_1 python -c "from dataduct.steps.executors.custom_check import validate_redshift_result"

create a login shell for the task_runner user

sudo chsh -s /bin/bash task_runner

restart the task runner process so it picks up its new permissions: sudo service task-runner restart

