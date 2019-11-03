# ImgCompareTool

ImgCompareTool is a Python package for creating comparing pairs of images.

## Installation

ImgCompareTool can be used in two ways: as a Python module to use in your own script or as a portable application with a simple GUI.

To install the Python module, simply clone the repository and run

```bash
>> python setup.py install
```

from the repository's root directory.

To use the tool as a portable application, download and run the appropriate app for your operating system from the root directory. The ImgCompareTool application is available for both Windows and MacOS.

## Usage



## Build

To compile new versions of the portable applications on Windows, run

```bash
>> pyinstaller --onefile --add-data <Path to Python>\Lib\site-packages\imagehash;imagehash --clean --noconsole --noconfirm --name ImgCompareTool ui.py
```
from the root of the repository. This will create a single .exe file that can be run by the end-user on Windows.

Due to a bug in the imagehash package, you must force PyInstaller to include the directory. Replace "<Path to Python>\Lib\site-packages\imagehash" with the path to imagehash package on your environment.

To compile new versions of the portable application on MacOS (10.15 or later), run

```bash
>> pyinstaller --add-data /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/imagehash:imagehash --add-data /Library/Frameworks/Python.framework/Versions/3.8/lib/tcl8.6:tcl --add-data /Library/Frameworks/Python.framework/Versions/3.8/lib/tk8.6:tk --clean --noconsole --noconfirm --name ImgCompareTool ui.py
```
from the root of the repository.

Due to a bug in the PyInstaller for MacOS, you must force PyInstaller to include the imagehash, Tk, and Tcl directories. Tk and Tcl are required for the UI library Tkinter. Replace the above paths with the appropriate ones for your environment with the path to imagehash package on your environment.

Due to a bug in MacOS 10.14 (Mjoave), the application that was compiled through PyInstaller will cause the system to crash. Updating to MacOS 10.15 (Catalina) will resolve this issue.

For MacOS 10.14, the application must be run through a Python3 interpreter. To run the graphical application on OS 10.14, use the following steps:
```bash
>> python setup.py install
>> python ui.py
```

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