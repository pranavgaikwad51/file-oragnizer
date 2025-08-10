def organize_files_simulation():
    files = input("Enter file names separated by commas: ").split(",")
    files = [f.strip() for f in files]

    organized = {}  # Dictionary to store by extension

    for file in files:
        if "." in file:
            ext = file.split(".")[-1].lower()
        else:
            ext = "NoExtension"

        if ext not in organized:
            organized[ext] = []
        organized[ext].append(file)

    print("\n📂 Files grouped by extension:")
    for ext, items in organized.items():
        print(f"{ext}/")
        for f in items:
            print(f"   {f}")

if __name__ == "__main__":
    organize_files_simulation()
