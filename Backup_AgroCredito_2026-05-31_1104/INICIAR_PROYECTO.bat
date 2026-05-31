@echo off
echo ============================================
echo   AgroCrédito Colombia - Seguridad Alimentaria
echo   Proyecto Final - Andrés, Sebastián, Julián, Yuri
echo   Talento Tech 2
echo ============================================
echo.
echo Iniciando servidor Streamlit en puerto 8520...
echo Abre http://localhost:8520 en tu navegador
echo.
python3 -m streamlit run app.py --server.port 8520 --server.headless true --server.address 0.0.0.0
pause
