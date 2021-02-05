from PIL import Image
import argparse
import sys
#make matrix out of list of pixels
def matrix (pix_list, width):
    for i in range(0, len(pix_list), width):
    	yield pix_list[i:i+width]
#find most frequent thing in a list
def mostFrequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        currentFrequency = List.count(i) 
        if(currentFrequency > counter): 
            counter = currentFrequency 
            num = i 
  
    return num 
#argument declaration
def arguments ():
    parser = argparse.ArgumentParser(description='Process an image')
    parser.add_argument( action ="store", dest="image", type = str, )
    user_args = vars(parser.parse_args(sys.argv[1:]))
    return user_args
#checks color if its in a predetermined amount and returns closest color to one provided if not in 
#predetermined colors.
def colorChecker(colors):
        colorsArray = []
        for i in range(6):
                for j in range(6):
                        for k in range(6):
                             colorsArray.append([i*51,j*51,k*51]) 
        colorWeights = []
        for i in colorsArray:
            colorVal = abs(colors[0] - i[0])
            colorVal = colorVal + abs(colors[1] - i[1])
            colorVal = colorVal + abs(colors[2] - i[2])
            colorWeights.append(colorVal)
        return colorsArray[colorWeights.index(min(colorWeights))]    

def normalize(pixels):
    normalizedPix = []    
    for i in pixels: 
        normalizedPix.append(colorChecker(i))
    return normalizedPix

def pixelArt (pixels: list, width, height, pixelSize):
        artWidth = width // pixelSize
        artHeight = height // pixelSize
        flatColorList = []
        pixels_matrix =list(matrix(pixels, width))
        pixels_result =list(matrix(pixels, width))
        print(artHeight)
        print(height)
        print(width)
        print(len(pixels_matrix[0]))

        for i in range(artWidth):
            for j in range(artHeight):
                colorList = []
                for ii in range(pixelSize):
                    for jj in range(pixelSize):
                        colorList.append(pixels_matrix[j*pixelSize+jj][i*pixelSize+ii])
                flatColorList.append(mostFrequent(colorList))
        blockCounter = 0
        for k in range(artWidth):
            for L in range(artHeight):
                for kk in range(pixelSize):
                    for LL in range(pixelSize):
                        pixels_result[L*pixelSize+LL][k*pixelSize+kk] = flatColorList[blockCounter]
                blockCounter = blockCounter + 1

        returnList = []
        for i in pixels_result:
            for j in i:
                returnList.append(j)
        return returnList
                



def main (args: list):
    if args["image"] != None:
        file = args["image"]
        img = Image.open(file)
        width, height = img.size
        pixels = list(map(list, img.getdata()))
        print("started normalizing")
        pixels = normalize(pixels)
        print("started pixelArting")
        pixels = pixelArt(pixels, width, height, 7)
        img.putdata(list(map(tuple, pixels)))
        print("about to save")
        img.save("new_image.bmp")



a = arguments()
main(a)