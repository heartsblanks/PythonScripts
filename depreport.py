def generate_html_report(dependency_json_path, reverse_dependency_json_path, output_html_path):
    """Generate an HTML report that includes the dependency and reverse dependency reports."""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Dependency Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            h1 {{
                text-align: center;
            }}
            .button {{
                padding: 10px 20px;
                margin: 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            .button:hover {{
                background-color: #0056b3;
            }}
            .content {{
                margin-top: 20px;
                display: none;
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 5px;
                background-color: #f9f9f9;
            }}
            pre {{
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
        </style>
    </head>
    <body>
        <h1>Project Dependency Report</h1>
        <div style="text-align: center;">
            <button class="button" onclick="loadContent('dependency_report.json', 'dependencyContent')">Dependency Report</button>
            <button class="button" onclick="loadContent('reversed_dependency_report.json', 'reverseDependencyContent')">Reverse Dependency Report</button>
        </div>

        <div id="dependencyContent" class="content">
            <h2>Dependency Report</h2>
            <pre id="dependencyPre"></pre>
        </div>

        <div id="reverseDependencyContent" class="content">
            <h2>Reverse Dependency Report</h2>
            <pre id="reverseDependencyPre"></pre>
        </div>

        <script>
            function loadContent(jsonFile, contentId) {{
                fetch(jsonFile)
                    .then(response => response.json())
                    .then(data => {{
                        document.getElementById('dependencyContent').style.display = 'none';
                        document.getElementById('reverseDependencyContent').style.display = 'none';
                        document.getElementById(contentId + 'Pre').textContent = JSON.stringify(data, null, 4);
                        document.getElementById(contentId).style.display = 'block';
                    }})
                    .catch(error => console.error('Error loading content:', error));
            }}
        </script>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_html_path, 'w') as file:
        file.write(html_content)

    print(f"HTML report generated: {output_html_path}")

# Example usage
generate_html_report('dependency_report.json', 'reversed_dependency_report.json', 'project_dependency_report.html')