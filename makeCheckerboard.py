from PIL import Image
import random

import click

def makeCheckerboard(imgSize, images):    
    images = [Image.open(image) for image in images]
    tileSize = images[0].size
    size = [imgSize[i] / tileSz for i, tileSz in enumerate(tileSize)]
    fullImage = Image.new("RGBA", imgSize)
    
    board = [[None] * size[0] for i in xrange(size[1])]
    
    for i in xrange(size[0]):
        for j in xrange(size[1]):
            adjImages = []
            for xdiff in xrange(-1, 2):
                for ydiff in xrange(-1, 2):
                    if (xdiff + ydiff) % 2 == 0:
                        continue
                    x = i + xdiff
                    y = j + ydiff
                    if x >= 0 and y >= 0 and x < size[0] and y < size[1] and board[y][x]:
                        adjImages.append(board[y][x])
            
            possibleImages = [img for img in images if img not in adjImages]            
            img = random.choice(possibleImages if possibleImages else images)
            board[j][i] = img
            fullImage.paste(img, (i * tileSize[0], j * tileSize[1]))

    fullImage.save('checkerboard.png')    

@click.command()
@click.argument('width', type=int)
@click.argument('height', type=int)
@click.argument('images', nargs=-1)
def makeCheckerboardWrapper(width, height, images):
    makeCheckerboard([width, height], images)

if __name__ == '__main__':
    makeCheckerboardWrapper()
