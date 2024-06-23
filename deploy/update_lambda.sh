fileDir=$(realpath ${0%/*})
projDir=$(dirname $fileDir)
projName=$(basename $projDir)
lambdaName="${projName}_lambda"

mkdir tmpPackage
python3 -m pip install -r "$projDir/requirements.txt" --target tmpPackage
python3 -m pip install $projDir --target tmpPackage

cd tmpPackage
zip -r "../$lambdaName.zip" .
cd ..
rm -rf tmpPackage

aws lambda update-function-code \
    --function-name $lambdaName \
    --zip-file fileb://$lambdaName.zip
    
rm "./$lambdaName.zip"