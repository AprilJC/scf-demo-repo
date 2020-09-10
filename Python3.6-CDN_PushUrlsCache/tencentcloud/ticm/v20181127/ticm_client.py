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
from tencentcloud.ticm.v20181127 import models


class TicmClient(AbstractClient):
    _apiVersion = '2018-11-27'
    _endpoint = 'ticm.tencentcloudapi.com'


    def DescribeVideoTask(self, request):
        """提交完視訊審核任務後，可以通過本介面來獲取當前處理的進度和結果

        :param request: Request instance for DescribeVideoTask.
        :type request: :class:`tencentcloud.ticm.v20181127.models.DescribeVideoTaskRequest`
        :rtype: :class:`tencentcloud.ticm.v20181127.models.DescribeVideoTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVideoTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVideoTaskResponse()
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


    def ImageModeration(self, request):
        """本介面提供多種維度的圖像審核能力，支援色情和性感内容識别，政治人物和涉政敏感場景識别，以及暴恐人物、場景、旗幟标識等違禁内容的識别。

        :param request: Request instance for ImageModeration.
        :type request: :class:`tencentcloud.ticm.v20181127.models.ImageModerationRequest`
        :rtype: :class:`tencentcloud.ticm.v20181127.models.ImageModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageModerationResponse()
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


    def VideoModeration(self, request):
        """本介面提供多種維度的視訊審核能力，支援色情和性感内容識别，政治人物和涉政敏感場景識别，以及暴恐人物、場景、旗幟标識等違禁内容的識别。

        :param request: Request instance for VideoModeration.
        :type request: :class:`tencentcloud.ticm.v20181127.models.VideoModerationRequest`
        :rtype: :class:`tencentcloud.ticm.v20181127.models.VideoModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VideoModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VideoModerationResponse()
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