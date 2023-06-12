import file_manager          #파일 작업을 위한 모듈
import parking_spot_manager  #파일에서 불러온 데이터 작업을 위한 모듈
def start_process(path):
    StrList = file_manager.read_file(path)                         
    ObjList = parking_spot_manager.str_list_to_class_list(StrList)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(ObjList)           #1번동작, 객체 출력
        elif select == 2:                                       #2번동작, 필터 메뉴 선택
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:       
                keyword = input('type name:')
                ObjList = parking_spot_manager.filter_by_name(ObjList, keyword)  #name 필터
            elif select == 2:
                keyword = input('type city:')
                ObjList = parking_spot_manager.filter_by_city(ObjList, keyword)  #city 필터
            elif select == 3:
                keyword = input('type district:')
                ObjList = parking_spot_manager.filter_by_district(ObjList, keyword)  #district 필터
            elif select == 4:
                keyword = input('type ptype:')
                ObjList = parking_spot_manager.filter_by_ptype(ObjList, keyword)      #ptype 필터
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_long = float(input('type min long:'))
                max_long= float(input('type max long:'))
                locations = (min_lat, max_lat, min_long, max_long)
                ObjList = parking_spot_manager.filter_by_location(ObjList, locations)  #location 필터
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")