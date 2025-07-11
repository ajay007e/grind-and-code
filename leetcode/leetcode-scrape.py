import os
import pathlib
import re
import sys

import requests


def get_leetcode_description(slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/",
        "User-Agent": "Mozilla/5.0",
    }

    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            title
            difficulty
            topicTags {
              name
            }
            content
            frontendQuestionId: questionFrontendId
          }
        }
        """,
        "variables": {"titleSlug": slug},
    }

    response = requests.post(url, json=query, headers=headers)
    if response.status_code == 200:
        data = response.json()
        question = data["data"]["question"]
        return {
            "title": question["title"],
            "difficulty": question["difficulty"],
            "topics": [tag["name"] for tag in question["topicTags"]],
            "description_html": question["content"],
            "frontendId": question["frontendQuestionId"],
        }
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


def fetch_file_with_extension(file_path, extension):
    for file_name in os.listdir(file_path):
        full_path = os.path.join(file_path, file_name)
        if os.path.isfile(full_path) and file_name.endswith(extension):
            return full_path  # Return full path


def fetch_first_file_content(file_path, extension):
    for file_name in os.listdir(file_path):
        full_path = os.path.join(file_path, file_name)
        if os.path.isfile(full_path) and file_name.endswith(extension):
            with open(full_path, "r") as file:
                return file.read()
    return None


def generate_code_markdown(content, language):
    return f"""

<details>
<summary>Click to read {language.capitalize()} code</summary>

```{language}
{content}
```

</details>
    """


def generate_example_block(examples):
    matches = re.findall(r"<pre>(.*?)</pre>", examples, re.DOTALL)
    example_md = """

## 🧪 Examples
"""
    for i, content in enumerate(matches, 1):
        example_md += f"""
### Example {i}
<pre>{content}</pre>

"""
    return example_md


def generate_constraints_block(constraints):
    matches = re.findall(r"<ul>(.*?)</ul>", constraints, re.DOTALL)
    contraints_md = f"""

## 📌 Constraints"
<ul>{matches[0]}</ul>
"""
    return contraints_md


def update_mardown(file_path):
    python_code = fetch_first_file_content(file_path, ".py")
    java_code = fetch_first_file_content(file_path, ".java")
    code = ""
    if python_code != None:
        code += generate_code_markdown(python_code, "python")
    if java_code != None:
        code += generate_code_markdown(java_code, "java")

    markdown_content = f"""

---

## 🧠 Code

{code}


"""
    filename = fetch_file_with_extension(file_path, ".md")
    with open(filename, "a") as file:
        file.write(markdown_content)


def generate_markdown(slug):
    details = get_leetcode_description(slug)
    description = details["description_html"].split("<p>&nbsp;</p>")
    example_md = generate_example_block(description[1])
    constraints_md = generate_constraints_block(description[2])

    markdown_content = f"""# 🧩 {details["frontendId"]}: {details["title"]}

- **Difficulty**: `{details["difficulty"]}`
- **Tags / Topics**: {", ".join(f"`{tag}`" for tag in details["topics"])}
- **Link**: [Leetcode](https://leetcode.com/problems/{slug}/)

---

## 📜 Description

{description[0]}
{example_md}
{constraints_md}
"""
    pathlib.Path(details["frontendId"]).mkdir(parents=True, exist_ok=True)
    filename = f"{details['frontendId']}/{details['frontendId']}.md"
    with open(filename, "w") as f:
        f.write(markdown_content)

    print(f"\n✅ Saved: {filename}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python leetcode-scrape.py [generate|update] [args]")
        return

    action = sys.argv[1]

    if action == "generate":
        if len(sys.argv) < 3:
            print("Error: Missing LeetCode URL for 'generate'")
            return
        link = sys.argv[2]
        if "/problems/" not in link:
            print("Invalid LeetCode URL format.")
        else:
            slug = link.split("/problems/")[1].strip("/")
            generate_markdown(slug)

    elif action == "update":
        if len(sys.argv) < 3:
            print("Error: Missing File path for 'update'")
            return
        file_path = sys.argv[2]
        update_mardown(file_path)

    else:
        print("Unknown action. Use 'generate' or 'update'.")


if __name__ == "__main__":
    main()
