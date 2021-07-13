#if문
money=true
if money:
    print("택시를 타고가라")
else:
    print("걸어가라")

pocket=['paper','cellphon','money']
if 'money' in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")

#조건문에서 아무일도 하지 않게 설정하려면?
if 'money' in pocket:
    pass # 실행문 없이 통과
else:
    print("카드를 꺼내라")
