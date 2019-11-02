# ImgCompareTool

ImgCompareTool is a Python package for creating comparing pairs of images.

## Installation

ImgCompareTool can be used in two ways: as a Python module to use in your own script or as a portable application with a simple GUI.

To install the Python module, simply clone the repository and run

```bash
python setup.py install
```

from the repository's root directory.

To use the tool as a portable application, download and run the appropriate app for your operating system from the root directory. The ImgCompareTool application is available for both Windows and MacOS.

## Usage



## Image Similarity

In broad strokes, two pictures are similar when they have the same colours in the same places. This can sometimes be complicated if a photo has undergone a transformation (e.g. rotated, cropped, brightened/darkened).

The measure of similarity should be sensitive to:

·     Colour properties (hue, tint/shade, etc.)

·     Colour location

On the other hand, the measure should be less sensitive to:

·     Image format (jpg, png, bmp, etc.)

·     Aspect ratio/cropping

·     Resolution

·     Rotation

## Testing



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](LICENSE)