import re

# Test1
content1 = 'Hello 123 4567 World_This is a Regex Demo'
result1 = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content1)

print('\n\nresult1:')
print(len(content1))
print(result1)
print(result1.group)
print(result1.span())


# Test2
content2 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^Hello\s(\d+)\sWorld', content2)

print('\n\nresult2:')
print(len(content2))
print(result2)
print(result2.group())
print(result2.group(1))
print(result2.span())





