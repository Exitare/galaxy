import logging
from galaxy.webapps.base.controller import BaseAPIController
from galaxy.web import (
    expose_api,
    expose_api_anonymous,
    require_admin,
    expose_api_anonymous_and_sessionless
)

log = logging.getLogger(__name__)


class JobResourcePredictionsAPIController(BaseAPIController):

    def __init__(self, app):
        super(JobResourcePredictionsAPIController, self).__init__(app)

    @expose_api_anonymous_and_sessionless
    def index(self, trans, **kwargs):
        """
        * GET /api/jobpredications/{}
            Lists cloud-based buckets (e.g., S3 bucket, Azure blob) user has defined.
        :param trans:
        :param kwargs:
        :return: A list of cloud-based buckets user has defined.
        """
        # TODO: This can be implemented leveraging PluggedMedia objects (part of the user-based object store project)
        trans.response.status = 501
        return 'Not Implemented'

    @expose_api_anonymous_and_sessionless
    def get(self, trans, **kwd):
        log.debug("Test log")
        return 'Maybe implemented as get'

    @expose_api_anonymous_and_sessionless
    def post(self, trans, **kwd):
        print("Test")
        return 'Maybe implemented as post'
