# ============================================================
# DAY 4 PROJECT - Contact Book
# Uses: dictionaries, tuples, sets, functions, file-style structure
# ============================================================

# Our "database" - a dictionary of dictionaries
contacts = {}
groups = {}   # group_name -> set of contact names


# ============================================================
# CONTACT OPERATIONS
# ============================================================


def add_contact(name,phone, email="", group=""):
    """ add new contact"""
    if name in contacts:
        print(f" contact '{name}' already exists. use update instead" )
        return False
        
    contacts[name] = {
        "phone": phone,
        "email": email,
        "group": group
    }
    if group:
        if group not in groups:
            groups[group] = set()
        groups[group].add(name)
    
    print(f" conatact {name} added.")
    return True 


def update_contact(name, **kwargs):
    """Update one or more fields of an existing contact."""
    if name not in contacts:
        print(f"  Contact '{name}' not found.")
        return False

    for field, value in kwargs.items():
        contacts[name][field] = value

    print(f"  Contact '{name}' updated.")
    return True


def delete_contact(name):
    """Delete a contact."""
    if name not in contacts:
        print(f"  Contact '{name}' not found.")
        return False

    info = contacts.pop(name)

    if info["group"] and info["group"] in groups:
        groups[info["group"]].discard(name)

    print(f"  Contact '{name}' deleted.")
    return True

def search_contact(query):
    """Search contacts by name (partial match)."""
    query = query.lower()
    results = {
        name: info
        for name, info in contacts.items()
        if query in name.lower()
    }

    if not results:
        print(f"  No contacts found for '{query}'.")
    else:
        print(f"\n  Found {len(results)} contact(s):")
        for name, info in results.items():
            display_contact(name, info)

    return results


def display_contact(name, info):
    """Display a single contact's details."""
    print(f"\n  Name:  {name}")
    print(f"  Phone: {info['phone']}")
    if info['email']:
        print(f"  Email: {info['email']}")
    if info['group']:
        print(f"  Group: {info['group']}")
    print("  " + "-" * 25)


def list_all_contacts():
    """List all contacts sorted alphabetically."""
    if not contacts:
        print("  No contacts saved yet.")
        return

    print(f"\n  Total contacts: {len(contacts)}")
    print("  " + "=" * 30)

    for name in sorted(contacts.keys()):
        info = contacts[name]
        group_tag = f"[{info['group']}]" if info['group'] else ""
        print(f"  {name:<20} {info['phone']:<15} {group_tag}")


def list_group(group_name):
    """List all contacts in a group."""
    if group_name not in groups or not groups[group_name]:
        print(f"  Group '{group_name}' is empty or doesn't exist.")
        return

    print(f"\n  Group: {group_name}")
    print(f"  Members: {len(groups[group_name])}")
    print("  " + "-" * 25)
    for name in sorted(groups[group_name]):
        print(f"  - {name}: {contacts[name]['phone']}")


def get_stats():
    """Show contact book statistics using sets and dicts."""
    total = len(contacts)
    with_email = sum(1 for info in contacts.values() if info["email"])
    group_names = {info["group"] for info in contacts.values() if info["group"]}
    phones = [info["phone"] for info in contacts.values()]
    unique_phones = len(set(phones))    # set removes duplicates

    print(f"\n  Total contacts:    {total}")
    print(f"  With email:        {with_email}")
    print(f"  Without email:     {total - with_email}")
    print(f"  Groups:            {len(group_names)}")
    print(f"  Unique phones:     {unique_phones}")
    if group_names:
        print(f"  Group names:       {', '.join(sorted(group_names))}")


# ============================================================
# MENU & MAIN
# ============================================================

def show_menu():
    print("\n" + "=" * 40)
    print("         CONTACT BOOK")
    print("=" * 40)
    print("  1. Add contact")
    print("  2. Search contact")
    print("  3. List all contacts")
    print("  4. Update contact")
    print("  5. Delete contact")
    print("  6. List by group")
    print("  7. Statistics")
    print("  0. Exit")
    print("-" * 40)


def handle_add():
    name  = input("  Name:         ").strip()
    phone = input("  Phone:        ").strip()
    email = input("  Email (skip): ").strip()
    group = input("  Group (skip): ").strip()

    add_contact(name, phone, email, group)


def handle_update():
    name = input("  Contact name: ").strip()
    if name not in contacts:
        print(f"  '{name}' not found.")
        return
    print("  What to update? (leave blank to skip)")
    phone = input(f"  New phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"  New email [{contacts[name]['email']}]: ").strip()
    updates = {}
    if phone:
        updates["phone"] = phone
    if email:
        updates["email"] = email
    if updates:
        update_contact(name, **updates)
    else:
        print("  No changes made.")


def seed_sample_data():
    """Pre-load some contacts so you can test immediately."""
    add_contact("Ali Khan",    "0300-1234567", "ali@gmail.com",   "Friends")
    add_contact("Sara Ahmed",  "0321-9876543", "sara@work.com",   "Work")
    add_contact("Umar Farooq", "0333-5556677", "",                "Friends")
    add_contact("Zara Malik",  "0311-1112222", "zara@gmail.com",  "Work")
    add_contact("John Smith",  "0345-9990001", "john@yahoo.com",  "")
    print("  Sample contacts loaded.\n")


def main():
    print("Welcome to Contact Book!")
    seed_sample_data()

    while True:
        show_menu()
        choice = input("  Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            handle_add()
        elif choice == "2":
            query = input("  Search name: ").strip()
            search_contact(query)
        elif choice == "3":
            list_all_contacts()
        elif choice == "4":
            handle_update()
        elif choice == "5":
            name = input("  Name to delete: ").strip()
            delete_contact(name)
        elif choice == "6":
            group = input("  Group name: ").strip()
            list_group(group)
        elif choice == "7":
            get_stats()
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
