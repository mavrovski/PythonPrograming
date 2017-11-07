width = float(input())
height = float(input())
widthCounts = int((width*100)/120)
heightCounts = int((height*100-100)/70)
result = widthCounts*heightCounts-3
print(result)