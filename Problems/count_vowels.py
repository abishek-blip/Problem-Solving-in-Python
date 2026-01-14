s = "abishek"
count = 0
for i in range(len(s)):
    if(s[i] in "aeiouAEIOU"):
        count += 1

print(count)