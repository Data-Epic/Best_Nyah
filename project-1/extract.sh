#!/bin/bash -e

# input data check
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 : <year> <month>"
    exit 1
fi

year="$1"
month="$2"


# ny taxi url
data_url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_$year-0$month.parquet"

# save directory path
download_dir="./data"

# create download dir if not exist
mkdir -p "$download_dir"

echo "Downloading..."

# download file with wget
output_file="$download_dir/ny_taxi_data_$year_$month.parquet" 

wget -c -O "$output_file" "$data_url"

# Print a success message
echo "$output_file"
