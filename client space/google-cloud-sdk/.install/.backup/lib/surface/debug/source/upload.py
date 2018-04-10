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
"""Upload a directory tree."""

import json
import os

from googlecloudsdk.api_lib.debug import upload
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core.util import files
from googlecloudsdk.third_party.appengine.tools import context_util


@base.ReleaseTracks(base.ReleaseTrack.BETA)
@base.Hidden
class Upload(base.CreateCommand):
  """Upload a directory tree.

  This command uploads a directory tree to a branch in the repository
  'google-source-captures' hosted on Cloud Source Repositories.

  The files and branches can be managed with git like any other repository.

  When uploading is done, this command can also produce a source context json
  file describing it.

  See https://cloud.google.com/debugger/docs/source-context for details on where
  to deploy the source context json file in order to enable Stackdriver tools to
  display the uploaded files.
  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'directory',
        help="""\
            The directory tree to upload.
        """)
    parser.add_argument(
        '--branch',
        help="""\
            The branch name. If the branch already exists, the new upload will
            overwrite its history.
        """)
    parser.add_argument(
        '--source-context-directory',
        help="""\
            The directory to write the source context files. Two files
            (source-context.json and source-contexts.json) will be created if
            this is specified.
        """)
    parser.display_info.AddFormat("""
          flattened(
            branch,
            context_file,
            extended_context_file
          )
        """)

  def Run(self, args):
    """Run the upload command."""
    if not os.path.isdir(args.directory):
      raise exceptions.InvalidArgumentException(
          'directory', args.directory + ' is not a directory.')

    mgr = upload.UploadManager()
    result = mgr.Upload(args.branch, args.directory)

    output_dir = args.source_context_directory
    if output_dir:
      files.MakeDir(output_dir)
      output_dir = os.path.realpath(output_dir)
      extended_contexts = result['source_contexts']

      result['extended_context_file'] = os.path.join(output_dir,
                                                     'source-contexts.json')
      with open(result['extended_context_file'], 'w') as f:
        json.dump(extended_contexts, f)

      result['context_file'] = os.path.join(output_dir, 'source-context.json')
      best_context = context_util.BestSourceContext(extended_contexts)
      result['best_context'] = context_util.BestSourceContext(extended_contexts)
      with open(result['context_file'], 'w') as f:
        json.dump(best_context, f)

    log.status.write('Wrote {0} file(s), {1} bytes.\n'.format(
        result['files_written'], result['size_written']))
    files_skipped = result['files_skipped']
    if files_skipped:
      log.status.write('Skipped {0} file(s) due to size limitations.\n'.format(
          files_skipped))
    return [result]