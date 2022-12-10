print('반복횟수를 입력하세요 :')
dow = int(input())

if dow == 0:
      print('0보다 작거나 같은 수는 입력할수 없습니다')
elif dow == dow < 0:
      print('0보다 작거나 같은 수는 입력할수 없습니다')
else:
      for i in range(1, dow+1, 1):
            for j in range(i):
                  print( "*", end = "" )
            print()
            
      
