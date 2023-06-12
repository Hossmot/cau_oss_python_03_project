#클래스
class parking_spot:

    #6개의 데이터를 저장할 수 있는 딕셔너리 객체, 생성자를 통해 생성/설정
    def __init__(self, name, city, district, ptype, longtitude, latitude):
        self.__item = {
            'name' : name,
            'city' : city,
            'district' : district,
            'ptype' : ptype,
            'longitude' : longtitude,
            'latitude' : latitude 
        }

    #get 메소드, 객체의 __item[keyword]값(value)을 반환한다. 기본인수는 'name'이다.
    def get(self, keyword='name'):
        return self.__item[keyword]
    
    def __str__(self):                                            #객체의 출력형태를 설정
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
#함수 
def str_list_to_class_list(str_list):        
    ReTurnList = []
    for ParkingSpotInfo in str_list:             #읽어온 str_list를 for로 문자열로 쪼개 반복한다
        element = ParkingSpotInfo.split(',')     #for문에서 넘겨준 문자열을 쉼표를 기준으로 단일 리스트로 쪼갠다
        ReTurnList.append(parking_spot(element[1], element[2], element[3], element[4], element[5], element[6])) #넘겨받은 리스트의 각 요소로 객체 생성
    return ReTurnList #parking_spot 클래스 객체의 리스트 반환
    
    
def print_spots(spots):                          #객체의 리스트를 받아 모든 객체의 값을 출력
    print(f'---print elements({len(spots)})---') #객체의 개수 출력
    for Obj in spots:
        print(Obj)
# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")

    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")

    # for s in str_list:
    #     print(s)      #파일 리딩 확인, 출력

    # for i in str_list_to_class_list(str_list):    #str_list_to_class_list 작동확인
    #     print(i)

    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)