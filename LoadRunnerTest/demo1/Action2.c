Action2()
{


	// post json



	/*
	 * step01 ��¼ 
	 */


	// ��鷵��ֵ��û��code=200
	// �������ҪдҪ���������ǰ��

	web_reg_find("Text=code\": 200,",
		LAST);


	// ������ȡtoken
	web_reg_save_param("userToken",
		"LB=token\": \"",
		"RB=\"",
		LAST);

	// ���ϵ�
	// 1. �ű������ü��ϵ�
	// 2. controller�����ü��ϵ�ִ�в���
	lr_rendezvous("login");

	// �����¼
	
	lr_start_transaction("user_login_and_logout");

	lr_start_transaction("login");

	web_custom_request("LUXLOGIN",
		"URL=http://132.232.44.158:5000/userLogin/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"username\":\"{username}\", \"password\":\"{password}\", \"captcha\":\"123456\"}", // ������
		LAST);

	lr_end_transaction("login", LR_AUTO);


	/*
	 * step02 �˳�
	 */
	web_reg_find("Text=code\": 200,",
		LAST);

	// 1. �ű������ü��ϵ�
	// 2. controller�����ü��ϵ�ִ�в���
	lr_rendezvous("logout");

	
	lr_start_transaction("logout");

	web_custom_request("logout",
		"URL=http://132.232.44.158:5000/userLogout/",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"token\": \"{userToken}\"}", // ���ñ���
		LAST);
	
	lr_end_transaction("logout", LR_AUTO);

	lr_end_transaction("user_login_and_logout", LR_AUTO);

	return 0;
}
