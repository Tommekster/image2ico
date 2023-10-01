# Image2ico

Image to icon converting tool

## Usage

```
usage: image2ico [-o OUTPUT] [-s [{16,24,32,48,64,128,255} ...]] [-h] input

Image to icon converting tool

positional arguments:
  input                 input image file

options:
  -o OUTPUT, --output OUTPUT
                        output ICO filename (default: input_file.ico)
  -s [{16,24,32,48,64,128,255} ...], --sizes [{16,24,32,48,64,128,255} ...]
                        list of icon sizes (ex: --sizes 16 32)
  -h, --help            show this help message and exit
```

## References

[https://stackoverflow.com/questions/45507/is-there-a-python-library-for-generating-ico-files](https://stackoverflow.com/questions/45507/is-there-a-python-library-for-generating-ico-files)

[https://www.codeproject.com/Articles/16178/IconLib-Icons-Unfolded-MultiIcon-and-Windows-Vista](https://www.codeproject.com/Articles/16178/IconLib-Icons-Unfolded-MultiIcon-and-Windows-Vista)

[https://stackoverflow.com/questions/2772452/how-to-associate-application-with-existing-file-types-using-wix-installer](https://stackoverflow.com/questions/2772452/how-to-associate-application-with-existing-file-types-using-wix-installer)
