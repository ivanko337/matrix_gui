from PIL import Image, ImageDraw, ImageFont
from MyMatrix import Matrix
from Cramer import Cramer

def matrix(a, b):
	r = Cramer(a, b)
	return r.getResult()
def getMatrixText():
	matrix = Matrix([ [5, 1, 2], [4, 3, 6], [12, 23, 18] ])
	s = [ [ str(matrix[i][j]) for j in range(len(matrix[i])) ] for i in range(len(matrix)) ]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	return ('\n'.join(table)).expandtabs()

img = Image.new('RGB', (100, 100), color = (73, 109, 137))

fnt = ImageFont.truetype('/ARIAL.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), getMatrixText(), font=fnt, fill=(255, 255, 0))

img.save('pil_text_font.png')
