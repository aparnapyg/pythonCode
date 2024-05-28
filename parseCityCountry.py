import re
def parse_city_country(text):
  pattern = '([a-zA-Z\s^!]+)' #enter the regex pattern here
  result = re.findall(pattern, text) #enter the re method  here
  if len(result) != 2:
    return ""
  return result[0]#return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank
