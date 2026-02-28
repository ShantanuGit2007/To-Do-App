import streamlit as st

#List for store task
if "list_of_task" not in st.session_state:
    st.session_state.list_of_task=[]

#Header Section
st.markdown('''
<center style: font-family="font-family: "Source Sans", sans-serif;"><h2>To-Do-App📝</h2></center>
''',
unsafe_allow_html=True)
#Task input section
task=st.text_input(label="Add Task", placeholder="Add Task Here",icon=":material/assignment:")

if st.button("Add Task",icon=":material/task_alt:"):

        if task:
            st.session_state.list_of_task.append(task.capitalize())
            st.success("Task Added Successfully")

#Delet and manipulated Section
col1,col2=st.columns([1,1])
#Delet Section
with col1:
    if st.session_state.list_of_task:
        deleted_task=st.selectbox("Select Task To Delete",(st.session_state.list_of_task))
        if st.button("Delete",icon=":material/delete:"):
            st.session_state.list_of_task.remove(deleted_task)

#manipulated Section
with col2:
     if st.session_state.list_of_task:
        manipulated_task=st.selectbox("Select Task To Change",(st.session_state.list_of_task))
        if manipulated_task:
            new_task=st.text_input(label="Add New Task", placeholder="Add  New Task Here",icon=":material/assignment:")
            if st.button("Change",icon=":material/change_circle:",):
            # if st.button("Change",icon=":material/change_circle:"):
                if new_task:
                    index_of_new_task=st.session_state.list_of_task.index(manipulated_task)
                    st.session_state.list_of_task[index_of_new_task]=new_task    

#Display Task Section
st.divider()
if st.session_state.list_of_task:
    for i, j in enumerate(st.session_state.list_of_task, start=1):
        st.checkbox(f"{j.title()}", key=f"task_{i}")
else:
    st.write("No tasks yet. Add some!")
st.divider()
#Clear All Section
if st.button("Clear Task",icon=":material/delete_sweep:"):
    st.session_state.list_of_task.clear()
#Fotter Section
st.markdown('''
<center style: font-family="font-family: "Source Sans", sans-serif;"><p> "Built With ❤️ and fueled by ☕️" </p></center>
''',
unsafe_allow_html=True)
