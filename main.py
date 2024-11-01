# main.py
import streamlit as st
from employees import employees_interface
from customers import customers_interface
from payments import payments_interface


# Selección de la tabla
option = st.sidebar.selectbox("Selecciona una tabla", ["Empleados", "Clientes", "Vehículos", "Ventas", "Pagos", "Reparaciones"])

if option == "Empleados":
    employees_interface()
elif option == "Clientes":
    customers_interface()
elif option == "Pagos":
    payments_interface()
