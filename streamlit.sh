#!/bin/bash
playwright install chromium
streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
