vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'


ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
