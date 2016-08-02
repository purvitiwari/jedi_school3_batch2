if [ $# -eq 0 ]
  then
    echo "Usage: bash findnum -n <mobile_number_with_national_code>"
    echo "Example: bash findnum -n +919816650201"
    exit 1
fi

if [ $1 == "-h" ] 
    then
        echo "Usage: bash findnum -n <mobile_number_with_national_code>"
		echo "Example: bash findnum -n +919816650201"
	exit 1
fi

if [ $# -eq 1 ] 
    then
    echo "Usage: bash findnum -n <mobile_number_with_national_code>"
		echo "Example: bash findnum -n +919816650201"
	exit 1
fi


if [ $# -eq 2 ]
  then
    echo "Checking number for $2"
fi

urll='http://apilayer.net/api/validate?access_key=5897967950821a17fbff92b7cc531bb9&number='$2'&format=1'
curl $urll |     sed -e 's/[{}]/''/g'| awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}'
