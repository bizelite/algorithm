def palindrome(s):
    s = s.strip(' \'.').lower().replace('\'', '').replace(' ', '').replace(',', '')
    return s == s[::-1]

if __name__ == '__main__':
    print(palindrome('mom'))
    print(palindrome('racecar'))
    print(palindrome('God\'s dog'))
    print(palindrome('Madam, I\'m Adam.'))
