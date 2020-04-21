import re

# Generic Match
content1 = 'Hello 123 4567 World_This is a Regex Demo'
result1 = re.match('^Hello.*Demo$', content1)

print('\n\nresult1:')
print(len(content1))
print(result1)
print(result1.group())
print(result1.span())


# Greed
content2 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('He.*(\d+).*Demo$', content2)
print('\n\nresult2:')
print(len(content2))
print(result2)
print(result2.group(1))


# Not Greed
content3 = 'Hello 1234567 World_This is a Regex Demo'
result3 = re.match('He.*?(\d+).*Demo$', content3)
print('\n\nresult3:')
print(len(content3))
print(result3)
print(result3.group(1))


# Not Greed Bad Example
content4 = 'http://weibo.com/comment/TuringGu'
result41 = re.match('http.*?comment/(.*?)', content4)
result42 = re.match('http.*?comment/(.*)', content4)

print('\n\nresult4:')
print('result41:', result41.group(1))
print('result42:', result42.group(1))

