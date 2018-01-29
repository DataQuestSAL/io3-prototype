# Copyright 2014 Google Inc. All Rights Reserved.
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
"""Command for describing instances."""
from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute.instances import flags


@base.ReleaseTracks(base.ReleaseTrack.GA, base.ReleaseTrack.BETA)
class Describe(base.DescribeCommand):
  """Describe a virtual machine instance.

  *{command}* displays all data associated with a Google Compute
  Engine virtual machine instance.
  """

  @staticmethod
  def Args(parser):
    flags.INSTANCE_ARG.AddArgument(parser, operation_type='describe')

  def _GetInstanceRef(self, holder, args):
    return flags.INSTANCE_ARG.ResolveAsResource(
        args,
        holder.resources,
        scope_lister=flags.GetInstanceZoneScopeLister(holder.client))

  def _GetInstance(self, holder, instance_ref):
    request = holder.client.messages.ComputeInstancesGetRequest(
        **instance_ref.AsDict())
    return holder.client.MakeRequests([
        (holder.client.apitools_client.instances, 'Get', request)])[0]

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    instance_ref = self._GetInstanceRef(holder, args)
    return self._GetInstance(holder, instance_ref)


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class DescribeAlpha(Describe):
  """Describe a virtual machine instance.

  *{command}* displays all data associated with a Google Compute
  Engine virtual machine instance.
  """

  @staticmethod
  def Args(parser):
    flags.INSTANCE_ARG.AddArgument(parser, operation_type='describe')
    parser.add_argument(
        '--guest-attributes',
        metavar='GUEST_ATTRIBUTE_KEY',
        type=arg_parsers.ArgList(),
        default=[],
        help=('Instead of instance resource display guest attributes of the '
              'instance stored with the given keys.'))

  def _GetGuestAttributes(self, holder, instance_ref, variable_keys):
    def _GetGuestAttributeRequest(holder, instance_ref, variable_key):
      req = holder.client.messages.ComputeInstancesGetGuestAttributesRequest(
          instance=instance_ref.Name(),
          project=instance_ref.project,
          variableKey=variable_key,
          zone=instance_ref.zone)
      return (
          holder.client.apitools_client.instances, 'GetGuestAttributes', req)

    requests = [
        _GetGuestAttributeRequest(holder, instance_ref, variable_key)
        for variable_key in variable_keys]
    return holder.client.MakeRequests(requests)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    instance_ref = self._GetInstanceRef(holder, args)
    if args.guest_attributes:
      return self._GetGuestAttributes(
          holder, instance_ref, args.guest_attributes)
    return self._GetInstance(holder, instance_ref)

