
def decimal_expansion(a,b):
     rest_list = [False]*b#create list filled with False statement with length equal to number of b remainders
     rest = a%b#we start with this because a//b is an integer part of the number e.g. 1/7 = 0, rest 1 then 1*10 = 10 then 10/7= 1 rest= 3 res +=1
     result = ''
     while rest !=0 and rest not in rest_list:#or while rest !=0 and rest_list[rest] == False:
         rest_list[rest] = rest
         rest *= 10
         result += str(rest//b)
         rest = rest % b
     if rest == 0:
          return a/b
     else:
          return f'{a//b}.({result})'

if __name__ == '__main__':
    print(decimal_expansion(1,7))


