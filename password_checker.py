import re
from colorama import init, Fore, Style
import time

#start up the color thing
init()

def check_password_strength(password):
    score = 0
    feedback = []
    
    #check if password is long enough
    if len(password) >= 12:
        score += 2
        feedback.append(f"{Fore.GREEN}✓ long (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append(f"{Fore.YELLOW}⚠ short (8-11 characters)")
    else:
        feedback.append(f"{Fore.RED}✗ too short (less than 8 characters)")
    
    #check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append(f"{Fore.GREEN}✓ has some uppercase letters")
    else:
        feedback.append(f"{Fore.RED}✗ no uppercase letters")
    
    #check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append(f"{Fore.GREEN}✓ has some lowercase letters")
    else:
        feedback.append(f"{Fore.RED}✗ no lowercase letters")
    
    #check for numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append(f"{Fore.GREEN}✓ has some numbers")
    else:
        feedback.append(f"{Fore.RED}✗ no numbers")
    
    #check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append(f"{Fore.GREEN}✓ has some special characters")
    else:
        feedback.append(f"{Fore.RED}✗ no special characters")
    
    return score, feedback

def display_rating(score):
    box_width = 38  # inside the borders
    bar_width = 30
    rating_art = [
        "╔" + "═" * box_width + "╗",
        "║" + "PASSWORD RATING".center(box_width) + "║",
        "╠" + "═" * box_width + "╣",
        "║" + " " * box_width + "║",
        "║" + " " * box_width + "║",
        "║" + " " * box_width + "║",
        "╚" + "═" * box_width + "╝"
    ]
    
    #pick a color based on how good the password is
    if score >= 5:
        color = Fore.GREEN
        strength = "STRONG PASSWORD"
    elif score >= 3:
        color = Fore.YELLOW
        strength = "OKAY PASSWORD"
    else:
        color = Fore.RED
        strength = "WEAK PASSWORD"
    
    #center the strength text (without color codes)
    strength_line = strength.center(box_width)
    rating_art[3] = f"║{color}{strength_line}{Style.RESET_ALL}║"
    
    #make a progress bar
    bar_length = int((score / 6) * bar_width)
    bar = "█" * bar_length + "░" * (bar_width - bar_length)
    bar_line = f"  {bar}  "  # 2 spaces padding on each side (2+30+2=34), so pad to 38
    bar_line = bar_line.center(box_width)
    rating_art[4] = f"║{color}{bar_line}{Style.RESET_ALL}║"
    
    #show the score, centered
    score_text = f"Score: {score}/6"
    score_line = score_text.center(box_width)
    rating_art[5] = f"║{color}{score_line}{Style.RESET_ALL}║"
    
    return "\n".join(rating_art)

def main():
    #show a welcome message
    print(f"{Fore.CYAN}╔══════════════════════════════════════╗")
    print(f"║        Password Strength Checker     ║")
    print(f"╚══════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    while True:
        #ask for a password
        password = input(f"{Fore.CYAN}type in your password (or 'quit' to exit): {Style.RESET_ALL}")
        
        if password.lower() == 'quit':
            print(f"\n{Fore.YELLOW}see ya later!{Style.RESET_ALL}")
            break
        
        print("\nchecking your password...")
        time.sleep(1) 
        
        score, feedback = check_password_strength(password)
        
        print("\n" + display_rating(score))
        print("\nhere's what i found:")
        for item in feedback:
            print(item)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main() 