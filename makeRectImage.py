from PIL import Image

import click

def makeRectImage(size, color, oName):
    img = Image.new("RGBA", size, color)
    img.save(oName)

def convertColor(color):
    colorSplit = (color[i*2:(i+1)*2] for i in xrange(4))
    return tuple(int(c, 16) if c else 255 for c in colorSplit)

@click.command()
@click.argument('width', type=int)
@click.argument('height', type=int)
@click.option('--color', default='ffffff')
@click.option('--name', default='image.png')
def makeRectImageWrapper(width, height, color, name):
    makeRectImage([width, height], convertColor(color), name)

if __name__ == '__main__':
    makeRectImageWrapper()
