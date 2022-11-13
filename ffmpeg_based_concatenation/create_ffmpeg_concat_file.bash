#!/bin/bash
rm -rf VideoFileList.txt
for f in *.mov; do echo "file '$f'" >> VideoFileList.txt; done
