height=float(input("請輸入身高 (公尺) : "))
weight=float(input("請輸入體重 (公斤) : "))
bmi=weight/height**2
print("BMI =",bmi)
# if 24<=bmi<27:
#     print("過重")
# elif 27<=bmi<27:
#     print("輕度肥胖")
# elif 30<=bmi<35:
#     print("中度肥胖")
# elif bmi>=35:
#     print("重度肥胖")
# elif bmi<18.5:
#     print("體重過輕")
# else:
#     print("正常")