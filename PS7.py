def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move the n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Take user input
n = int(input("Enter the number of disks: "))

# Call the function
tower_of_hanoi(n, 'A', 'B', 'C')
