from PIL import Image, ImageChops, ImageDraw

def newImage(pix, widthImg, heightImg):
    newImg=Image.new('L', (widthImg, heightImg))
    draw = ImageDraw.Draw(newImg)
    for i in range(widthImg):
        for j in range(heightImg):
            draw.point((i, j), (pix[j][i]))
    return newImg

def ReLU(x):
    if x>0:
        return x
    else:
        return 0

def convolution(pix, matrix, widthImg, heightImg, sizeMatrix, padding):
    newPix=[[0]*widthImg for i in range(heightImg)]
    for i in range(heightImg):
        for j in range(widthImg):
            s=0
            #перемножение матриц
            for w in range(sizeMatrix):
                for k in range(sizeMatrix):
                    s+=pix[i+w][j+k]*matrix[w][k]
            newPix[i][j]=ReLU(s)
    return newPix           
            

def transformPix(pix, width, height, padding):
    newMatrix=[[0]*(width + 2*padding) for i in range(height + 2*padding)]
    #print(newMatrix)
    for i in range(width):
        #print(i)
        for j in range (height):
            #print(j)
            #print(pix[i,j])
            newMatrix[j + padding][i + padding]=pix[i,j]
    return newMatrix

if __name__=='__main__':
    matrix=((0, 1, 0), (1, -4, 1), (0, 1,  0))
    path=input('Введите путь до изображения\n')
    k=int(input('Введите размерность матрицы(2*k+1)\n'))
    sizeMatrix=2*k+1
    #matrix=[[0]*sizeMatrix for i in range(sizeMatrix)]
    #print('Введите матрицу')
    #for i in range(sizeMatrix):
    #    for j in range(sizeMatrix):
    #        matrix[i][j]=int(input())              
    image=Image.open(path).convert('L')
    image=ImageChops.invert(image)
    padding=int((sizeMatrix-1)/2)#отступ c каждой стороны
    pixels=image.load()
    widthImg=image.size[0]
    heightImg=image.size[1]    
    pixMatrix=transformPix(pixels, widthImg, heightImg, padding)
    newPix=convolution(pixMatrix, matrix, widthImg, heightImg, sizeMatrix, padding)
    image2=newImage(newPix, widthImg, heightImg)
    image2.save('D:/Рабочий стол/результат/rez.png', 'PNG')
    image2.show()
 
