for num in range(2, 101):
    for i in range(2,num):
        if not num % i:
          break
    else :
        print(num)
      

