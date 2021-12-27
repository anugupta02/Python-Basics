#import re
#a = "sd3s5d1f32sdf54s3f1sd3f4s65d4f3s1324sd68f"
#print(dir(re))
#print(help(re))
#b = re.findall('\d', a)
#b = re.findall('\d+', a)  #if we want faster sorting process
#b = re.findall('\D+', a)
#b = re.findall('[a-f]+', a)
#print(b)

import re
a = "sd3s5dabcdbdbDACBD1f32sd\tf54s3f1sd3f4s65d4f3s1324sd68f"
b = re.findall('[a-f]+',a,re.IGNORECASE)
print(b)

#match selfstudy