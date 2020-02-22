#2、单利公式
def danli():
     p=input("请输入本金P：")
     t=input("请输入时间T:")
     r=input("请输入利率r:")
     c=float((float(p)*float(t)*float(r))/100)
     print("单利是: %d" %(c))
danli()