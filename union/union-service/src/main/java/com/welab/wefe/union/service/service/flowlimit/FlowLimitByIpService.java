package com.welab.wefe.union.service.service.flowlimit;

import com.alibaba.fastjson.JSONObject;
import com.welab.wefe.common.data.mongodb.constant.FlowLimitStrategyTypeEnum;
import com.welab.wefe.common.web.api.base.AbstractApi;
import com.welab.wefe.common.web.api.base.Api;
import com.welab.wefe.common.web.api.base.FlowLimitByIp;
import com.welab.wefe.common.web.util.HttpServletRequestUtil;

import javax.servlet.http.HttpServletRequest;

/**
 * IP address flow control
 *
 * @author aaron.li
 * @date 2021/10/22 15:50
 **/
public class FlowLimitByIpService extends AbstractFlowLimitService {

    public FlowLimitByIpService(HttpServletRequest httpServletRequest, AbstractApi<?, ?> api, JSONObject params) {
        super(httpServletRequest, api, params);
    }

    @Override
    protected String getFlowLimitKey() {
        String clientIp = HttpServletRequestUtil.getClientIp(getHttpServletRequest());
        String path = getApi().getClass().getAnnotation(Api.class).path();
        return path + "_" + FlowLimitStrategyTypeEnum.IP + "_" + clientIp;
    }

    @Override
    protected FlowLimitStrategyTypeEnum getFlowLimitStrategyType() {
        return FlowLimitStrategyTypeEnum.IP;
    }

    @Override
    protected String getFlowLimitStrategyValue() {
        return HttpServletRequestUtil.getClientIp(getHttpServletRequest());
    }

    @Override
    protected int getFlowLimitCount() {
        return getApi().getClass().getAnnotation(FlowLimitByIp.class).count();
    }

    @Override
    protected long getFlowLimitSecond() {
        return getApi().getClass().getAnnotation(FlowLimitByIp.class).second();
    }

    @Override
    protected String getFlowLimitExceptionTips() {
        return "该IP访问次数过于频繁，请稍后再试";
    }
}
