# Wallpaper CLI
*A command-line tool for managing wallpapers on Hyprland using SWWW*

## Overview

- ✅**Set Specific Wallpaper** - Apply a wallpaper instantly using the CLI.
- ✅**Random Wallpaper Selection** - Pick a random wallpaper from a user-defined pool.
- ✅**Minimal Dependencies** - Requires only 'python' and 'swww'.
- ✅**Simple & Modular** - Clean and maintainable Python codebase.

---

## 📦 Installation
## 🔹 Manual Installation
1. Clone the repository:
``` bash
git clone https://github.com/Akihiro120/wallpaper-cli
cd wallpaper-cli
```
2. Build and install the package using `makepkg`:
``` bash
makepkg -si
```

---
## 🖥️ Usage
Once installed, you can run wallpaper-cli directory from the terminal.

**Add Picture**
``` bash
wallpaper-cli --add "filepath/to/picture"
```

**Remove Picture**
``` bash
wallpaper-cli --remove index
```

**Set Picture**
``` bash
wallpaper-cli --set index
```

**Display Pictures**
``` bash
wallpaper-cli --display
```

**Prev**
``` bash
wallpaper-cli --prev
```

**Next**
``` bash
wallpaper-cli --next
```

**Toggle Cycle**
``` bash
wallpaper-cli --togglecycle
```
**Enable Cycle Feature**
``` bash
wallpaper-cli --enablecycle
```

---
## 🔧 Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch:
``` bash
git checkout -b feature/your-feature-name
```
3. Make your changes and commit them:
``` bash
git commit -m "Add feature XYZ"
```
4. Push the branch to your fork
``` bash
git push origin feature/your-feature-name
```
5. Open a pull request

---
## 📝 License

This project is licensed under the GNU General Public License (GPL).
See the LICENSE file for details.

---
## 📬 Contact

For support, bug reports, or feature requests, please open an issue on GitHub.
