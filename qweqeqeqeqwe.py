#2자리 숫자를 입력받아 앞자리와 뒷자리 값을 더하세요.
number=input("2자리 숫자를 입력하세요")
print(type(number))

#입력값이 2자리인지확인
if len(number)  != 2:
    print("2자리 숫자를 입력하세요.")
else:
    # 각 자리의 숫자를 추출하여 정수로 변환하여 더하기

    first_num=int(number[0])
    second_num = int (number[1])
 print("앞자리와 뒷자리의 합:", result)