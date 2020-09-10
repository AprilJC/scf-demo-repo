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
from tencentcloud.sqlserver.v20180328 import models


class SqlserverClient(AbstractClient):
    _apiVersion = '2018-03-28'
    _endpoint = 'sqlserver.tencentcloudapi.com'


    def CreateAccount(self, request):
        """本介面（CreateAccount）用于創建實例賬号

        :param request: 調用CreateAccount所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
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


    def CreateBackup(self, request):
        """本介面(CreateBackup)用于創建備份。

        :param request: 調用CreateBackup所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupResponse()
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


    def CreateDB(self, request):
        """本介面（CreateDB）用于創建資料庫。

        :param request: 調用CreateDB所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBResponse()
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


    def CreateDBInstances(self, request):
        """本介面（CreateDBInstances）用于創建實例。

        :param request: 調用CreateDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstancesResponse()
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


    def CreateMigration(self, request):
        """本介面（CreateMigration）作用是創建一個遷移任務

        :param request: 調用CreateMigration所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrationResponse()
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


    def DeleteAccount(self, request):
        """本介面（DeleteAccount）用于删除實例賬号。

        :param request: 調用DeleteAccount所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
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


    def DeleteDB(self, request):
        """本介面(DeleteDB)用于删除資料庫。

        :param request: 調用DeleteDB所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDBResponse()
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


    def DeleteMigration(self, request):
        """本介面（DeleteMigration）用于删除遷移任務

        :param request: 調用DeleteMigration所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMigrationResponse()
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


    def DescribeAccounts(self, request):
        """本介面（DescribeAccounts）用于拉取實例帳戶清單。

        :param request: 調用DescribeAccounts所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeBackups(self, request):
        """本介面(DescribeBackups)用于查詢備份清單。

        :param request: 調用DescribeBackups所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupsResponse()
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


    def DescribeDBInstances(self, request):
        """本介面(DescribeDBInstances)用于查詢實例清單。

        :param request: 調用DescribeDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
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


    def DescribeDBs(self, request):
        """本介面（DescribeDBs）用于查詢資料庫清單。

        :param request: 調用DescribeDBs所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBsResponse()
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


    def DescribeFlowStatus(self, request):
        """本介面(DescribeFlowStatus)用于查詢流程狀态。

        :param request: 調用DescribeFlowStatus所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowStatusResponse()
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


    def DescribeMigrationDetail(self, request):
        """本介面（DescribeMigrationDetail）用于查詢遷移任務的詳細情況

        :param request: 調用DescribeMigrationDetail所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrationDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrationDetailResponse()
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


    def DescribeMigrations(self, request):
        """本介面（DescribeMigrations）根據輸入的限定條件，查詢符合條件的遷移任務清單

        :param request: 調用DescribeMigrations所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrationsResponse()
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


    def DescribeOrders(self, request):
        """本介面（DescribeOrders）用于查詢訂單訊息

        :param request: 調用DescribeOrders所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOrders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrdersResponse()
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


    def DescribeProductConfig(self, request):
        """本介面 (DescribeProductConfig) 用于查詢售賣規格配置。

        :param request: 調用DescribeProductConfig所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductConfigResponse()
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


    def DescribeRegions(self, request):
        """本介面 (DescribeRegions) 用于查詢售賣地域訊息。

        :param request: 調用DescribeRegions所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeRollbackTime(self, request):
        """本介面（DescribeRollbackTime）用于查詢實例可回檔時間範圍

        :param request: 調用DescribeRollbackTime所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRollbackTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackTimeResponse()
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


    def DescribeSlowlogs(self, request):
        """本介面（DescribeSlowlogs）用于獲取慢查詢日志文件訊息

        :param request: 調用DescribeSlowlogs所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowlogsResponse()
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


    def DescribeZones(self, request):
        """本介面 (DescribeZones) 用于查詢當前可售賣的可用區訊息。

        :param request: 調用DescribeZones所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
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


    def InquiryPriceCreateDBInstances(self, request):
        """本介面（InquiryPriceCreateDBInstances）用于查詢申請實例價格。

        :param request: 調用InquiryPriceCreateDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateDBInstancesResponse()
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


    def InquiryPriceRenewDBInstance(self, request):
        """本介面（InquiryPriceRenewDBInstance）用于查詢續約實例的價格。

        :param request: 調用InquiryPriceRenewDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceRenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewDBInstanceResponse()
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


    def InquiryPriceUpgradeDBInstance(self, request):
        """本介面（InquiryPriceUpgradeDBInstance）用于查詢升級實例的價格。

        :param request: 調用InquiryPriceUpgradeDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeDBInstanceResponse()
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


    def ModifyAccountPrivilege(self, request):
        """本介面（ModifyAccountPrivilege）用于修改實例帳戶權限。

        :param request: 調用ModifyAccountPrivilege所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountPrivilege", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountPrivilegeResponse()
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


    def ModifyAccountRemark(self, request):
        """本介面（ModifyAccountRemark）用于修改帳戶備注。

        :param request: 調用ModifyAccountRemark所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountRemarkResponse()
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


    def ModifyDBInstanceName(self, request):
        """本介面（ModifyDBInstanceName）用于修改實例名字。

        :param request: 調用ModifyDBInstanceName所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
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


    def ModifyDBInstanceProject(self, request):
        """本介面（ModifyDBInstanceProject）用于修改資料庫實例所屬項目。

        :param request: 調用ModifyDBInstanceProject所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceProjectResponse()
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


    def ModifyDBInstanceRenewFlag(self, request):
        """本介面（ModifyDBInstanceRenewFlag）用于修改實例續約标記

        :param request: 調用ModifyDBInstanceRenewFlag所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceRenewFlagRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceRenewFlagResponse()
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


    def ModifyDBName(self, request):
        """本介面（ModifyDBName）用于更新資料庫名。

        :param request: 調用ModifyDBName所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBNameResponse()
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


    def ModifyDBRemark(self, request):
        """本介面（ModifyDBRemark）用于修改資料庫備注。

        :param request: 調用ModifyDBRemark所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBRemarkResponse()
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


    def ModifyMigration(self, request):
        """本介面（ModifyMigration）可以修改已有的遷移任務訊息

        :param request: 調用ModifyMigration所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrationResponse()
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


    def RenewDBInstance(self, request):
        """本介面（RenewDBInstance）用于續約實例。

        :param request: 調用RenewDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDBInstanceResponse()
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


    def ResetAccountPassword(self, request):
        """本介面（ResetAccountPassword）用于重置實例的帳戶密碼。

        :param request: 調用ResetAccountPassword所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAccountPasswordResponse()
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


    def RestartDBInstance(self, request):
        """本介面（RestartDBInstance）用于重啓資料庫實例。

        :param request: 調用RestartDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartDBInstanceResponse()
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


    def RestoreInstance(self, request):
        """本介面（RestoreInstance）用于根據備份文件恢複實例。

        :param request: 調用RestoreInstance所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreInstanceResponse()
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


    def RollbackInstance(self, request):
        """本介面（RollbackInstance）用于回檔實例

        :param request: 調用RollbackInstance所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RollbackInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollbackInstanceResponse()
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


    def RunMigration(self, request):
        """本介面（RunMigration）用于啓動遷移任務，開始遷移

        :param request: 調用RunMigration所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunMigrationResponse()
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


    def UpgradeDBInstance(self, request):
        """本介面（UpgradeDBInstance）用于升級實例

        :param request: 調用UpgradeDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceResponse()
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