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
from tencentcloud.autoscaling.v20180419 import models


class AutoscalingClient(AbstractClient):
    _apiVersion = '2018-04-19'
    _endpoint = 'as.tencentcloudapi.com'


    def AttachInstances(self, request):
        """本介面（AttachInstances）用于将 CVM 實例添加到伸縮組。

        :param request: Request instance for AttachInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.AttachInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.AttachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachInstancesResponse()
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


    def CompleteLifecycleAction(self, request):
        """本介面（CompleteLifecycleAction）用于完成生命週期動作。

        * 用戶通過調用本介面，指定一個具體的生命週期挂鈎的結果（“CONITNUE”或者“ABANDON”）。如果一直不調用本介面，則生命週期挂鈎會在超時後按照“DefaultResult”進行處理。

        :param request: Request instance for CompleteLifecycleAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CompleteLifecycleActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CompleteLifecycleActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteLifecycleAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteLifecycleActionResponse()
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


    def CreateAutoScalingGroup(self, request):
        """本介面（CreateAutoScalingGroup）用于創建伸縮組

        :param request: Request instance for CreateAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoScalingGroupResponse()
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


    def CreateAutoScalingGroupFromInstance(self, request):
        """本介面（CreateAutoScalingGroupFromInstance）用于根據實例創建啓動配置及伸縮組。

        說明：根據按包年包月計費的實例所創建的伸縮組，其擴容的實例爲按量計費實例。

        :param request: Request instance for CreateAutoScalingGroupFromInstance.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupFromInstanceRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupFromInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAutoScalingGroupFromInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoScalingGroupFromInstanceResponse()
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


    def CreateLaunchConfiguration(self, request):
        """本介面（CreateLaunchConfiguration）用于創建新的啓動配置。

        * 啓動配置，可以通過 `ModifyLaunchConfigurationAttributes` 修改少量欄位。如需使用新的啓動配置，建議重新創建啓動配置。

        * 每個項目最多只能創建20個啓動配置，詳見[使用限制](https://cloud.tencent.com/document/product/377/3120)。

        :param request: Request instance for CreateLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLaunchConfigurationResponse()
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


    def CreateLifecycleHook(self, request):
        """本介面（CreateLifecycleHook）用于創建生命週期挂鈎。

        * 您可以爲生命週期挂鈎配置訊息通知，彈性伸縮會通知您的CMQ訊息隊列，通知内容形如：

        ```
        {
        	"Service": "Tencent Cloud Auto Scaling",
        	"Time": "2019-03-14T10:15:11Z",
        	"AppId": "1251783334",
        	"ActivityId": "asa-fznnvrja",
        	"AutoScalingGroupId": "asg-rrrrtttt",
        	"LifecycleHookId": "ash-xxxxyyyy",
        	"LifecycleHookName": "my-hook",
        	"LifecycleActionToken": "3080e1c9-0efe-4dd7-ad3b-90cd6618298f",
        	"InstanceId": "ins-aaaabbbb",
        	"LifecycleTransition": "INSTANCE_LAUNCHING",
        	"NotificationMetadata": ""
        }
        ```

        :param request: Request instance for CreateLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLifecycleHookResponse()
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


    def CreateNotificationConfiguration(self, request):
        """本介面（CreateNotificationConfiguration）用于創建通知。

        :param request: Request instance for CreateNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNotificationConfigurationResponse()
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


    def CreatePaiInstance(self, request):
        """本介面 (CreatePaiInstance) 用于創建一個指定配置的PAI實例。

        :param request: Request instance for CreatePaiInstance.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreatePaiInstanceRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreatePaiInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePaiInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePaiInstanceResponse()
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


    def CreateScalingPolicy(self, request):
        """本介面（CreateScalingPolicy）用于創建告警觸發策略。

        :param request: Request instance for CreateScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScalingPolicyResponse()
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


    def CreateScheduledAction(self, request):
        """本介面（CreateScheduledAction）用于創建定時任務。

        :param request: Request instance for CreateScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScheduledActionResponse()
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


    def DeleteAutoScalingGroup(self, request):
        """本介面（DeleteAutoScalingGroup）用于删除指定伸縮組，删除前提是伸縮組内無實例且當前未在執行伸縮活動。

        :param request: Request instance for DeleteAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAutoScalingGroupResponse()
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


    def DeleteLaunchConfiguration(self, request):
        """本介面（DeleteLaunchConfiguration）用于删除啓動配置。

        * 若啓動配置在伸縮組中屬于生效狀态，則該啓動配置不允許删除。

        :param request: Request instance for DeleteLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLaunchConfigurationResponse()
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


    def DeleteLifecycleHook(self, request):
        """本介面（DeleteLifecycleHook）用于删除生命週期挂鈎。

        :param request: Request instance for DeleteLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLifecycleHookResponse()
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


    def DeleteNotificationConfiguration(self, request):
        """本介面（DeleteNotificationConfiguration）用于删除特定的通知。

        :param request: Request instance for DeleteNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNotificationConfigurationResponse()
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


    def DeleteScalingPolicy(self, request):
        """本介面（DeleteScalingPolicy）用于删除告警觸發策略。

        :param request: Request instance for DeleteScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScalingPolicyResponse()
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


    def DeleteScheduledAction(self, request):
        """本介面（DeleteScheduledAction）用于删除特定的定時任務。

        :param request: Request instance for DeleteScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScheduledActionResponse()
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


    def DescribeAccountLimits(self, request):
        """本介面（DescribeAccountLimits）用于查詢用戶帳戶在彈性伸縮中的資源限制。

        :param request: Request instance for DescribeAccountLimits.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAccountLimitsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAccountLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountLimitsResponse()
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


    def DescribeAutoScalingActivities(self, request):
        """本介面（DescribeAutoScalingActivities）用于查詢伸縮組的伸縮活動記錄。

        :param request: Request instance for DescribeAutoScalingActivities.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingActivitiesResponse()
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


    def DescribeAutoScalingGroupLastActivities(self, request):
        """本介面（DescribeAutoScalingGroupLastActivities）用于查詢伸縮組的最新一次伸縮活動記錄。

        :param request: Request instance for DescribeAutoScalingGroupLastActivities.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupLastActivitiesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupLastActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingGroupLastActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingGroupLastActivitiesResponse()
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


    def DescribeAutoScalingGroups(self, request):
        """本介面（DescribeAutoScalingGroups）用于查詢伸縮組訊息。

        * 可以根據伸縮組ID、伸縮組名稱或者啓動配置ID等訊息來查詢伸縮組的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的伸縮組。

        :param request: Request instance for DescribeAutoScalingGroups.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingGroupsResponse()
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


    def DescribeAutoScalingInstances(self, request):
        """本介面（DescribeAutoScalingInstances）用于查詢彈性伸縮關聯實例的訊息。

        * 可以根據實例ID、伸縮組ID等訊息來查詢實例的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的實例。

        :param request: Request instance for DescribeAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingInstancesResponse()
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


    def DescribeLaunchConfigurations(self, request):
        """本介面（DescribeLaunchConfigurations）用于查詢啓動配置的訊息。

        * 可以根據啓動配置ID、啓動配置名稱等訊息來查詢啓動配置的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的啓動配置。

        :param request: Request instance for DescribeLaunchConfigurations.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLaunchConfigurations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLaunchConfigurationsResponse()
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


    def DescribeLifecycleHooks(self, request):
        """本介面（DescribeLifecycleHooks）用于查詢生命週期挂鈎訊息。

        * 可以根據伸縮組ID、生命週期挂鈎ID或者生命週期挂鈎名稱等訊息來查詢生命週期挂鈎的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的生命週期挂鈎。

        :param request: Request instance for DescribeLifecycleHooks.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLifecycleHooksRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLifecycleHooksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLifecycleHooks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLifecycleHooksResponse()
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


    def DescribeNotificationConfigurations(self, request):
        """本介面 (DescribeNotificationConfigurations) 用于查詢一個或多個通知的詳細訊息。

        可以根據通知ID、伸縮組ID等訊息來查詢通知的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        如果參數爲空，返回當前用戶一定數量（Limit所指定的數量，預設爲20）的通知。

        :param request: Request instance for DescribeNotificationConfigurations.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotificationConfigurations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotificationConfigurationsResponse()
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


    def DescribePaiInstances(self, request):
        """本介面（DescribePaiInstances）用于查詢PAI實例訊息。

        * 可以根據實例ID、實例域名等訊息來查詢PAI實例的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的PAI實例。

        :param request: Request instance for DescribePaiInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribePaiInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribePaiInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePaiInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePaiInstancesResponse()
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


    def DescribeScalingPolicies(self, request):
        """本介面（DescribeScalingPolicies）用于查詢告警觸發策略。

        :param request: Request instance for DescribeScalingPolicies.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScalingPoliciesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingPoliciesResponse()
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


    def DescribeScheduledActions(self, request):
        """本介面 (DescribeScheduledActions) 用于查詢一個或多個定時任務的詳細訊息。

        * 可以根據定時任務ID、定時任務名稱或者伸縮組ID等訊息來查詢定時任務的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（Limit所指定的數量，預設爲20）的定時任務。

        :param request: Request instance for DescribeScheduledActions.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScheduledActionsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScheduledActionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScheduledActions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScheduledActionsResponse()
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


    def DetachInstances(self, request):
        """本介面（DetachInstances）用于從伸縮組移出 CVM 實例，本介面不會銷毀實例。

        :param request: Request instance for DetachInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DetachInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DetachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachInstancesResponse()
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


    def DisableAutoScalingGroup(self, request):
        """本介面（DisableAutoScalingGroup）用于停用指定伸縮組。

        :param request: Request instance for DisableAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DisableAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DisableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableAutoScalingGroupResponse()
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


    def EnableAutoScalingGroup(self, request):
        """本介面（EnableAutoScalingGroup）用于啓用指定伸縮組。

        :param request: Request instance for EnableAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.EnableAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.EnableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableAutoScalingGroupResponse()
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


    def ExecuteScalingPolicy(self, request):
        """本介面（ExecuteScalingPolicy）用于執行伸縮策略。

        * 可以根據伸縮策略ID執行伸縮策略。
        * 伸縮策略所屬伸縮組處于伸縮活動時，會拒絕執行伸縮策略。

        :param request: Request instance for ExecuteScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ExecuteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ExecuteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExecuteScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExecuteScalingPolicyResponse()
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


    def ModifyAutoScalingGroup(self, request):
        """本介面（ModifyAutoScalingGroup）用于修改伸縮組。

        :param request: Request instance for ModifyAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoScalingGroupResponse()
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


    def ModifyDesiredCapacity(self, request):
        """本介面（ModifyDesiredCapacity）用于修改指定伸縮組的期望實例數

        :param request: Request instance for ModifyDesiredCapacity.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyDesiredCapacityRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyDesiredCapacityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDesiredCapacity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDesiredCapacityResponse()
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


    def ModifyLaunchConfigurationAttributes(self, request):
        """本介面（ModifyLaunchConfigurationAttributes）用于修改啓動配置部分屬性。

        * 修改啓動配置後，已經使用該啓動配置擴容的存量實例不會發生變更，此後使用該啓動配置的新增實例會按照新的配置進行擴容。
        * 本介面支援修改部分簡單類型。

        :param request: Request instance for ModifyLaunchConfigurationAttributes.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLaunchConfigurationAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLaunchConfigurationAttributesResponse()
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


    def ModifyLoadBalancers(self, request):
        """本介面（ModifyLoadBalancers）用于修改伸縮組的負載均衡器。

        * 本介面用于爲伸縮組指定新的負載均衡器配置，采用“完全函蓋”風格，無論之前配置如何，統一按照介面參數配置爲新的負載均衡器。
        * 如果要爲伸縮組清空負載均衡器，則在調用本介面時僅指定伸縮組ID，不指定具體負載均衡器。
        * 本介面會立即修改伸縮組的負載均衡器，并生成一個伸縮活動，異步修改存量實例的負載均衡器。

        :param request: Request instance for ModifyLoadBalancers.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancersRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancersResponse()
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


    def ModifyNotificationConfiguration(self, request):
        """本介面（ModifyNotificationConfiguration）用于修改通知。

        :param request: Request instance for ModifyNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNotificationConfigurationResponse()
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


    def ModifyScalingPolicy(self, request):
        """本介面（ModifyScalingPolicy）用于修改告警觸發策略。

        :param request: Request instance for ModifyScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyScalingPolicyResponse()
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


    def ModifyScheduledAction(self, request):
        """本介面（ModifyScheduledAction）用于修改定時任務。

        :param request: Request instance for ModifyScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyScheduledActionResponse()
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


    def PreviewPaiDomainName(self, request):
        """本介面（PreviewPaiDomainName）用于預覽PAI實例域名。

        :param request: Request instance for PreviewPaiDomainName.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.PreviewPaiDomainNameRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.PreviewPaiDomainNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PreviewPaiDomainName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PreviewPaiDomainNameResponse()
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


    def RemoveInstances(self, request):
        """本介面（RemoveInstances）用于從伸縮組删除 CVM 實例。根據當前的産品邏輯，如果實例由彈性伸縮自動創建，則實例會被銷毀；如果實例系創建後加入伸縮組的，則會從伸縮組中移除，保留實例。

        :param request: Request instance for RemoveInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.RemoveInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveInstancesResponse()
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


    def SetInstancesProtection(self, request):
        """本介面（SetInstancesProtection）用于設置實例移除保護。
        子機設置爲移除保護之後，當發生不健康替換、報警策略、期望值變更等觸發縮容時，将不對此子機縮容操作。

        :param request: Request instance for SetInstancesProtection.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.SetInstancesProtectionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SetInstancesProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetInstancesProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetInstancesProtectionResponse()
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


    def StartAutoScalingInstances(self, request):
        """本介面（StartAutoScalingInstances）用于開啓伸縮組内 CVM 實例。
        * 開機成功，實例轉爲`IN_SERVICE`狀态後，會增加期望實例數，期望實例數不可超過設置的最大值
        * 本介面支援批次操作，每次請求開機實例的上限爲100

        :param request: Request instance for StartAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.StartAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.StartAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartAutoScalingInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartAutoScalingInstancesResponse()
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


    def StopAutoScalingInstances(self, request):
        """本介面（StopAutoScalingInstances）用于關閉伸縮組内 CVM 實例。
        * 關機方式采用`SOFT_FIRST`方式，表示在正常關閉失敗後進行強制關閉
        * 關閉`IN_SERVICE`狀态的實例，會減少期望實例數，期望實例數不可低于設置的最小值
        * 使用`STOP_CHARGING`選項關機，待關機的實例需要滿足[關機不收費條件](https://cloud.tencent.com/document/product/213/19918)
        * 本介面支援批次操作，每次請求關機實例的上限爲100

        :param request: Request instance for StopAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.StopAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.StopAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopAutoScalingInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopAutoScalingInstancesResponse()
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


    def UpgradeLaunchConfiguration(self, request):
        """本介面（UpgradeLaunchConfiguration）用于升級啓動配置。

        * 本介面用于升級啓動配置，采用“完全函蓋”風格，無論之前參數如何，統一按照介面參數設置爲新的配置。對于非必填欄位，不填寫則按照預設值賦值。
        * 升級修改啓動配置後，已經使用該啓動配置擴容的存量實例不會發生變更，此後使用該啓動配置的新增實例會按照新的配置進行擴容。

        :param request: Request instance for UpgradeLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLaunchConfigurationResponse()
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


    def UpgradeLifecycleHook(self, request):
        """本介面（UpgradeLifecycleHook）用于升級生命週期挂鈎。

        * 本介面用于升級生命週期挂鈎，采用“完全函蓋”風格，無論之前參數如何，統一按照介面參數設置爲新的配置。對于非必填欄位，不填寫則按照預設值賦值。

        :param request: Request instance for UpgradeLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLifecycleHookResponse()
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