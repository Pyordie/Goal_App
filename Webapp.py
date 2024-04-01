import streamlit as st
import functions


st.title("Goaly")
st.subheader("This the goaly app")

st.text("Ennter your goals: ")


def add_goal():
    goal = st.session_state["new_goal"]
    goals.append(goal + '\n')
    functions.update_goals(goals)

## Showing goals
goals = functions.get_goals()
for i , goali in enumerate(goals):
    checkbox = st.checkbox(goali, key=goali)
    if checkbox:
        goals.pop(i)
        functions.update_goals(goals)
        del st.session_state[goali]
        st.rerun()
## adding goals
st.text_input("Add your goals: ", on_change=add_goal, key="new_goal")

## deleting goals :


