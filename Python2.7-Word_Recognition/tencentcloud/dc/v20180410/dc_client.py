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
from tencentcloud.dc.v20180410 import models


class DcClient(AbstractClient):
    _apiVersion = '2018-04-10'
    _endpoint = 'dc.tencentcloudapi.com'


    def AcceptDirectConnectTunnel(self, request):
        """接受專用通道申請

        :param request: 調用AcceptDirectConnectTunnel所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.AcceptDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.AcceptDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AcceptDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcceptDirectConnectTunnelResponse()
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


    def CreateDirectConnect(self, request):
        """申請物理專線接入。
        調用該介面時，請注意：
        賬号要進行實名認證，否則不允許申請物理專線；
        若帳戶下存在欠費狀态的物理專線，則不能申請更多的物理專線。

        :param request: 調用CreateDirectConnect所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectResponse()
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


    def CreateDirectConnectTunnel(self, request):
        """用于創建專用通道的介面

        :param request: 調用CreateDirectConnectTunnel所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectTunnelResponse()
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


    def DeleteDirectConnect(self, request):
        """删除物理專線。
        只能删除處于狀态的物理專線。

        :param request: 調用DeleteDirectConnect所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectResponse()
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


    def DeleteDirectConnectTunnel(self, request):
        """删除專用通道

        :param request: 調用DeleteDirectConnectTunnel所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectTunnelResponse()
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


    def DescribeAccessPoints(self, request):
        """查詢物理專線接入點

        :param request: 調用DescribeAccessPoints所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeAccessPointsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeAccessPointsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessPoints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessPointsResponse()
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


    def DescribeDirectConnectTunnels(self, request):
        """用于查詢專用通道清單。

        :param request: 調用DescribeDirectConnectTunnels所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectTunnels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectTunnelsResponse()
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


    def DescribeDirectConnects(self, request):
        """查詢物理專線清單。

        :param request: 調用DescribeDirectConnects所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectsResponse()
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


    def ModifyDirectConnectAttribute(self, request):
        """修改物理專線的屬性。

        :param request: 調用ModifyDirectConnectAttribute所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectAttributeRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDirectConnectAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDirectConnectAttributeResponse()
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


    def ModifyDirectConnectTunnelAttribute(self, request):
        """修改專用通道屬性

        :param request: 調用ModifyDirectConnectTunnelAttribute所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelAttributeRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDirectConnectTunnelAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDirectConnectTunnelAttributeResponse()
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


    def RejectDirectConnectTunnel(self, request):
        """拒絕專用通道申請

        :param request: 調用RejectDirectConnectTunnel所需參數的結構體。
        :type request: :class:`tencentcloud.dc.v20180410.models.RejectDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.RejectDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RejectDirectConnectTunnel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RejectDirectConnectTunnelResponse()
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