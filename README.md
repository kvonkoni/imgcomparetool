# ImgCompareTool

ImgCompareTool is a Python (3.x) package for comparing the similarity of pairs of images.

## Installation

ImgCompareTool can be used in two ways: as a Python (3.x) module to use in your own script or, alternatively, as a portable application with a graphical user interface (available as portable applications for Windows and MacOS in addition to a Python script).

#### Portable application

###### Windows 10

Download the current release of ImgCompareTool-win10.exe to your desired location and run the application.

###### Mac OS 10.15

Download and extract ImgCompareTool-macos-10.15.zip to your desired location. Run the ImgCompareTool file in the extracted directory.

###### Mac OS 10.14

Due to a known bug in OS 10.14 (Mojave) that causes Tkinter-based applications compiled using PyInstaller to crash the system, ImgCompareTool must be run using a Python (3.x) interpreter when using this operating system.

To run the graphical application on OS 10.14, use the following steps:

```bash
>> python setup.py install
>> python ui.py
```

#### Python package (platform-independent)

To install the Python module, simply clone the repository to any location and run

```bash
>> python setup.py install
```

from the repository's root directory.

To use the ImgCompileTool GUI from your Python (3.x) interpreter, simple copy the ui.py file from the repository to a location of your choice and run

```bash
>> python ui.py
```

Since this package uses PySimpleGUI, the graphical interface run from the interpreter in this way will work on Windows, MacOS, and Linux.

## Usage

The tool compared 

#### Portable application



#### Python package

The package can be used as part of a Python script using the ImageList class.

## Build and Release

#### Portable application

###### Windows 10

To compile new versions of the portable applications on Windows, run

```bash
>> pyinstaller --onefile --add-data <Path to Python>\Lib\site-packages\imagehash;imagehash --clean --noconsole --noconfirm --name ImgCompareTool ui.py
```
from the root of the repository. This will create a single .exe file that can be run by the end-user on Windows.

Due to a bug in the imagehash package, you must force PyInstaller to include the package directory. Replace "<Path to Python>\Lib\site-packages\imagehash" with the path to imagehash package on your environment.

###### Mac OS 10.15

To compile new versions of the portable application on MacOS (10.15 or later), run

```bash
>> pyinstaller --add-data /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/imagehash:imagehash --add-data /Library/Frameworks/Python.framework/Versions/3.8/lib/tcl8.6:tcl --add-data /Library/Frameworks/Python.framework/Versions/3.8/lib/tk8.6:tk --clean --noconsole --noconfirm --name ImgCompareTool ui.py
```
from the root of the repository.

Due to a bug in the PyInstaller for MacOS, you must force PyInstaller to include the imagehash, Tk, and Tcl package directories. Tk and Tcl are required for the GUI application Tkinter, which is a dependency of PySimpleGUI. Replace the above paths to these directories with the appropriate ones from your environment.

Compress the ImgCompareTool directory and distribute this to users. The tool cannot be run from the .app file since the software is not signed.

###### Mac OS 10.14

Due to the bug mentioned in [Installation and Use](Mac OS 10.14), the application must be run through a Python interpreter for this operating system. Therefore, there is no need to build and release a portable application.

#### Python package (platform-independent)

Version information for the package is stored in the setup.py file in the root of the repository. Make sure to update the version parameter during releases.

```python
setup(  name='imgcomparetool',
        version='0.1',
        ...
     )
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

The ImgCompareTool package includes a unit test script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](LICENSE)