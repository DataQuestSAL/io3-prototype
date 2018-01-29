"""Generated message classes for cloudscheduler version v1alpha1.

Creates and manages jobs run on a regular recurring schedule.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudscheduler'


class AppEngineHttpTarget(_messages.Message):
  """App Engine target. The job will be pushed to a job handler by means of an
  HTTP request via an AppEngineHttpTarget.http_method such as HTTP POST, HTTP
  GET, etc. The job is acknowledged by means of an HTTP response code in the
  range [200 - 299]. Error 503 is considered an App Engine system error
  instead of an application error. Requests returning error 503 will be
  retried regardless of retry configuration and not counted against retry
  counts. Any other response code, or a failure to receive a response before
  the deadline, constitutes a failed execution.

  Enums:
    HttpMethodValueValuesEnum: The HTTP method to use for the request. The
      default is POST.

  Messages:
    HeadersValue: HTTP request headers.  This map contains the header field
      names and values. Headers can be set when the job is created.  Cloud
      Scheduler sets some headers to default values:  * `User-Agent`: By
      default, this header is   `"AppEngine-Google;
      (+http://code.google.com/appengine)"`.   This header can be modified,
      but Cloud Scheduler will append   `"AppEngine-Google;
      (+http://code.google.com/appengine)"` to the   modified `User-Agent`.
      If the job has an AppEngineHttpTarget.payload, Cloud Scheduler sets the
      following headers:  * `Content-Type`: By default, the `Content-Type`
      header is set to   `"application/octet-stream"`. The default can be
      overridden by explictly   setting `Content-Type` to a particular media
      type when the job is   created.   For example, `Content-Type` can be set
      to `"application/json"`. * `Content-Length`: This is computed by Cloud
      Scheduler. This value is   output only. It cannot be changed.  The
      headers below are output only. They cannot be set or overridden:  *
      `X-Google-*`: For Google internal use only. * `X-AppEngine-*`: For
      Google internal use only. See   [Reading request
      headers](/appengine/docs/python/taskqueue/push/creating-
      handlers#reading_request_headers).  In addition, some App Engine
      headers, which contain job-specific information, are also be sent to the
      job handler; see [request headers](/appengine/docs/python/taskqueue/push
      /creating-handlers#reading_request_headers).

  Fields:
    appEngineRouting: App Engine Routing setting for the job.
    headers: HTTP request headers.  This map contains the header field names
      and values. Headers can be set when the job is created.  Cloud Scheduler
      sets some headers to default values:  * `User-Agent`: By default, this
      header is   `"AppEngine-Google; (+http://code.google.com/appengine)"`.
      This header can be modified, but Cloud Scheduler will append
      `"AppEngine-Google; (+http://code.google.com/appengine)"` to the
      modified `User-Agent`.  If the job has an AppEngineHttpTarget.payload,
      Cloud Scheduler sets the following headers:  * `Content-Type`: By
      default, the `Content-Type` header is set to   `"application/octet-
      stream"`. The default can be overridden by explictly   setting `Content-
      Type` to a particular media type when the job is   created.   For
      example, `Content-Type` can be set to `"application/json"`. * `Content-
      Length`: This is computed by Cloud Scheduler. This value is   output
      only. It cannot be changed.  The headers below are output only. They
      cannot be set or overridden:  * `X-Google-*`: For Google internal use
      only. * `X-AppEngine-*`: For Google internal use only. See   [Reading
      request   headers](/appengine/docs/python/taskqueue/push/creating-
      handlers#reading_request_headers).  In addition, some App Engine
      headers, which contain job-specific information, are also be sent to the
      job handler; see [request headers](/appengine/docs/python/taskqueue/push
      /creating-handlers#reading_request_headers).
    httpMethod: The HTTP method to use for the request. The default is POST.
    payload: Payload.  The payload will be sent as the HTTP message body. A
      message body, and thus a payload, is allowed only if the HTTP method is
      POST or PUT. It is an error to set a data payload on a job with an
      incompatible HttpMethod.
    relativeUrl: The relative URL.  The relative URL must begin with "/" and
      must be a valid HTTP relative URL. It can contain a path, query string
      arguments, and `#` fragments. If the relative URL is empty, then the
      root path "/" will be used. No spaces are allowed, and the maximum
      length allowed is 2083 characters.
    retryConfig: Settings that determine the retry behavior.
  """

  class HttpMethodValueValuesEnum(_messages.Enum):
    """The HTTP method to use for the request. The default is POST.

    Values:
      HTTP_METHOD_UNSPECIFIED: HTTP method unspecified
      POST: HTTP Post
      GET: HTTP Get
      HEAD: HTTP Head
      PUT: HTTP Put
      DELETE: HTTP Delete
    """
    HTTP_METHOD_UNSPECIFIED = 0
    POST = 1
    GET = 2
    HEAD = 3
    PUT = 4
    DELETE = 5

  @encoding.MapUnrecognizedFields('additionalProperties')
  class HeadersValue(_messages.Message):
    """HTTP request headers.  This map contains the header field names and
    values. Headers can be set when the job is created.  Cloud Scheduler sets
    some headers to default values:  * `User-Agent`: By default, this header
    is   `"AppEngine-Google; (+http://code.google.com/appengine)"`.   This
    header can be modified, but Cloud Scheduler will append   `"AppEngine-
    Google; (+http://code.google.com/appengine)"` to the   modified `User-
    Agent`.  If the job has an AppEngineHttpTarget.payload, Cloud Scheduler
    sets the following headers:  * `Content-Type`: By default, the `Content-
    Type` header is set to   `"application/octet-stream"`. The default can be
    overridden by explictly   setting `Content-Type` to a particular media
    type when the job is   created.   For example, `Content-Type` can be set
    to `"application/json"`. * `Content-Length`: This is computed by Cloud
    Scheduler. This value is   output only. It cannot be changed.  The headers
    below are output only. They cannot be set or overridden:  * `X-Google-*`:
    For Google internal use only. * `X-AppEngine-*`: For Google internal use
    only. See   [Reading request
    headers](/appengine/docs/python/taskqueue/push/creating-
    handlers#reading_request_headers).  In addition, some App Engine headers,
    which contain job-specific information, are also be sent to the job
    handler; see [request headers](/appengine/docs/python/taskqueue/push
    /creating-handlers#reading_request_headers).

    Messages:
      AdditionalProperty: An additional property for a HeadersValue object.

    Fields:
      additionalProperties: Additional properties of type HeadersValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a HeadersValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  appEngineRouting = _messages.MessageField('AppEngineRouting', 1)
  headers = _messages.MessageField('HeadersValue', 2)
  httpMethod = _messages.EnumField('HttpMethodValueValuesEnum', 3)
  payload = _messages.BytesField(4)
  relativeUrl = _messages.StringField(5)
  retryConfig = _messages.MessageField('RetryConfig', 6)


class AppEngineRouting(_messages.Message):
  """App Engine Routing.  For more information about services, versions, and
  instances see [An Overview of App Engine](/appengine/docs/python/an-
  overview-of-app-engine), [Microservices Architecture on Google App
  Engine](/appengine/docs/python/microservices-on-app-engine), [App Engine
  Standard request routing](/appengine/docs/standard/python/how-requests-are-
  routed), and [App Engine Flex request
  routing](/appengine/docs/flexible/python/how-requests-are-routed).

  Fields:
    host: Output only.  The host that the job is sent to. For more information
      about how App Engine requests are routed, see
      [here](/appengine/docs/standard/python/how-requests-are-routed).  The
      host is constructed as:   * `host = [application_domain_name]`</br>   `|
      [service] + '.' + [application_domain_name]`</br>   `| [version] + '.' +
      [application_domain_name]`</br>   `| [version_dot_service]+ '.' +
      [application_domain_name]`</br>   `| [instance] + '.' +
      [application_domain_name]`</br>   `| [instance_dot_service] + '.' +
      [application_domain_name]`</br>   `| [instance_dot_version] + '.' +
      [application_domain_name]`</br>   `| [instance_dot_version_dot_service]
      + '.' + [application_domain_name]`  * `application_domain_name` = The
      domain name of the app, for   example <app-id>.appspot.com, which is
      associated with the   job's project ID.  * `service =`
      AppEngineRouting.service  * `version =` AppEngineRouting.version  *
      `version_dot_service =`   AppEngineRouting.version `+ '.' +`
      AppEngineRouting.service  * `instance =` AppEngineRouting.instance  *
      `instance_dot_service =`   AppEngineRouting.instance `+ '.' +`
      AppEngineRouting.service  * `instance_dot_version =`
      AppEngineRouting.instance `+ '.' +` AppEngineRouting.version  *
      `instance_dot_version_dot_service =`   AppEngineRouting.instance `+ '.'
      +`   AppEngineRouting.version `+ '.' +` AppEngineRouting.service  If
      AppEngineRouting.service is empty, then the job will be sent to the
      service which is the default service when the job is attempted.  If
      AppEngineRouting.version is empty, then the job will be sent to the
      version which is the default version when the job is attempted.  If
      AppEngineRouting.instance is empty, then the job will be sent to an
      instance which is available when the job is attempted.  When
      AppEngineRouting.service is "default", AppEngineRouting.version is
      "default", and AppEngineRouting.instance is empty, AppEngineRouting.host
      is shortened to just the `application_domain_name`.  If
      AppEngineRouting.service, AppEngineRouting.version, or
      AppEngineRouting.instance is invalid, then the job will be sent to the
      default version of the default service when the job is attempted.
    instance: App instance.  By default, the job is sent to an instance which
      is available when the job is attempted.  Requests can only be sent to a
      specific instance if [manual scaling is used in App Engine
      Standard](/appengine/docs/python/an-overview-of-app-
      engine?hl=en_US#scaling_types_and_instance_classes). App Engine Flex
      does not support instances. For more information, see [App Engine
      Standard request routing](/appengine/docs/standard/python/how-requests-
      are-routed) and [App Engine Flex request
      routing](/appengine/docs/flexible/python/how-requests-are-routed).
    service: App service.  By default, the job is sent to the service which is
      the default service when the job is attempted ("default").
    version: App version.  By default, the job is sent to the version which is
      the default version when the job is attempted ("default").
  """

  host = _messages.StringField(1)
  instance = _messages.StringField(2)
  service = _messages.StringField(3)
  version = _messages.StringField(4)


class CloudschedulerProjectsLocationsGetRequest(_messages.Message):
  """A CloudschedulerProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class CloudschedulerProjectsLocationsJobsCreateRequest(_messages.Message):
  """A CloudschedulerProjectsLocationsJobsCreateRequest object.

  Fields:
    job: A Job resource to be passed as the request body.
    parent: Required.  The location name. For example:
      `projects/PROJECT_ID/locations/LOCATION_ID`.
  """

  job = _messages.MessageField('Job', 1)
  parent = _messages.StringField(2, required=True)


class CloudschedulerProjectsLocationsJobsDeleteRequest(_messages.Message):
  """A CloudschedulerProjectsLocationsJobsDeleteRequest object.

  Fields:
    name: Required.  The job name. For example:
      `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`.
  """

  name = _messages.StringField(1, required=True)


class CloudschedulerProjectsLocationsJobsGetRequest(_messages.Message):
  """A CloudschedulerProjectsLocationsJobsGetRequest object.

  Enums:
    ResponseViewValueValuesEnum: The response_view specifies which subset of
      the Job will be returned.  By default ListJobsRequest.response_view is
      Job.View.BASIC; not all information is retrieved by default because some
      data, such as payloads, might be desirable to return only when needed
      because of its large size or because of the sensitivity of data that it
      contains.  Authorization for Job.View.FULL requires
      `cloudscheduler.jobs.fullView` [Google
      IAM](https://cloud.google.com/iam/) permission on the Job.name resource.

  Fields:
    name: The job name. For example:
      `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`.
    responseView: The response_view specifies which subset of the Job will be
      returned.  By default ListJobsRequest.response_view is Job.View.BASIC;
      not all information is retrieved by default because some data, such as
      payloads, might be desirable to return only when needed because of its
      large size or because of the sensitivity of data that it contains.
      Authorization for Job.View.FULL requires `cloudscheduler.jobs.fullView`
      [Google IAM](https://cloud.google.com/iam/) permission on the Job.name
      resource.
  """

  class ResponseViewValueValuesEnum(_messages.Enum):
    """The response_view specifies which subset of the Job will be returned.
    By default ListJobsRequest.response_view is Job.View.BASIC; not all
    information is retrieved by default because some data, such as payloads,
    might be desirable to return only when needed because of its large size or
    because of the sensitivity of data that it contains.  Authorization for
    Job.View.FULL requires `cloudscheduler.jobs.fullView` [Google
    IAM](https://cloud.google.com/iam/) permission on the Job.name resource.

    Values:
      VIEW_UNSPECIFIED: <no description>
      BASIC: <no description>
      FULL: <no description>
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  name = _messages.StringField(1, required=True)
  responseView = _messages.EnumField('ResponseViewValueValuesEnum', 2)


class CloudschedulerProjectsLocationsJobsListRequest(_messages.Message):
  """A CloudschedulerProjectsLocationsJobsListRequest object.

  Enums:
    ResponseViewValueValuesEnum: The response_view specifies which subset of
      the Job will be returned.  By default response_view is Job.View.BASIC;
      not all information is retrieved by default because some data, such as
      payloads, might be desirable to return only when needed because of its
      large size or because of the sensitivity of data that it contains.
      Authorization for Job.View.FULL requires `cloudscheduler.jobs.fullView`
      [Google IAM](https://cloud.google.com/iam/) permission on the Job.name
      resource.

  Fields:
    pageSize: Requested page size. Fewer jobs than requested might be
      returned.  The maximum page size is 500. If unspecified, the page size
      will be the maximum. Fewer jobs than requested might be returned, even
      if more jobs exist; use next_page_token to determine if more jobs exist.
    pageToken: A token identifying a page of results the server will return.
      To request the first page results, page_token must be empty. To request
      the next page of results, page_token must be the value of
      ListJobsResponse.next_page_token returned from the previous call to
      CloudScheduler.ListJobs. It is an error to switch the value of
      ListJobsRequest.filter or ListJobsRequest.order_by while iterating
      through pages.  For JSON requests, the value of this field must be
      base64-encoded.
    parent: Required.  The location name. For example:
      `projects/PROJECT_ID/locations/LOCATION_ID`.
    responseView: The response_view specifies which subset of the Job will be
      returned.  By default response_view is Job.View.BASIC; not all
      information is retrieved by default because some data, such as payloads,
      might be desirable to return only when needed because of its large size
      or because of the sensitivity of data that it contains.  Authorization
      for Job.View.FULL requires `cloudscheduler.jobs.fullView` [Google
      IAM](https://cloud.google.com/iam/) permission on the Job.name resource.
  """

  class ResponseViewValueValuesEnum(_messages.Enum):
    """The response_view specifies which subset of the Job will be returned.
    By default response_view is Job.View.BASIC; not all information is
    retrieved by default because some data, such as payloads, might be
    desirable to return only when needed because of its large size or because
    of the sensitivity of data that it contains.  Authorization for
    Job.View.FULL requires `cloudscheduler.jobs.fullView` [Google
    IAM](https://cloud.google.com/iam/) permission on the Job.name resource.

    Values:
      VIEW_UNSPECIFIED: <no description>
      BASIC: <no description>
      FULL: <no description>
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.BytesField(2)
  parent = _messages.StringField(3, required=True)
  responseView = _messages.EnumField('ResponseViewValueValuesEnum', 4)


class CloudschedulerProjectsLocationsJobsRunRequest(_messages.Message):
  """A CloudschedulerProjectsLocationsJobsRunRequest object.

  Fields:
    name: Required.  The job name. For example:
      `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`.
    runJobRequest: A RunJobRequest resource to be passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  runJobRequest = _messages.MessageField('RunJobRequest', 2)


class CloudschedulerProjectsLocationsListRequest(_messages.Message):
  """A CloudschedulerProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Job(_messages.Message):
  """Configuration for a job.

  Enums:
    JobStateValueValuesEnum: Output only. State of the job. For example:
      running, paused, or disabled.

  Fields:
    appEngineHttpTarget: App Engine Http target.
    description: A human-readable description for the job.
    jobState: Output only. State of the job. For example: running, paused, or
      disabled.
    name: The job name. For example:
      `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`.  Caller-
      specified in CreateJobRequest, after which it becomes output only.
    nextScheduleTime: Output only. The next time the job is scheduled. Note
      that this may be a retry of a previously failed execution or the next
      execution time according to the schedule.
    pubsubTarget: Pub/Sub target.
    schedule: Specifies a schedule of start times. This can be used to specify
      more complicated, and time-zone-aware schedules than is possible using
      only Job.period.  A scheduled start time will be skipped if the previous
      execution has not ended when its scheduled time occurs.  If
      RetryConfig.retry_count > 0 and a job attempt fails, the job will be a
      total of tried RetryConfig.retry_count times, with exponential backoff,
      until the next scheduled start time.
    status: Output only. The response from the target of the last attempted
      execution.
    userUpdateTime: Output only. The time of the last user update to the job,
      or the creation time if there have been no updates.
  """

  class JobStateValueValuesEnum(_messages.Enum):
    """Output only. State of the job. For example: running, paused, or
    disabled.

    Values:
      JOB_STATE_UNSPECIFIED: Unspecified state.
      ENABLED: The job is executing normally.
      PAUSED: The job is paused by the user. It will not execute. A user can
        intentionally pause the job using CloudScheduler.PauseJobRequest.
      DISABLED: The job is disabled by the system due to error. The user
        cannot directly set a job to be disabled. The error can be viewed in
        Job.status.
    """
    JOB_STATE_UNSPECIFIED = 0
    ENABLED = 1
    PAUSED = 2
    DISABLED = 3

  appEngineHttpTarget = _messages.MessageField('AppEngineHttpTarget', 1)
  description = _messages.StringField(2)
  jobState = _messages.EnumField('JobStateValueValuesEnum', 3)
  name = _messages.StringField(4)
  nextScheduleTime = _messages.StringField(5)
  pubsubTarget = _messages.MessageField('PubsubTarget', 6)
  schedule = _messages.MessageField('Schedule', 7)
  status = _messages.MessageField('Status', 8)
  userUpdateTime = _messages.StringField(9)


class ListJobsResponse(_messages.Message):
  """Response message for listing jobs using CloudScheduler.ListJobs.

  Fields:
    jobs: The list of jobs.
    nextPageToken: A token to retrieve next page of results. Pass this value
      in the ListJobsRequest.page_token field in the subsequent call to
      JobQueues.ListJobs to retrieve the next page of results. If this is
      empty it indicates that there are no more results through which to
      paginate.  For JSON requests, the value of this field must be
      base64-encoded.  The page token is valid for only 2 hours.
  """

  jobs = _messages.MessageField('Job', 1, repeated=True)
  nextPageToken = _messages.BytesField(2)


class ListLocationsResponse(_messages.Message):
  """The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class Location(_messages.Message):
  """A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  labels = _messages.MessageField('LabelsValue', 1)
  locationId = _messages.StringField(2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)


class PubsubMessage(_messages.Message):
  """A message data and its attributes. The message payload must not be empty;
  it must contain either a non-empty data field, or at least one attribute.

  Messages:
    AttributesValue: Optional attributes for this message.

  Fields:
    attributes: Optional attributes for this message.
    data: The message payload.
    messageId: ID of this message, assigned by the server when the message is
      published. Guaranteed to be unique within the topic. This value may be
      read by a subscriber that receives a `PubsubMessage` via a `Pull` call
      or a push delivery. It must not be populated by the publisher in a
      `Publish` call.
    publishTime: The time at which the message was published, populated by the
      server when it receives the `Publish` call. It must not be populated by
      the publisher in a `Publish` call.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class AttributesValue(_messages.Message):
    """Optional attributes for this message.

    Messages:
      AdditionalProperty: An additional property for a AttributesValue object.

    Fields:
      additionalProperties: Additional properties of type AttributesValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a AttributesValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  attributes = _messages.MessageField('AttributesValue', 1)
  data = _messages.BytesField(2)
  messageId = _messages.StringField(3)
  publishTime = _messages.StringField(4)


class PubsubTarget(_messages.Message):
  """Pub/Sub target. Jobs will be delivered by publishing a message to the
  given Pub/Sub topic.

  Messages:
    PubsubMessageValue: Required.  This pubsub message is sent when the job is
      attempted.  `pubsub_message` should be a google.pubsub.v1.PubsubMessage.

  Fields:
    pubsubMessage: Required.  This pubsub message is sent when the job is
      attempted.  `pubsub_message` should be a google.pubsub.v1.PubsubMessage.
    topicName: Required.  The name of the Cloud Pub/Sub topic to which
      messages will be published when a job is delivered. The topic name must
      be in the same format as required by PubSub's [PublishRequest.name](http
      s://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#publishr
      equest), for example `projects/PROJECT_ID/topics/TOPIC_ID`.  The topic
      must be in the same project as the Cloud Scheduler job.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PubsubMessageValue(_messages.Message):
    """Required.  This pubsub message is sent when the job is attempted.
    `pubsub_message` should be a google.pubsub.v1.PubsubMessage.

    Messages:
      AdditionalProperty: An additional property for a PubsubMessageValue
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a PubsubMessageValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  pubsubMessage = _messages.MessageField('PubsubMessageValue', 1)
  topicName = _messages.StringField(2)


class RetryConfig(_messages.Message):
  """Settings that determine the retry behavior.  By default, if a job does
  not complete successfully (meaning that an acknowledgement is not received
  from the handler before the
  [deadline](/appengine/docs/python/taskqueue/push/#the_task_deadline), then
  it will be retried with exponential backoff according to the settings in
  RetryConfig.

  Fields:
    jobAgeLimit: The time limit for retrying a failed job, measured from when
      the job was first run. If specified with RetryConfig.retry_count, the
      job will be retried until both limits are reached.  The default value
      for job_age_limit is zero, which means job age is unlimited.
    maxBackoffSeconds: The maximum amount of time to wait before retrying a
      task after it fails.  The default value of this field is 1 hour.
    maxDoublings: The maximum number of times that the interval between failed
      job retries will be doubled before the increase becomes constant. The
      constant is: 2**(max_doublings - 1) * RetryConfig.min_backoff_seconds.
      The default value of this field is 16.
    minBackoffSeconds: The minimum amount of time to wait before retrying a
      task after it fails.  The default value of this field is 0.1 seconds.
    retryCount: It determines the total number  attempts that the system will
      make to deliver a job using the exponential backoff procedure described
      above.  The default value of retry_count is zero.  If retry_count is
      zero, a job attempt will *not* be retried if it fails. Instead the Cloud
      Scheduler system will wait for the next scheduled execution time.  If
      retry_count is set to a non-zero number then Cloud Scheduler will retry
      failed attempts, using exponential backoff, retry_count times, or until
      the next scheduled execution time, whichever comes first.  Value greater
      than 5 and negative values are not allowed.
  """

  jobAgeLimit = _messages.StringField(1)
  maxBackoffSeconds = _messages.StringField(2)
  maxDoublings = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  minBackoffSeconds = _messages.StringField(4)
  retryCount = _messages.IntegerField(5, variant=_messages.Variant.INT32)


class RunJobRequest(_messages.Message):
  """Request message for forcing a job to run now using CloudScheduler.RunJob.
  """



class Schedule(_messages.Message):
  """Scheduler schedule in an English-like format.

  Fields:
    schedule: Required.  Scheduler schedules are specified using an English-
      like format. See https://cloud.google.com/appengine/docs/standard/python
      /config/cronref#schedule_format
    timezone: Specifies the time zone to be used in interpreting
      ScheduleSpec.schedule. The value of this field must be a time zone name
      from the tz database: http://en.wikipedia.org/wiki/Tz_database.  Note
      that some timezones include a includes a provision for daylight savings
      time. The rules for daylight saving time are determined by the chosen
      tz. For UTC use the string "utc". If a timezone is not specified, the
      default will be in UTC (also known as GMT).
  """

  schedule = _messages.StringField(1)
  timezone = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Status(_messages.Message):
  """The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
