#! /usr/bin/bash

streamlit run /app/"${MAIN_APP_FILE}" --server.enableXsrfProtection=false --server.port 8501
