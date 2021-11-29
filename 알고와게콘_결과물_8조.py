print("기온별 옷차림을 추천해드리겠습니다!")

tem=int(input("오늘의 온도를 입력하세요. : "))

aa=input("상의 또는 하의 중 하나를 입력하세요.: ")
if aa=="상의":
    if tem >= 27:
        print("민소매티, 반팔을 추천합니다.")
    elif 27 > tem >= 22:
        print("반팔, 얇은 셔츠를 추천합니다.")
    elif 22 > tem >= 16:
        print("니트, 가디건, 후드티를 추천합니다.")
    elif 16 > tem >= 11:
        print("자켓, 셔츠, 가디건, 간절기용 야상을 추천합니다.")
    elif 11 > tem >=5:
        print("코트, 가죽자켓을 추천합니다.")
    else:
        print("패딩, 코트를 추천합니다.")

else:
    if tem >= 27:
        print("반바지를 추천합니다.")
    elif 27 > tem >= 22:
        print("면바지, 슬랙스를 추천합니다.")
    elif 22 > tem >= 16:
        print("청바지를 추천합니다.")
    elif 16 > tem >= 11:
        print("스타킹, 간절기용 면바지를 추천합니다.")
    elif 11 > tem >= 5:
        print("솜바지, 기모스타킹을 추천합니다.")
    else:
        print("패딩바지, 기모가 들어간 바지를 추천합니다.")

print("즐거운 하루 되세요!")
