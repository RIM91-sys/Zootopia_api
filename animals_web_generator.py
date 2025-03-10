import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def generate_animal_info(data):
    """Generates a formatted string for the animals' information."""

    output = ""

    for animal_obj in data:
        if 'name' not in animal_obj or 'diet' not in animal_obj['characteristics'] or 'type' not in animal_obj[
            'characteristics'] or 'locations' not in animal_obj:
            continue  # Skip animals missing required fields
        output += serialize_animal(animal_obj)
    return output


def serialize_animal(animal_obj):
    """ Handle a single animal serialization """
    output = ""


    output += '<li class="cards__item">'
    output += '<div class="card__title">'


    output += f" {animal_obj['name']}</div>\n"
    output += '<p class="card__text">'

    if 'diet' in animal_obj['characteristics']:
        output += f"<strong>Diet:</strong>{animal_obj['characteristics']['diet']}<br/>\n"

    if isinstance(animal_obj['locations'], list) and animal_obj['locations']:
       output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"

    if 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"

    output += " " * 30 + "\n"  # Separator for readability
    output += '</p>'
    output += '</li>'

    return output



def create_html_file(template_path, output_path, animals_info):
    """ Generates an HTML file replacing the placeholder with the animal data """
    with open(template_path, "r") as file:
        html_content = file.read()

    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_path, "w") as file:
        file.write(new_html_content)

animals_data = load_data("animals_data.json")

animals_info = generate_animal_info(animals_data)

create_html_file("animals_template.html", "animals.html", animals_info)
print(animals_info)