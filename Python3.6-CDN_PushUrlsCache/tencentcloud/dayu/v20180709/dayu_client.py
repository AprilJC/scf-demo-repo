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
from tencentcloud.dayu.v20180709 import models


class DayuClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'dayu.tencentcloudapi.com'


    def CreateBasicDDoSAlarmThreshold(self, request):
        """設置基礎防護的DDoS告警阈值，只支援基礎防護産品

        :param request: Request instance for CreateBasicDDoSAlarmThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateBasicDDoSAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateBasicDDoSAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBasicDDoSAlarmThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBasicDDoSAlarmThresholdResponse()
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


    def CreateBoundIP(self, request):
        """綁定IP到高防包實例，支援獨享包、共享包；需要注意的是此介面綁定或解綁IP是異步介面，當處于綁定或解綁中時，則不允許再進行綁定或解綁，需要等待當前綁定或解除綁定完成。

        :param request: Request instance for CreateBoundIP.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateBoundIPRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateBoundIPResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBoundIP", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBoundIPResponse()
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


    def CreateCCFrequencyRules(self, request):
        """添加CC防護的訪問頻率控制規則

        :param request: Request instance for CreateCCFrequencyRules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateCCFrequencyRulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateCCFrequencyRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCCFrequencyRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCCFrequencyRulesResponse()
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


    def CreateCCSelfDefinePolicy(self, request):
        """創建CC自定義策略

        :param request: Request instance for CreateCCSelfDefinePolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateCCSelfDefinePolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateCCSelfDefinePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCCSelfDefinePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCCSelfDefinePolicyResponse()
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


    def CreateDDoSPolicy(self, request):
        """添加DDoS高級策略

        :param request: Request instance for CreateDDoSPolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSPolicyResponse()
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


    def CreateDDoSPolicyCase(self, request):
        """添加策略場景

        :param request: Request instance for CreateDDoSPolicyCase.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDDoSPolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSPolicyCaseResponse()
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


    def CreateInstanceName(self, request):
        """資源實例重命名，支援獨享包、共享包、高防IP、高防IP專業版；

        :param request: Request instance for CreateInstanceName.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateInstanceNameRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceNameResponse()
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


    def CreateL4HealthConfig(self, request):
        """上傳四層健康檢查配置

        :param request: Request instance for CreateL4HealthConfig.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL4HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL4HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL4HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL4HealthConfigResponse()
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


    def CreateL4Rules(self, request):
        """添加L4轉發規則

        :param request: Request instance for CreateL4Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL4RulesResponse()
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


    def CreateL7CCRule(self, request):
        """此介面是7層CC的訪問頻控自定義規則（IP+Host維度，不支援具體的URI），此介面已棄用，請調用新介面CreateCCFrequencyRules，新介面同時支援IP+Host維度以及具體的URI；

        :param request: Request instance for CreateL7CCRule.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7CCRuleRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7CCRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7CCRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7CCRuleResponse()
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


    def CreateL7HealthConfig(self, request):
        """上傳七層健康檢查配置

        :param request: Request instance for CreateL7HealthConfig.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7HealthConfigResponse()
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


    def CreateL7RuleCert(self, request):
        """配置7層轉發規則的證書

        :param request: Request instance for CreateL7RuleCert.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7RuleCertRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7RuleCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7RuleCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RuleCertResponse()
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


    def CreateL7Rules(self, request):
        """添加7層(網站)轉發規則

        :param request: Request instance for CreateL7Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RulesResponse()
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


    def CreateL7RulesUpload(self, request):
        """批次上傳7層轉發規則

        :param request: Request instance for CreateL7RulesUpload.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesUploadRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesUploadResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7RulesUpload", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RulesUploadResponse()
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


    def CreateNetReturn(self, request):
        """高防IP專業版一鍵切回源站

        :param request: Request instance for CreateNetReturn.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateNetReturnRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateNetReturnResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetReturn", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetReturnResponse()
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


    def CreateNewL4Rules(self, request):
        """添加L4轉發規則

        :param request: Request instance for CreateNewL4Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateNewL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateNewL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNewL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNewL4RulesResponse()
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


    def CreateNewL7Rules(self, request):
        """添加7層轉發規則

        :param request: Request instance for CreateNewL7Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateNewL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateNewL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNewL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNewL7RulesResponse()
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


    def CreateUnblockIp(self, request):
        """IP解封操作

        :param request: Request instance for CreateUnblockIp.
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateUnblockIpRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateUnblockIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUnblockIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUnblockIpResponse()
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


    def DeleteCCFrequencyRules(self, request):
        """删除CC防護的訪問頻率控制規則

        :param request: Request instance for DeleteCCFrequencyRules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteCCFrequencyRulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteCCFrequencyRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCCFrequencyRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCCFrequencyRulesResponse()
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


    def DeleteCCSelfDefinePolicy(self, request):
        """删除CC自定義策略

        :param request: Request instance for DeleteCCSelfDefinePolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteCCSelfDefinePolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteCCSelfDefinePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCCSelfDefinePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCCSelfDefinePolicyResponse()
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


    def DeleteDDoSPolicy(self, request):
        """删除DDoS高級策略

        :param request: Request instance for DeleteDDoSPolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSPolicyResponse()
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


    def DeleteDDoSPolicyCase(self, request):
        """删除策略場景

        :param request: Request instance for DeleteDDoSPolicyCase.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDDoSPolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSPolicyCaseResponse()
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


    def DeleteL4Rules(self, request):
        """删除四層轉發規則

        :param request: Request instance for DeleteL4Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL4RulesResponse()
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


    def DeleteL7Rules(self, request):
        """删除七層轉發規則

        :param request: Request instance for DeleteL7Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL7RulesResponse()
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


    def DeleteNewL4Rules(self, request):
        """删除L4轉發規則

        :param request: Request instance for DeleteNewL4Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteNewL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteNewL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNewL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNewL4RulesResponse()
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


    def DeleteNewL7Rules(self, request):
        """删除L7轉發規則

        :param request: Request instance for DeleteNewL7Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteNewL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteNewL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNewL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNewL7RulesResponse()
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


    def DescribeActionLog(self, request):
        """獲取操作日志

        :param request: Request instance for DescribeActionLog.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeActionLogRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeActionLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeActionLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeActionLogResponse()
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


    def DescribeBGPIPL7RuleMaxCnt(self, request):
        """獲取高防IP可添加的最多7層規則數量

        :param request: Request instance for DescribeBGPIPL7RuleMaxCnt.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeBGPIPL7RuleMaxCntRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeBGPIPL7RuleMaxCntResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBGPIPL7RuleMaxCnt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBGPIPL7RuleMaxCntResponse()
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


    def DescribeBaradData(self, request):
        """爲大禹子産品提供業務轉發指标數據的介面

        :param request: Request instance for DescribeBaradData.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeBaradDataRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeBaradDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBaradData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBaradDataResponse()
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


    def DescribeBasicCCThreshold(self, request):
        """獲取基礎防護CC防護阈值

        :param request: Request instance for DescribeBasicCCThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeBasicCCThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeBasicCCThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBasicCCThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicCCThresholdResponse()
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


    def DescribeBasicDeviceThreshold(self, request):
        """獲取基礎防護黑洞阈值

        :param request: Request instance for DescribeBasicDeviceThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeBasicDeviceThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeBasicDeviceThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBasicDeviceThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicDeviceThresholdResponse()
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


    def DescribeCCAlarmThreshold(self, request):
        """獲取高防包、高防IP、高防IP專業版、棋牌盾産品設置CC攻擊的告警通知阈值

        :param request: Request instance for DescribeCCAlarmThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCAlarmThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCAlarmThresholdResponse()
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


    def DescribeCCEvList(self, request):
        """獲取CC攻擊事件清單

        :param request: Request instance for DescribeCCEvList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCEvListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCEvListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCEvList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCEvListResponse()
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


    def DescribeCCFrequencyRules(self, request):
        """獲取CC防護的訪問頻率控制規則

        :param request: Request instance for DescribeCCFrequencyRules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCFrequencyRulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCFrequencyRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCFrequencyRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCFrequencyRulesResponse()
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


    def DescribeCCIpAllowDeny(self, request):
        """獲取CC的IP黑白名單

        :param request: Request instance for DescribeCCIpAllowDeny.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCIpAllowDenyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCIpAllowDenyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCIpAllowDeny", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCIpAllowDenyResponse()
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


    def DescribeCCSelfDefinePolicy(self, request):
        """獲取CC自定義策略

        :param request: Request instance for DescribeCCSelfDefinePolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCSelfDefinePolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCSelfDefinePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCSelfDefinePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCSelfDefinePolicyResponse()
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


    def DescribeCCTrend(self, request):
        """獲取CC攻擊指标數據，包括總請求峰值(QPS)和攻擊請求(QPS)

        :param request: Request instance for DescribeCCTrend.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCTrendRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCTrendResponse()
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


    def DescribeCCUrlAllow(self, request):
        """獲取CC的Url白名單

        :param request: Request instance for DescribeCCUrlAllow.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCUrlAllowRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCUrlAllowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCUrlAllow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCUrlAllowResponse()
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


    def DescribeDDoSAlarmThreshold(self, request):
        """獲取高防包、高防IP、高防IP專業版、棋牌盾産品設置DDoS攻擊的告警通知阈值

        :param request: Request instance for DescribeDDoSAlarmThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSAlarmThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAlarmThresholdResponse()
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


    def DescribeDDoSAttackIPRegionMap(self, request):
        """獲取DDoS攻擊源IP地域分布圖，支援全球攻擊分布和國内省份攻擊分布；

        :param request: Request instance for DescribeDDoSAttackIPRegionMap.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSAttackIPRegionMapRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSAttackIPRegionMapResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSAttackIPRegionMap", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackIPRegionMapResponse()
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


    def DescribeDDoSAttackSource(self, request):
        """獲取DDoS攻擊源清單

        :param request: Request instance for DescribeDDoSAttackSource.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSAttackSourceRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSAttackSourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSAttackSource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackSourceResponse()
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


    def DescribeDDoSCount(self, request):
        """獲取DDoS攻擊占比分析

        :param request: Request instance for DescribeDDoSCount.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSCountRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSCountResponse()
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


    def DescribeDDoSDefendStatus(self, request):
        """獲取DDoS防護狀态（臨時關閉狀态），支援産品：基礎防護，獨享包，共享包，高防IP，高防IP專業版；調用此介面是獲取當前是否有設置臨時關閉DDoS防護狀态，如果有設置會返回臨時關閉的時長等參數。

        :param request: Request instance for DescribeDDoSDefendStatus.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSDefendStatusRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSDefendStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSDefendStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSDefendStatusResponse()
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


    def DescribeDDoSEvInfo(self, request):
        """獲取DDoS攻擊事件詳情

        :param request: Request instance for DescribeDDoSEvInfo.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvInfoRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSEvInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSEvInfoResponse()
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


    def DescribeDDoSEvList(self, request):
        """獲取DDoS攻擊事件清單

        :param request: Request instance for DescribeDDoSEvList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSEvList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSEvListResponse()
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


    def DescribeDDoSIpLog(self, request):
        """獲取DDoSIP攻擊日志

        :param request: Request instance for DescribeDDoSIpLog.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSIpLogRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSIpLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSIpLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSIpLogResponse()
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


    def DescribeDDoSNetCount(self, request):
        """獲取高防IP專業版資源的DDoS攻擊占比分析

        :param request: Request instance for DescribeDDoSNetCount.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetCountRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetCountResponse()
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


    def DescribeDDoSNetEvInfo(self, request):
        """獲取高防IP專業版資源的DDoS攻擊事件詳情

        :param request: Request instance for DescribeDDoSNetEvInfo.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvInfoRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetEvInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetEvInfoResponse()
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


    def DescribeDDoSNetEvList(self, request):
        """獲取高防IP專業版資源的DDoS攻擊事件清單

        :param request: Request instance for DescribeDDoSNetEvList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetEvList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetEvListResponse()
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


    def DescribeDDoSNetIpLog(self, request):
        """獲取高防IP專業版資源的DDoSIP攻擊日志

        :param request: Request instance for DescribeDDoSNetIpLog.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetIpLogRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetIpLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetIpLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetIpLogResponse()
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


    def DescribeDDoSNetTrend(self, request):
        """獲取高防IP專業版資源的DDoS攻擊指标數據

        :param request: Request instance for DescribeDDoSNetTrend.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetTrendRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetTrendResponse()
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


    def DescribeDDoSPolicy(self, request):
        """獲取DDoS高級策略

        :param request: Request instance for DescribeDDoSPolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSPolicyResponse()
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


    def DescribeDDoSTrend(self, request):
        """獲取DDoS攻擊流量頻寬和攻擊包速率數據

        :param request: Request instance for DescribeDDoSTrend.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSTrendRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSTrendResponse()
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


    def DescribeDDoSUsedStatis(self, request):
        """統計用戶的高防資源的使用天數和DDoS攻擊防護次數

        :param request: Request instance for DescribeDDoSUsedStatis.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSUsedStatisRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSUsedStatisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSUsedStatis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSUsedStatisResponse()
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


    def DescribeIPProductInfo(self, request):
        """獲取獨享包或共享包IP對應的雲資産訊息，只支援獨享包和共享包的IP

        :param request: Request instance for DescribeIPProductInfo.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeIPProductInfoRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeIPProductInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIPProductInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIPProductInfoResponse()
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


    def DescribeInsurePacks(self, request):
        """獲取保險包套餐清單

        :param request: Request instance for DescribeInsurePacks.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeInsurePacksRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeInsurePacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInsurePacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInsurePacksResponse()
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


    def DescribeIpBlockList(self, request):
        """獲取IP封堵清單

        :param request: Request instance for DescribeIpBlockList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeIpBlockListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeIpBlockListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpBlockList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpBlockListResponse()
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


    def DescribeIpUnBlockList(self, request):
        """獲取IP解封記錄

        :param request: Request instance for DescribeIpUnBlockList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeIpUnBlockListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeIpUnBlockListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpUnBlockList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpUnBlockListResponse()
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


    def DescribeL4HealthConfig(self, request):
        """導出四層健康檢查配置

        :param request: Request instance for DescribeL4HealthConfig.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeL4HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeL4HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4HealthConfigResponse()
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


    def DescribeL4RulesErrHealth(self, request):
        """獲取L4轉發規則健康檢查異常結果

        :param request: Request instance for DescribeL4RulesErrHealth.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeL4RulesErrHealthRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeL4RulesErrHealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4RulesErrHealth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4RulesErrHealthResponse()
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


    def DescribeL7HealthConfig(self, request):
        """導出七層健康檢查配置

        :param request: Request instance for DescribeL7HealthConfig.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeL7HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeL7HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7HealthConfigResponse()
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


    def DescribeNewL4Rules(self, request):
        """獲取L4轉發規則

        :param request: Request instance for DescribeNewL4Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeNewL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeNewL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNewL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNewL4RulesResponse()
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


    def DescribeNewL4RulesErrHealth(self, request):
        """獲取L4轉發規則健康檢查異常結果

        :param request: Request instance for DescribeNewL4RulesErrHealth.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeNewL4RulesErrHealthRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeNewL4RulesErrHealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNewL4RulesErrHealth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNewL4RulesErrHealthResponse()
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


    def DescribeNewL7RulesErrHealth(self, request):
        """獲取L7轉發規則健康檢查異常結果

        :param request: Request instance for DescribeNewL7RulesErrHealth.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeNewL7RulesErrHealthRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeNewL7RulesErrHealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNewL7RulesErrHealth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNewL7RulesErrHealthResponse()
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


    def DescribePackIndex(self, request):
        """獲取産品總覽統計，支援高防包、高防IP、高防IP專業版；

        :param request: Request instance for DescribePackIndex.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribePackIndexRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribePackIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePackIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePackIndexResponse()
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


    def DescribePcap(self, request):
        """下載攻擊事件的pcap包

        :param request: Request instance for DescribePcap.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribePcapRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribePcapResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePcap", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePcapResponse()
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


    def DescribePolicyCase(self, request):
        """獲取策略場景

        :param request: Request instance for DescribePolicyCase.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribePolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribePolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyCaseResponse()
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


    def DescribeResIpList(self, request):
        """獲取資源的IP清單

        :param request: Request instance for DescribeResIpList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeResIpListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeResIpListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResIpList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResIpListResponse()
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


    def DescribeResourceList(self, request):
        """獲取資源清單

        :param request: Request instance for DescribeResourceList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeResourceListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeResourceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceListResponse()
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


    def DescribeRuleSets(self, request):
        """獲取資源的規則數

        :param request: Request instance for DescribeRuleSets.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeRuleSetsRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeRuleSetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRuleSets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRuleSetsResponse()
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


    def DescribeSchedulingDomainList(self, request):
        """獲取調度域名清單

        :param request: Request instance for DescribeSchedulingDomainList.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeSchedulingDomainListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeSchedulingDomainListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSchedulingDomainList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSchedulingDomainListResponse()
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


    def DescribeSecIndex(self, request):
        """獲取本月安全統計

        :param request: Request instance for DescribeSecIndex.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeSecIndexRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeSecIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecIndexResponse()
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


    def DescribeSourceIpSegment(self, request):
        """獲取回源IP段，支援的産品：高防IP，高防IP專業版；

        :param request: Request instance for DescribeSourceIpSegment.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeSourceIpSegmentRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeSourceIpSegmentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSourceIpSegment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSourceIpSegmentResponse()
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


    def DescribeTransmitStatis(self, request):
        """獲取業務轉發統計數據，支援轉發流量和轉發包速率

        :param request: Request instance for DescribeTransmitStatis.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeTransmitStatisRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeTransmitStatisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTransmitStatis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTransmitStatisResponse()
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


    def DescribeUnBlockStatis(self, request):
        """獲取黑洞解封次數

        :param request: Request instance for DescribeUnBlockStatis.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeUnBlockStatisRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeUnBlockStatisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnBlockStatis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnBlockStatisResponse()
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


    def DescribleL4Rules(self, request):
        """獲取四層轉發規則

        :param request: Request instance for DescribleL4Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribleL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribleL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribleL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribleL4RulesResponse()
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


    def DescribleL7Rules(self, request):
        """獲取七層轉發規則

        :param request: Request instance for DescribleL7Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribleL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribleL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribleL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribleL7RulesResponse()
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


    def DescribleNewL7Rules(self, request):
        """獲取7層規則

        :param request: Request instance for DescribleNewL7Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribleNewL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribleNewL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribleNewL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribleNewL7RulesResponse()
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


    def DescribleRegionCount(self, request):
        """獲取地域的資源實例數

        :param request: Request instance for DescribleRegionCount.
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribleRegionCountRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribleRegionCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribleRegionCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribleRegionCountResponse()
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


    def ModifyCCAlarmThreshold(self, request):
        """爲高防包、高防IP、高防IP專業版、棋牌盾産品設置CC攻擊的告警通知阈值

        :param request: Request instance for ModifyCCAlarmThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCAlarmThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCAlarmThresholdResponse()
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


    def ModifyCCFrequencyRules(self, request):
        """修改CC防護的訪問頻率控制規則

        :param request: Request instance for ModifyCCFrequencyRules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCFrequencyRulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCFrequencyRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCFrequencyRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCFrequencyRulesResponse()
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


    def ModifyCCFrequencyRulesStatus(self, request):
        """開啓或關閉CC防護的訪問頻率控制規則

        :param request: Request instance for ModifyCCFrequencyRulesStatus.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCFrequencyRulesStatusRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCFrequencyRulesStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCFrequencyRulesStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCFrequencyRulesStatusResponse()
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


    def ModifyCCHostProtection(self, request):
        """開啓或關閉CC域名防護

        :param request: Request instance for ModifyCCHostProtection.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCHostProtectionRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCHostProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCHostProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCHostProtectionResponse()
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


    def ModifyCCIpAllowDeny(self, request):
        """添加或删除CC的IP黑白名單

        :param request: Request instance for ModifyCCIpAllowDeny.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCIpAllowDenyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCIpAllowDenyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCIpAllowDeny", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCIpAllowDenyResponse()
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


    def ModifyCCLevel(self, request):
        """修改CC防護等級

        :param request: Request instance for ModifyCCLevel.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCLevelRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCLevelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCLevel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCLevelResponse()
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


    def ModifyCCPolicySwitch(self, request):
        """修改CC自定義策略開關

        :param request: Request instance for ModifyCCPolicySwitch.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCPolicySwitchRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCPolicySwitchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCPolicySwitch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCPolicySwitchResponse()
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


    def ModifyCCSelfDefinePolicy(self, request):
        """修改CC自定義策略

        :param request: Request instance for ModifyCCSelfDefinePolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCSelfDefinePolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCSelfDefinePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCSelfDefinePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCSelfDefinePolicyResponse()
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


    def ModifyCCThreshold(self, request):
        """修改CC的防護阈值

        :param request: Request instance for ModifyCCThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCThresholdResponse()
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


    def ModifyCCUrlAllow(self, request):
        """添加或删除CC的URL白名單

        :param request: Request instance for ModifyCCUrlAllow.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCUrlAllowRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCUrlAllowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCUrlAllow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCUrlAllowResponse()
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


    def ModifyDDoSAIStatus(self, request):
        """讀取或修改DDoS的AI防護狀态

        :param request: Request instance for ModifyDDoSAIStatus.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSAIStatusRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSAIStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSAIStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSAIStatusResponse()
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


    def ModifyDDoSAlarmThreshold(self, request):
        """爲高防包、高防IP、高防IP專業版、棋牌盾等産品設置DDoS攻擊的告警通知阈值

        :param request: Request instance for ModifyDDoSAlarmThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSAlarmThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSAlarmThresholdResponse()
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


    def ModifyDDoSDefendStatus(self, request):
        """開啓或關閉DDoS防護狀态，調用此介面允許臨時關閉DDoS防護一段時間，等時間到了會自動開啓DDoS防護；

        :param request: Request instance for ModifyDDoSDefendStatus.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSDefendStatusRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSDefendStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSDefendStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSDefendStatusResponse()
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


    def ModifyDDoSLevel(self, request):
        """讀取或修改DDoS的防護等級

        :param request: Request instance for ModifyDDoSLevel.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSLevelRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSLevelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSLevel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSLevelResponse()
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


    def ModifyDDoSPolicy(self, request):
        """修改DDoS高級策略

        :param request: Request instance for ModifyDDoSPolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyResponse()
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


    def ModifyDDoSPolicyCase(self, request):
        """修改策略場景

        :param request: Request instance for ModifyDDoSPolicyCase.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSPolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyCaseResponse()
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


    def ModifyDDoSPolicyName(self, request):
        """修改DDoS高級策略名稱

        :param request: Request instance for ModifyDDoSPolicyName.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyNameRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSPolicyName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyNameResponse()
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


    def ModifyDDoSSwitch(self, request):
        """開啓或關閉DDoS防護，只支援基礎防護産品；

        :param request: Request instance for ModifyDDoSSwitch.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSSwitchRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSSwitchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSSwitch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSSwitchResponse()
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


    def ModifyDDoSThreshold(self, request):
        """修改DDoS清洗阈值

        :param request: Request instance for ModifyDDoSThreshold.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSThresholdResponse()
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


    def ModifyDDoSWaterKey(self, request):
        """支援浮水印金鑰的添加，删除，開啓，關閉

        :param request: Request instance for ModifyDDoSWaterKey.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSWaterKeyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSWaterKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSWaterKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSWaterKeyResponse()
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


    def ModifyElasticLimit(self, request):
        """修改彈性防護阈值

        :param request: Request instance for ModifyElasticLimit.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyElasticLimitRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyElasticLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyElasticLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyElasticLimitResponse()
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


    def ModifyL4Health(self, request):
        """修改L4轉發規則健康檢查參數，支援的子産品：高防IP、高防IP專業版

        :param request: Request instance for ModifyL4Health.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL4HealthRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL4HealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4Health", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4HealthResponse()
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


    def ModifyL4KeepTime(self, request):
        """修改L4轉發規則的會話保持，支援的子産品：高防IP、高防IP專業版

        :param request: Request instance for ModifyL4KeepTime.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL4KeepTimeRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL4KeepTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4KeepTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4KeepTimeResponse()
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


    def ModifyL4Rules(self, request):
        """修改L4轉發規則

        :param request: Request instance for ModifyL4Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4RulesResponse()
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


    def ModifyL7Rules(self, request):
        """修改L7轉發規則

        :param request: Request instance for ModifyL7Rules.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7RulesResponse()
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


    def ModifyNetReturnSwitch(self, request):
        """在客戶收攻擊或者被封堵時，切回到源站，并設置回切的時長

        :param request: Request instance for ModifyNetReturnSwitch.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyNetReturnSwitchRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyNetReturnSwitchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetReturnSwitch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetReturnSwitchResponse()
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


    def ModifyResBindDDoSPolicy(self, request):
        """資源實例綁定DDoS高級策略

        :param request: Request instance for ModifyResBindDDoSPolicy.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyResBindDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyResBindDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyResBindDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResBindDDoSPolicyResponse()
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


    def ModifyResourceRenewFlag(self, request):
        """修改資源自動續約标記

        :param request: Request instance for ModifyResourceRenewFlag.
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyResourceRenewFlagRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyResourceRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyResourceRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourceRenewFlagResponse()
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