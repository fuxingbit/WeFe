package com.welab.wefe.common.data.mongodb.entity.sms;

import com.welab.wefe.common.data.mongodb.constant.MongodbTable;
import com.welab.wefe.common.data.mongodb.constant.SmsBusinessTypeEnum;
import com.welab.wefe.common.data.mongodb.entity.AbstractNormalMongoModel;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = MongodbTable.Sms.VERIFICATION_CODE)
public class SmsVerificationCode extends AbstractNormalMongoModel {
    private String mobile;
    private String code;
    private SmsBusinessTypeEnum businessType;

    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public SmsBusinessTypeEnum getBusinessType() {
        return businessType;
    }

    public void setBusinessType(SmsBusinessTypeEnum businessType) {
        this.businessType = businessType;
    }
}
