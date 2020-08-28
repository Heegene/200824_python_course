# Open API
# ① http://developers.naver.com 싸이트 이동
# ② Naver API 사용 위해 Application 등록 수행
# ③ 사용 API에서 검색 서비스 선택(get / post 방식)
# ④ 파이썬 검색어로 검색하여 결과 JSON 확인

# 과제 : 1) 응답에 대한 JSON parsing ->ITEM 항목을 100개 가져옴
#        2) tbl_API에 모두 저장(단 regdate는 system의 현재일자 적용하기)

import requests
import cx_Oracle
import pprint


headers = {
    'X-Naver-Client-Id' : 'j513HictYVPoWEl27Yor',
    'X-Naver-Client-Secret' : '' ,
}

payLoad = {
    'query' : '파이썬',
    'display' : 100,
 }
url = 'https://openapi.naver.com/v1/search/blog' # json 결과

res = requests.get(url,  headers=headers , params=payLoad)

print('request sended...')
# 응답이 json 형태로 오기로 되어 있음
print(res.json())
# 응답에 대한 parsing -> pprint : 모양이 좀더 좋음  pprint(res.json())

# 응답에 대한 JSON parsing ->ITEM 항목을 100개 가져옴
itemCnt = len(res.json()['items'])
print('itemCnt -> %d' %itemCnt)


if itemCnt > 0:
    # 1.Oracle Session Open
    dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
    con = cx_Oracle.connect("scott", "tiger", dsn)
    cursor = con.cursor()

    # 2.i=0~itemCnt까지 최대 99번 loop가 돌아감
    for i in range(itemCnt):  #
        result = res.json()['items'][i]['title']
        print('%d번째 Title -> %s' % (i,result))
        # cursor.execute("INSERT INTO  tbl_API(num , title ) values (:v_num , :v_title ) ", v_num=i, v_title=result)
        try:
            cursor.execute("INSERT INTO  tbl_API(num , title , regdate ) values (:v_num , :v_title , sysdate ) ",
                           v_num=i, v_title=result)
        except :
            print("Oracle {}번째 {}입력오류" .format(i ,result ))
        # cursor.execute("INSERT INTO tbl_API(num , title )  VALUES(?, ?); ", (i, result))  -> 안됨 , sqlite에서만 됨
    # 3.저장 중요
    con.commit()
    con.close()

    print('tbl_API %d건  저장 완료 되었습니다 '%itemCnt)
else:
    print('해당구문에 해당하는 조회된 건수가 없습니다')