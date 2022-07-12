import streamlit as st
from PIL import Image
image = Image.open('Hosp.jpeg')

st.sidebar.title(" Cross Hospitals Checkin App")
st.sidebar.image(image,caption = " ")
st.sidebar.error(f'''Welcome to Cross Hospital''')
st.sidebar.write(f''' Cross Hospital is a divison of Cross Group of companies.''')
st.sidebar.write(f''' The many patients we treat each year prepares us to treat the one who matters most — you.
                    When you need answers - Come to us.''')

option_list = ['Select','Yes','No']
options = st.sidebar.selectbox(" Is this your first time at Cross Hospital? ",option_list)
proceed = st.sidebar.button( " Proceed")

if options == 'Yes': 
    st.subheader(" Registration Form ")
    st.write(" Note all * are compulsory and mus be filled.")
    
    col1,col2 = st.columns(2)
    with col1:
        st.text_input( "First name * : ")
    with col2 :
        st.text_input(" Last name * :")
    col1,col2,col3 = st.columns(3)
    with col1 :
        st.number_input(" Age : ")
    with col2:
        st.number_input(" Phone no *: ")
    with col3:
        gender_list= ['Select','Male','Female']
        st.selectbox(" Gender : ", gender_list)
    st.text_input( " Full Address * : ")
    st.write(" Provide your Next of Kin(NOK) details below ")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input(" NOK's Full name : ")
    with col2:
        st.number_input(" NOK's Phone no *: ")
    st.text_input(" NOK's Full Address : ")
    submit = st.button("Submit")
    if submit :
        st.success(" Form submitted Succesfully ")
        st.write(f''' Kindly proceed to Annex B - Accounts Department for Payment. \n
                     Make a registration payment of N2,500 ''')
        st.subheader(" Thank you ")
    
    
elif options == 'No' :
    st.title("  Welcome to Cross Hospital. ")
    st.subheader(" Input your hospital registration number ")
    st.number_input(" ")
    
    dept_list = ['Select a department','GOPD','OB-GYN','Pediatrics','Radiology']
    st.success(f''' Note - GOPD: General outpatient Department. \t 
                    OB-GYN : Obstetrics and Gynaecology''')
    dept = st.selectbox(" Choose the department for visit ", dept_list)
    no_submit = st.button(" Submit ")
    if dept == 'GOPD' and no_submit:
        st.write(f''' Kindly proceed to the Nursing room at Annex C - Hall 1 for Vitals check. ''')
    elif dept == 'OB-GYN' and no_submit :
        st.write(f''' Kindly proceed to the Nursing room at Annex B - Hall 2 for Vitals check. ''')
    elif dept == 'Pediatrics' and no_submit :
        st.write(f''' Kindly proceed to the Nursing room at the Children's Clinic in Annex C - Hall 2 for Vitals check. ''')
    elif dept == 'Radiology' and no_submit :
        st.write(f''' Kindly proceed to the Nursing room at Annex E - Hall 1 for more Inquiries. ''')
    elif dept == 'Select a department' : 
        image = Image.open('no_page.jpg')
        st.image(image,caption = " ")
        
    
    
else:
    st.title(" Welcome to Cross Hospital")
    st.write(f''' Cross Hospital is a divison of Cross Group of companies. 
                    The many patients we treat each year prepares us to treat the one 
                    who matters most — you. When you need answers - Come to us.''')
    image = Image.open('doctor.jpg')
    st.image(image,caption = " We utilise state-of-the-art technologies and employs a team of true experts. ")
    
