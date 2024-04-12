
print('1.使用for循环输出1+2+3+…+100的结果')

sum = 0 #for循环

for i in range(1,101):#1~100
  sum+=i

print('The sum is :{}  .'.format(sum))

print('2.使用 while 循环输出 100 以内的偶数。')

j=1

while(j!=100):

  if(j%2==0):

    print(j)

  j = j+1


print('3.使用for循环或 while循环输出100以内的素数')

for num in range(2,101):

    flag = True #作为判断标志

    for i in range(2,num):

      if(num%i==0): #一旦出现可以除掉非1、非自身的数，则立即判断为假

        flag = False  

        break

    if(flag):

      print(num)
