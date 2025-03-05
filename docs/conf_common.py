# ---------------------------------------------------------------

from esp_docs.conf_docs import *  # noqa: F403,F401

languages = ["en"]

# idf_targets = [
#     "esp32",
# ]

# link roles config
github_repo = "espressif/arduino-esp32"

# context used by sphinx_idf_theme
html_context["github_user"] = "espressif"  # noqa: F405
html_context["github_repo"] = "arduino-esp32"  # noqa: F405

html_static_path = ["../_static"]

# Conditional content

extensions += [  # noqa: F405
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "esp_docs.esp_extensions.dummy_build_system",
]

# ESP32_DOCS = [
#     "index.rst",
# ]

# ESP32S2_DOCS = ESP32_DOCS

# conditional_include_dict = {
#     "esp32": ESP32_DOCS,
# }

# Extra options required by sphinx_idf_theme
project_slug = "arduino-esp32"

# versions_url = "./../_static/arduino_versions.js"
