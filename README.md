# password checker script

a fun and easy way to check how strong your passwords are!

## what it does

- shows a cool box with your password rating
- uses pretty colors in the terminal
- tells you what's good and bad about your password
- easy to use - just type in your password
- gives you a score from 0 to 6

## what you need

- python 3.6 or newer
- the colorama package (easy to install)

## how to set it up

1. download these files
2. open your terminal and run:
```bash
pip install -r requirements.txt
```

## how to use it

just run:
```bash
python password_checker.py
```

then:
- type in your password when it asks
- it'll show you:
  - a cool box with your password strength
  - your score out of 6
  - what's good and bad about your password
- type 'quit' when you're done

## what makes a good password?

it checks for:
- length (8+ characters is good)
- big letters (like A, B, C)
- small letters (like a, b, c)
- numbers (like 1, 2, 3)
- special stuff (like !, @, #)

## what you'll see

you'll get:
- a cool box showing how strong your password is
- a progress bar that fills up based on your score
- green for good stuff, yellow for okay stuff, red for weak stuff
- a list of what's good and bad about your password 