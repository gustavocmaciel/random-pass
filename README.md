<p align="center">
 <img src="">
   <a href=""><img src=""></a>
 </p>
<h1 align="center"><b>Random Password</b></h1>
<p align="center">A Password Generator Tool.</p>

![Screenshot](./assets/takenote-light.png)

## About

Random password is a web version of [pass-gen-cli](https://github.com/gcmaciel/pass-gen-cli), which means it is a password generator desinged to work on web browsers.

It generates a password containing a uppercase letter, a special character, a number and lowercase letters. The user can choose the length of the password (it can be either 4, 16, 32 or 64).

This project was created with Python (Flask), Javascript and, of course, HTML and CSS.

## Contributing

Feel free to [open a bug](https://github.com/gcmaciel/random-pass/issues) or [contribute to code](https://github.com/gcmaciel/random-pass/pulls)

### Folder structure

Description of the project files and directories.

```bash
├── templates/                 # Templates files
│   ├── index.html             # Index file
│   ├── layout.js              # The application layout
│   ├── new_password.html      # File to render the genarated password to the user
├── static/                    # Static files
│   ├── favicon.ico            # Icon
│   ├── scripts.js             # Main Javascript file
│   ├── styles.css             # CSS
├── media/                     # Media files
│   ├── screenshot_index.png   # Index page screenshot
│   ├── screenshot_new.png     # New password page screenshot
├── application.py             # Main application file
├── helpers.py                 # File where the function to generate password is defined
├── .gitignore                 # Files ignored by git
├── CHANGELOG.md               # List of significant changes
├── LICENSE                    # License for this open source project
├── README.md
```

### Styleguide

Some coding convetions for the project:

- Double quotes
- Four space indentation (Python, HTML)
- Two space indentation (Javascript)
    

## Author

[gcmaciel](https://github.com/gcmaciel)


## License

This project is open source and available under the [MIT license](LICENSE).
