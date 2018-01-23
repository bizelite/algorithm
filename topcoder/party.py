def nof(first, second):
    dic = {}
    for i in first:
        dic[i] = dic.get(i, 0) + 1
    for j in second:
        dic[j] = dic.get(j, 0) + 1

    return max(dic.values())

if __name__ == '__main__':
    first = ['fishing', 'gardening', 'swimming', 'fishing']
    second = ['hunting', 'fishing', 'fishing', 'biting']

    print(nof(first, second))

    first = ['variety', 'diversity', 'loquacity', 'courtesy']
    second = ['talking', 'speaking', 'discussion', 'meeting']

    print(nof(first, second))
    
    first = ['snakes', 'programming', 'cobra', 'monty']
    second = ['python', 'python', 'anaconda', 'python']

    print(nof(first, second))
    
    first = ['t', 'o', 'p', 'c', 'o', 'd', 'e', 'r', 's', 'i', 'n', 'g', 'l', 'e', \
             'r', 'o', 'u', 'n', 'd', 'm', 'a', 't', 'c', 'h', 'f', 'o', 'u', 'r', 'n', 'i']
    second = ['n', 'e', 'f', 'o', 'u', 'r', 'j', 'a', 'n', 'u', 'a', 'r', 'y', 't', 'w', \
              'e', 'n', 't', 'y', 't', 'w', 'o', 's', 'a', 't', 'u', 'r', 'd', 'a', 'y']

    print(nof(first, second))
    


