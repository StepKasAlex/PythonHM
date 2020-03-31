seconds = int(input())
hours = (seconds // 3600) % 24
minutes1 = seconds // 60 % 60 // 10
minutes2 = seconds // 60 % 60 % 10
sec1 = seconds % 60 // 10
sec2 = seconds % 10
print(hours, ':', minutes1, minutes2, ':', sec1, sec2, sep='')
