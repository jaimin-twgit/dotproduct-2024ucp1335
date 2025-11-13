def main():
    vec1 = list(map(float, input("Enter elements of first vector (space-separated): ").split()))
    vec2 = list(map(float, input("Enter elements of second vector (space-separated): ").split()))
    if len(vec1) != len(vec2):
        print("Error: Vectors must be of the same length.")
        return
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    print("Dot Product:", dot_product)

if __name__ == "__main__":
    main()

#this is change in main branch 

#this is a new branch.


#this is stash 


