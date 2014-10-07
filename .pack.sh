#!/bin/sh
echo "current branch:"
git rev-parse --abbrev-ref HEAD
# make sure
echo -n "version: "
read version

package="traversing_v$version"
tagname="master-$version"
temp_dir=/var/tmp/$package

proj_dir=~/traversing

[[ ! -d $proj_dir ]]&&proj_dir=~/develop/traversing
echo -n "package: $package.tar.gz (Y/n):"
read confirm
if [ "$confirm" != "Y" ];then
    echo "abandoned pack"
    exit 0
fi

# copy to temp directory
if [ -d $temp_dir ];then
    rm -rf $temp_dir
fi
echo "mkdir $temp_dir"
mkdir $temp_dir

for dir in gfirefly gtwisted shared app appmain.py config.json models.json mgc.config template.json startmaster.py; do
    echo "cp -rf $dir $temp_dir"
    cp $dir -rf $temp_dir
done

cd $temp_dir
echo "compile *.py to *.pyc"
find -name '*.py' -exec python -m py_compile {} \;
cp startmaster.py ..
cp appmain.py ..
echo "clear useless files"
find ./ -name '.*' -exec rm -rf {} \;
find ./ -name '~*' -exec rm -rf {} \;
find ./ -name '*.log' -exec rm -rf {} \;
find ./ -name '*.py' -exec rm -rf {} \;
find ./ -name '*.zip' -exec rm -rf {} \;
find ./ -name '*.xls' -exec rm -rf {} \;

mv ../startmaster.py .
mv ../appmain.py .

rm startmaster.pyc
rm appmain.pyc

cd ../
echo "tar -czf $package.tar.gz $package"
tar -czf $package.tar.gz $package
rm -rf $package
mv $package.tar.gz /share/

cd /share
echo "md5 $package.tar.gz"
./md5.sh $package.tar.gz > $package.md5

echo "pack $package success"

echo -n "tag: $tagname (Y/n):"
read confirm
if [ "$confirm" != "Y" ];then
    echo "abandoned tag"
    exit 0
fi

cd $proj_dir
git tag $tagname
git push --tags

echo "tag $tagname success"
exit 0