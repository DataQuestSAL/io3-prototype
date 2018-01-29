# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Submit a Hadoop job to a cluster."""

from googlecloudsdk.api_lib.dataproc import util
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dataproc.jobs import hadoop
from googlecloudsdk.command_lib.dataproc.jobs import submitter


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Hadoop(hadoop.HadoopBase, submitter.JobSubmitter):
  r"""Submit a Hadoop job to a cluster.

  Submit a Hadoop job to a cluster.

  ## EXAMPLES

  To submit a Hadoop job that runs the main class of a jar, run:

   $ {command} --cluster my_cluster --jar my_jar.jar -- arg1 arg2

  To submit a Hadoop job that runs a specific class of a jar, run:

    $ {command} --cluster my_cluster --class org.my.main.Class \
        --jars my_jar1.jar,my_jar2.jar -- arg1 arg2

  To submit a Hadoop job that runs a jar that is already on the cluster, run:

    $ {command} --cluster my_cluster \
        --jar file:///usr/lib/hadoop-op/hadoop-op-examples.jar \
        -- wordcount gs://my_bucket/my_file.txt gs://my_bucket/output
  """

  @staticmethod
  def Args(parser):
    hadoop.HadoopBase.Args(parser)
    submitter.JobSubmitter.Args(parser)
    driver_group = parser.add_argument_group()
    util.AddJvmDriverFlags(driver_group)

  def ConfigureJob(self, messages, job, args):
    hadoop.HadoopBase.ConfigureJob(messages, job, self.files_by_type,
                                   self.BuildLoggingConfig(
                                       messages, args.driver_log_levels), args)
    submitter.JobSubmitter.ConfigureJob(messages, job, args)


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class HadoopBeta(hadoop.HadoopBase, submitter.JobSubmitterBeta):
  r"""Submit a Hadoop job to a cluster.

  Submit a Hadoop job to a cluster.

  ## EXAMPLES

  To submit a Hadoop job that runs the main class of a jar, run:

    $ {command} --cluster my_cluster --jar my_jar.jar -- arg1 arg2

  To submit a Hadoop job that runs a specific class of a jar, run:

    $ {command} --cluster my_cluster --class org.my.main.Class \
        --jars my_jar1.jar,my_jar2.jar -- arg1 arg2

  To submit a Hadoop job that runs a jar that is already on the cluster, run:

    $ {command} --cluster my_cluster \
        --jar file:///usr/lib/hadoop-op/hadoop-op-examples.jar \
        -- wordcount gs://my_bucket/my_file.txt gs://my_bucket/output
  """

  @staticmethod
  def Args(parser):
    hadoop.HadoopBase.Args(parser)
    submitter.JobSubmitterBeta.Args(parser)
    driver_group = parser.add_mutually_exclusive_group(required=True)
    util.AddJvmDriverFlags(driver_group)

  def ConfigureJob(self, messages, job, args):
    hadoop.HadoopBase.ConfigureJob(messages, job, self.files_by_type,
                                   self.BuildLoggingConfig(
                                       messages, args.driver_log_levels), args)
    submitter.JobSubmitterBeta.ConfigureJob(messages, job, args)
