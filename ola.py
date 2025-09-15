import pymysql
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu 
st.title("Ride Insights Application")
with st.sidebar:
    selected = option_menu("Main Menu", ["Home",  "SQL Queries", "Data Visualization"], 
        icons=["house", "list-task", "bar-chart-line"], menu_icon="cast", default_index=0)
    
    if selected == "Home":
        st.title("🏠 Home Page")
    elif selected == "Analytics":
        st.title("📊 Analytics Dashboard")
    elif selected == "SQL Queries":
        
        st.title("🗃️ SQL Queries")
        # Database connection parameters
        host = "localhost"  
        user    = "root"  
        password = "password"       
        database = "zukun"
        # Connect to the database
        try:
            connection = pymysql.connect(host=host, user=user, password=password, database=database)
            st.success("Connected to the database successfully!")
        except Exception as e:
            st.error(f"Error connecting to the database: {e}")
            
            query = "SELECT * FROM ola_ride LIMIT 10;"
        query = st.text_area("Enter your SQL query here:")  
        if st.button("Execute Query"):
            if query.strip() != "":
                try:
                    df = pd.read_sql(query, connection)
                    st.dataframe(df)
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(label="Download data as CSV", data=csv, file_name='query_results.csv', mime='text/csv')
                except Exception as e:
                    st.error(f"Error executing query: {e}")
            else:
                st.warning("Please enter a valid SQL query.")
    elif selected == "Data Visualization":
        st.title("📈 Data Visualization")
        st.write("Data visualization features will be implemented here.")

# Database connection parameters (commented out for security reasons)



        



            #with st.sidebar:
    #st.header("Database Connection Parameters")
    #host = st.text_input("Host", "localhost")
    #user = st.text_input("User", "root")
    #password = st.text_input("Password", "", type="password")
    #database = st.text_input("Database", "ola_db")