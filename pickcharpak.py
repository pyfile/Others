import cv2

name1 = input('请输入立绘主图文件名：')
charpak = cv2.imread('%s.png' % name1)
charpakalpha = cv2.imread('%s' % name1+'[alpha]'+'.png', cv2.IMREAD_GRAYSCALE)
#charpakalpha = cv2.resize(charpakalpha, None, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
b,g,r = cv2.split(charpak)
img_bgra = cv2.merge((b,g,r,charpakalpha))
cv2.imwrite('C:\A_MyData\Beautiful_Pictures\Arknights\%s.png' % name1, img_bgra)
