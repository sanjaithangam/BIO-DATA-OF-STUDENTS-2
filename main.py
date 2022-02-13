import streamlit as st
import pandas as pd
import csv

st.set_page_config(page_title = "BIO-DATA OF STUDENTS", page_icon=":smile:")

title = st.container()
Create = st.container()
Update = st.container()
Read = st.container()
Delete = st.container()

file_location = 'Students.csv'

with title:
    st.header("BIO-DATA OF STUDENTS")
    st.write("HERE YOU CAN INFORMATION ABOUT A STUDENT!")

df = pd.read_csv(file_location)

rows = 0
for row in df.iterrows():
    rows = rows + 1

with Create:
    rows = rows + 2
    st.header("CREATE AN ID!")
    name = st.text_input("NAME: ").strip().upper()
    admission_no = st.text_input("ADMISSION NO: ").strip().upper()
    clas = st.text_input("CLASS: ").strip().upper()
    section = st.text_input("SECTION: ").strip().upper()
    roll_no = st.text_input("ROLL NO: ").strip().upper()
    if name != "" and admission_no != "" and clas != "" and section != "" and roll_no != "":
        if name not in list(df["NAME"]):
            with open(file_location, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([name, admission_no, clas, section, roll_no])
        else:
            st.write("THE NAME IS ALREADY TAKEN!")
    else:
        st.write("FILL THE CREDENTIALS!")
    form = st.form("my_form")
    submit = form.form_submit_button("SUBMIT")

with Update:
    st.header("UPDATE!")
    st.write("HERE YOU CAN UPDATE YOUR PERSONAL DETAILS!")
    rows = rows - 2
    NAme = st.text_input("Name: ").strip().upper()
    heading = st.text_input("HEADING: ").strip().upper()
    for i in range(0, rows):
        if NAme == df.iloc[i, 0]:
            if heading == "ADMISSION NO":
                new = st.text_input("New Input: ")
                df.iloc[i, 1] = new
                df.to_csv(file_location, index=False)
            elif heading == "CLASS":
                new = st.text_input("NEw Input: ")
                df.iloc[i, 2] = new
                df.to_csv(file_location, index=False)
            elif heading == "SECTION":
                new = st.text_input("NEW INPUT: ")
                df.iloc[i, 3] = new
                df.to_csv(file_location, index=False)
            elif heading == "ROLL NO":
                new = st.text_input("new input: ")
                df.iloc[i, 4] = new
                df.to_csv(file_location, index=False)
            else:
                pass

with Read:
    st.header("SHOW AN ID!")
    Admission_no = st.text_input("Enter Admission no: ").strip().upper()
    if Admission_no != "":
        for i in range(0, rows):
            if Admission_no == df.iloc[i, 1]:
                Name = df.iloc[i, 0]
                Admission_no = df.iloc[i, 1]
                Class = df.iloc[i, 2]
                Section = df.iloc[i, 3]
                Roll_no = df.iloc[i, 4]
            else:
                pass

        try:
                 st.write("NAME: " + str(Name))
                 st.write("ADMISSION NO: " + str(Admission_no))
                 st.write("CLASS: " + str(Class))
                 st.write("SECTION: " + str(Section))
                 st.write("ROLL NO: " + str(Roll_no))
        except:
            st.write("INPUT IS INVALID!")
    else:
        pass

with Delete:
    st.header("DELETE AN ID!")
    st.write("HERE YOU CAN DELETE THE STUDENT'S ID!")
    ADmission_no = st.text_input("ADMISSION NO:").strip().upper()
    if ADmission_no != "":
        if ADmission_no in list(df["ADMISSION NO"]):
            result = st.text_input("ARE YOU SURE: ").strip().upper()
            if result == "YES":
                for i in range(0, rows):
                    if ADmission_no == df.iloc[1, i]:
                        NAMe = df.iloc[i, 0]
                        df = df[df["ADMISSION NO"] != ADmission_no]
                        df.to_csv(file_location, index=False)
                    else:
                        pass
            elif result == "NO":
                st.write("PROCESS CANCELLED!")
        else:
            st.write("THE ADMISSION NO. IS INCORRECT!")
    else:
        pass

table = df[["NAME", "ADMISSION NO", "CLASS", "SECTION", "ROLL NO"]].astype(str)
st.dataframe(table)
