# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.gs.v20191118 import models


class GsClient(AbstractClient):
    _apiVersion = '2019-11-18'
    _endpoint = 'gs.tencentcloudapi.com'


    def CreateSession(self, request):
        """創建會話

        :param request: Request instance for CreateSession.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateSessionRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateSessionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSession", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSessionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWorkers(self, request):
        """查詢空閑機器數量

        :param request: Request instance for DescribeWorkers.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeWorkersRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeWorkersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWorkers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWorkersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWorkersInfo(self, request):
        """獲取機器訊息

        :param request: Request instance for DescribeWorkersInfo.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeWorkersInfoRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeWorkersInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWorkersInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWorkersInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnterQueue(self, request):
        """進入排隊鎖定機器

        :param request: Request instance for EnterQueue.
        :type request: :class:`tencentcloud.gs.v20191118.models.EnterQueueRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.EnterQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnterQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnterQueueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWorkers(self, request):
        """修改機器訊息

        :param request: Request instance for ModifyWorkers.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyWorkersRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyWorkersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWorkers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWorkersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuitQueue(self, request):
        """登出排隊

        :param request: Request instance for QuitQueue.
        :type request: :class:`tencentcloud.gs.v20191118.models.QuitQueueRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.QuitQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QuitQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuitQueueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopGame(self, request):
        """強制登出遊戲

        :param request: Request instance for StopGame.
        :type request: :class:`tencentcloud.gs.v20191118.models.StopGameRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StopGameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopGame", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopGameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TrylockWorker(self, request):
        """嘗試鎖定機器

        :param request: Request instance for TrylockWorker.
        :type request: :class:`tencentcloud.gs.v20191118.models.TrylockWorkerRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.TrylockWorkerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TrylockWorker", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TrylockWorkerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)