pytest -v test_main_page.py                #Обычный запуск тестов

pytest name_tests --alluredir=./my_allure_results     #"Генерация отчета + запукс тестов"
allure serve ./my_allure_results           #"Просмотр"