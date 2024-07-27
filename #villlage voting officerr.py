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

    # Ensure the candidate is the majority
    if count > num_voters // 2:
        return candidate
    else:
        return -1

# Taking input from the user
num_voters = int(input("Enter the number of voters: "))
votes = list(map(int, input("Enter the votes separated by spaces: ").split()))

# Ensure that the number of votes matches the number of voters
if len(votes) != num_voters:
    print("The number of votes does not match the number of voters.")
else:
    # Find and print the majority party or -1 if there is no majority
    result = find_majority_party(num_voters, votes)
    print(result)
