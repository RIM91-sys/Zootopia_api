import data_fetcher


def generate_html(animal_name, animal_data):
    """Generate an HTML file based on the API response."""
    html_content = "<html><head><title>Animal Info</title></head><body>"
    html_content += f"<h1>Results for: {animal_name}</h1>"

    if animal_data:  # If data exists
        for animal in animal_data:
            html_content += f"<h2>{animal.get('name', 'Unknown')}</h2>"
            scientific_name = animal.get("taxonomy", {}).get("scientific_name", "N/A")
            habitat = animal.get("characteristics", {}).get("habitat", "N/A")
            lifespan = animal.get("characteristics", {}).get("lifespan", "N/A")
            diet = animal.get("characteristics", {}).get("diet", "N/A")

            html_content += f"<p><strong>Scientific Name:</strong> {scientific_name}</p>"
            html_content += f"<p><strong>Habitat:</strong> {habitat}</p>"
            html_content += f"<p><strong>Lifespan:</strong> {lifespan}</p>"
            html_content += f"<p><strong>Diet:</strong> {diet}</p>"
            html_content += "<hr>"
    else:
        html_content += f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
        html_content += "<p>Try searching for another animal.</p>"

    html_content += "</body></html>"

    # Save HTML file
    with open("animals.html", "w") as file:
        file.write(html_content)

    print(f"Website was successfully generated to the file animals.html.")

# Main Program
def main():
    animal_name = input("Enter a name of an animal: ").strip()
    animal_data = data_fetcher.fetch_data(animal_name)  # Now using the fetcher module
    generate_html(animal_name, animal_data)


if __name__ == "__main__":
    main()
