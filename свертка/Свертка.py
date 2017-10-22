from PIL import Image, ImageChops, ImageDraw

def newImage(pix, widthImg, heightImg):
    newImg=Image.new('L', (widthImg, heightImg))
    draw = ImageDraw.Draw(newImg)
    for i in range(widthImg):
        for j in range(heightImg):
            draw.point((i, j), (pix[i][j]))
    return newImg

def ReLU(x):
    if x>0:
        return x
    else:
        return 0

def convolution(pix, matrix, widthImg, heightImg, sizeMatrix, padding):
    newPix=[[0]*widthImg for i in range(heightImg)]
    for i in range(widthImg):
        for j in range(heightImg):
            s=0
            #перемножение матриц
            for w in range(sizeMatrix):
                for k in range(sizeMatrix):
                    s+=pix[i+w][j+k]*matrix[w][k]
            newPix[i][j]=ReLU(s)
    return newPix           
            

def transformPix(pix, width, height, padding):
    newMatrix=[[0]*(width + 2*padding) for i in range(height + 2*padding)]
    for i in range(height):
        for j in range (width):
            newMatrix[i+padding][j+padding]=pix[i, j]
    return newMatrix

if __name__=='__main__':
    matrix=((0, 1, 0), (1, -4, 1), (0, 1,  0))
    path=input()
    k=int(input())
    image=Image.open(path).convert('L')
    image=ImageChops.invert(image)
    sizeMatrix=2*k+1
    padding=int((sizeMatrix-1)/2)#отступ c каждой стороны
    pixels=image.load()
    widthImg=image.size[0]
    heightImg=image.size[1]    
    pixMatrix=transformPix(pixels, widthImg, heightImg, padding)
    newPix=convolution(pixMatrix, matrix, widthImg, heightImg, sizeMatrix, padding)
    image2=newImage(newPix, widthImg, heightImg)
    image2.save('D:/Рабочий стол/результат/rez.png', 'PNG')
    image2.show()
 
