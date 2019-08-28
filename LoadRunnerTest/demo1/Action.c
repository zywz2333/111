Action()
{

    // get·½·¨
	web_custom_request("web_custom_request",
		"URL=http://132.232.44.158:8080/morning/getAllGoods",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body=",
		LAST);


	// post form-data
	web_submit_data("login",
		"Action=http://132.232.44.158:8080/morning/user/userLogin",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=user.loginName", "Value=2941635995@qq.com", ENDITEM,
		"Name=user.loginPassword", "Value=a123456", ENDITEM,
		LAST);


	// post json
	web_custom_request("LUXLOGIN",
		"URL=http://132.232.44.158:5000/userLogin/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"username\":\"test\", \"password\":\"123456\", \"captcha\":\"123456\"}",
		LAST);


	return 0;
}
