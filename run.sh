#!/bin/bash

# You can also pass a URL to streamlit run! This is great when combined with Github Gists. For example:
# $ streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

PythonScript=$1

if [ -z ${PythonScript} ];then
    echo "<usage> ./run.sh {Your Main Python Script}"
    exit 1
fi

echo "streamlit run ${PythonScript}"
streamlit run ${PythonScript}