"""Update an IP allow-list by removing addresses that are no longer authorized."""


def update_file(import_file, remove_list):
    """Remove IP addresses in remove_list from the allow-list text file."""
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    ip_addresses = ip_addresses.split()

    # Iterate over a copy so removals do not affect loop traversal.
    for element in ip_addresses[:]:
        if element in remove_list:
            ip_addresses.remove(element)

    ip_addresses = " ".join(ip_addresses)

    with open(import_file, "w") as file:
        file.write(ip_addresses)


if __name__ == "__main__":
    import_file = "allow_list.txt"
    remove_list = [
        "192.168.97.225",
        "192.168.158.170",
        "192.168.201.40",
        "192.168.58.57",
    ]
    update_file(import_file, remove_list)
