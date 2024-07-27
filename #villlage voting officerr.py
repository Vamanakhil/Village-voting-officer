import streamlit as st

def find_majority_party(num_voters, votes):
    if num_voters == 1:
        return votes[0]

    candidate = None
    count = 0

    # First pass to find the candidate
    for vote in votes:
        if count == 0:
            candidate = vote
            count = 1
        elif vote == candidate:
            count += 1
        else:
            count -= 1

    # Second pass to confirm the candidate
    count = 0
    for vote in votes:
        if vote == candidate:
            count += 1

    if count > num_voters // 2:
        return candidate
    else:
        return -1

# Streamlit App
st.title("Majority Party Finder")

# Input: Number of Voters
num_voters = st.number_input("Enter the number of voters:", min_value=1, step=1)

# Input: Votes
votes_input = st.text_area("Enter the votes separated by space (e.g., 1 2 2 3 2 1):")
votes = list(map(int, votes_input.split())) if votes_input else []

# Button to find the majority party
if st.button("Find Majority Party"):
    if len(votes) != num_voters:
        st.error(f"The number of votes ({len(votes)}) does not match the number of voters ({num_voters}).")
    else:
        result = find_majority_party(num_voters, votes)
        if result == -1:
            st.write("No party has the majority.")
        else:
            st.write(f"The majority party is: {result}")

# Example usage
if st.button("Show Example"):
    st.write("Example:")
    st.write("Number of Voters: 6")
    st.write("Votes: 1 1 2 2 2 3")
    result = find_majority_party(6, [1, 1, 2, 2, 2, 3])
    st.write(f"The majority party in the example is: {result}")
