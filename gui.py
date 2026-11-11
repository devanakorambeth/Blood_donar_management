import streamlit as st
from donarview import BloodDonorManager

donar_instance=BloodDonorManager()

tab1,tab2,tab3,tab4=st.tabs(["Add Donor","View Donors","Update Donor","Delete Donor"])

blood_groups=["A+","A-","B+","B-","AB+","AB-","O+","O-"]

with tab1:
    st.header("add New Donors")
    name=st.text_input("enter donar name")
    blood_group=st.selectbox("select blood group",["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    phone=st.text_input("enter donar phone number")
    city=st.text_input("enter donar city")
    last_donation=st.date_input("enter last donation date")
    if st.button("submit"):
        donar_instance.post(name=name,  blood_group=blood_group, phone=phone, city=city, last_donation=last_donation)
        st.success("donor added successfully....")
        
with tab2:
    st.header("View blood Donor details")
    records=donar_instance.get()
    print("_________")
    print(records)
    if records:
        st.table(records)
    else:
        st.warning("no donors found..!")
        
with tab3:
    st.title("Update Donor details")
    records=donar_instance.get()
    
    if records:
        donar_ids=[r[0] for r in records]
        #donar_ids=[1,5,6,7]
        id=st.selectbox("select donar id",donar_ids,key="update_id")
        
        record=donar_instance.get_object(id=id)
        # record=1,anu,A+,1234567890,city,2023-01-01
        name=st.text_input("enter donar name",value=record[1])
        blood_group=st.selectbox("select blood group",
                                 blood_groups,
                                 index=blood_groups.index(record[2]),
                                 key="update_group")
        phone=st.text_input("enter donar phone number",value=record[3])
        city=st.text_input("enter donar city",value=record[4])
        last_donation=st.date_input("enter last donation date",value=record[5])
        
        if st.button("update"):
            status,message=donar_instance.put(id=id,
                                              name=name,
                                              blood_group=blood_group,
                                              phone=phone,
                                              city=city,
                                              last_donation=last_donation
                                                )
            if status:
                st.success(message)
                
            else:
                st.error(message)
        else:
            st.warning("no donors found..!")
                
                
with tab4:
    st.title("Delete Donor details")
   
    
    