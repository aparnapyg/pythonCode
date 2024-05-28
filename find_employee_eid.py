import re
def find_eid(report):
  pattern = "Employees\s?([A-Z]?-\d+)\s?and\s?([A-Z]?-\d+)" #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result


print(find_eid("Employees B-1234567 and C-12345678 worked with products X-123456 and Z-123456789")) # Should return ['B-1234567', 'C-1234567']
print(find_eid("Employees B-1234567 and C-12345678, not employees b-1234567 and c-12345678")) #Should return ['B-1234567', 'C-1234567']