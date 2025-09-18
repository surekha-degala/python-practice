
def count_articles(s):
    s = s.lower() 
  words = s.split(" ")
  count = 0
    for word in words:
       if word == "a" or word == "an" or word == "the" or word == "a," or word == "an," or word == "the.":
            count+=1
          return count
s = input()
print(count_articles(s))
    
