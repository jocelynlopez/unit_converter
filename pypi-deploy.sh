#!/bin/bash

echo "[distutils]" > ~/.pypirc
echo "index-servers =" >> ~/.pypirc
echo "    pypi" >> ~/.pypirc
echo " " >> ~/.pypirc
echo "[pypi]" >> ~/.pypirc
echo "username:"${PYPI_USER} >> ~/.pypirc
echo "password:"${PYPI_PASSWORD} >> ~/.pypirc

chmod 600 .pypirc

version=$(python3 -c "from ${REPONAME} import __version__;print(__version__)")
curl -f -s -S -k -X GET -I https://pypi.python.org/packages/source/d/${REPONAME}/${REPONAME}-$version.tar.gz

if [[ $? -eq 0 ]]
then
    echo "Current package version is already at PyPi. If your intention was to"
    echo "release a new version, you'll have to increase the version number."
else
    echo "Uploading $version version to PyPi"
    python setup.py sdist upload
fi

exit 0

