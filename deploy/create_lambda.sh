#!/bin/bash
fileDir=$(realpath ${0%/*})
projDir=$(dirname $fileDir)
projName=$(basename $projDir)
lambdaName="${projName}_lambda"
roleName="${lambdaName}_role"

aws iam create-role \
    --role-name $roleName \
    --assume-role-policy-document "file://$fileDir/policies/trust_policy.json"
aws iam put-role-policy \
    --role-name $roleName \
    --policy-document "file://$fileDir/policies/role_policy.json" \
    --policy-name "${lambdaName}_policy"

mkdir tmpPackage
python3 -m pip install -r "$projDir/requirements.txt" --target tmpPackage
python3 -m pip install $projDir --target tmpPackage

cd tmpPackage
zip -r "../$lambdaName.zip" .
cd ..
rm -rf tmpPackage

aws lambda create-function \
    --function-name $lambdaName \
    --runtime python3.12 \
    --zip-file fileb://$lambdaName.zip \
    --handler $projName.lambda_function.lambda_handler \
    --role arn:aws:iam::176924676374:role/$roleName \
    --timeout 30 \
    --environment 'Variables={SNS_TOPIC_ARN=arn:aws:sns:us-east-1:176924676374:item-availability-updates}'
    
rm "./$lambdaName.zip"