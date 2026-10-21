[app]

# (str) Title of your application
title = Portefeuille de Poche

# (str) Package name
package.name = portefeuille

# (str) Package domain (needed for android packaging)
package.domain = org.wallet

# (str) Source code where the main.py lives
source.dir = .

# (str) Application versioning
version = 0.1

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of exclusion patterns
source.exclude_exts = spec

# (list) List of exclusions using pattern matching
source.exclude_dirs = tests, bin, venv

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The permissions for your application
android.permissions = INTERNET

# (list) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_root = 1
