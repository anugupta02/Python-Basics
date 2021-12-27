

import wikipedia as wp

result = wp.search("Python")
print(result)
wp.set_lang("hindi")
print("Hello World")
wp.set_lang("hindi")

result = wp.page("Python")
print(result.title)
print(result.content)



