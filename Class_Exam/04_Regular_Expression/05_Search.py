import re

# Test 1
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra string'
# result = re.match('Hello.*?(\d+).*?Demo', content)
result1 = re.search('Hello.*?(\d+).*?Demo', content)

print('\n\nresult1:')
print(result1)


# Test 2
html = '''
<div id="song-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>
'''

result2 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print('\n\nresult2:')
if result2:
    print(result2.group(1), result2.group(2))
