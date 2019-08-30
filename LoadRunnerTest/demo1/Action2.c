Action2()
{


	// post json



	/*
	 * step01 登录 
	 */


	// 检查返回值有没有code=200
	// 检查点必须要写要检查的请求的前面

	web_reg_find("Text=code\": 200,",
		LAST);


	// 关联获取token
	web_reg_save_param("userToken",
		"LB=token\": \"",
		"RB=\"",
		LAST);

	// 集合点
	// 1. 脚本中设置集合点
	// 2. controller中设置集合点执行策略
	lr_rendezvous("login");

	// 请求登录
	
	lr_start_transaction("user_login_and_logout");

	lr_start_transaction("login");

	web_custom_request("LUXLOGIN",
		"URL=http://132.232.44.158:5000/userLogin/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"username\":\"{username}\", \"password\":\"{password}\", \"captcha\":\"123456\"}", // 参数化
		LAST);

	lr_end_transaction("login", LR_AUTO);


	/*
	 * step02 退出
	 */
	web_reg_find("Text=code\": 200,",
		LAST);

	// 1. 脚本中设置集合点
	// 2. controller中设置集合点执行策略
	lr_rendezvous("logout");

	
	lr_start_transaction("logout");

	web_custom_request("logout",
		"URL=http://132.232.44.158:5000/userLogout/",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"token\": \"{userToken}\"}", // 引用变量
		LAST);
	
	lr_end_transaction("logout", LR_AUTO);

	lr_end_transaction("user_login_and_logout", LR_AUTO);

	return 0;
}
