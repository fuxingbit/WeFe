/**
 * Copyright 2021 Tianmian Tech. All Rights Reserved.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *     http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.welab.wefe.gateway.service.processors;

import com.welab.wefe.gateway.api.meta.basic.BasicMetaProto;
import com.welab.wefe.gateway.api.meta.basic.GatewayMetaProto;
import com.welab.wefe.gateway.base.Processor;
import com.welab.wefe.gateway.cache.SystemConfigCache;
import com.welab.wefe.gateway.common.ReturnStatusBuilder;

/**
 * Refresh system configuration cache processor
 *
 * @author aaron.li
 **/
@Processor(name = "refreshSystemConfigCacheProcessor", desc = "Refresh system configuration cache processor")
public class RefreshSystemConfigCacheProcessor extends AbstractProcessor {
    @Override
    public BasicMetaProto.ReturnStatus preToRemoteProcess(GatewayMetaProto.TransferMeta transferMeta) {
        boolean ret = SystemConfigCache.getInstance().refreshCache();
        return ret ? ReturnStatusBuilder.ok(transferMeta.getSessionId()) : ReturnStatusBuilder.sysExc("刷新系统配置缓存失败", transferMeta.getSessionId());
    }
}
