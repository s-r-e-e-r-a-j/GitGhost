import requests

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print(f"""{GREEN}

   _____ _ _    _____ _               _   
  / ____(_) |  / ____| |             | |  
 | |  __ _| |_| |  __| |__   ___  ___| |_ 
 | | |_ | | __| | |_ | '_ \ / _ \/ __| __|
 | |__| | | |_| |__| | | | | (_) \__ \ |_ 
  \_____|_|\__|\_____|_| |_|\___/|___/\__|
                                           

{RESET}{YELLOW}* GitHub Unfollowers Finder Tool{RESET}
{YELLOW}* https://github.com/s-r-e-e-r-a-j{RESET}\n"""

)

# Prompt for GitHub username
USERNAME = input(f"{YELLOW}Enter your GitHub username: {RESET}").strip()

# Prompt for GitHub token (optional)
TOKEN = input(f"{YELLOW}Enter your GitHub token (Press Enter to use default): {RESET}").strip() or "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"

headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

def get_users(endpoint):
    """ Fetch paginated lists of users (following or followers) """
    users = set()
    url = f"https://api.github.com/users/{USERNAME}/{endpoint}"
    
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            users.update(user["login"] for user in response.json())
            url = response.links.get("next", {}).get("url")  # Handle pagination
        else:
            print(f"{RED}Error fetching {endpoint}: {response.status_code}{RESET}")
            url = None
    return users

print(f"\n{BLUE}Fetching followers and following lists...{RESET}")

# Get lists
following = get_users("following")  # People YOU follow
followers = get_users("followers")  # People WHO FOLLOW YOU

# Find non-followers
not_following_back = following - followers

# Ask to save results
save_file = input(f"\n{YELLOW}Do you want to save results to a file? (y/n): {RESET}").strip().lower()
if save_file == "y":
    file_path = input(f"{YELLOW}Enter file path to save results (e.g., unfollowers.txt): {RESET}").strip()
    with open(file_path, "w") as file:
        file.write("\n".join(not_following_back))
    print(f"{GREEN}Results saved to {file_path}{RESET}")

# Print result
if not_following_back:
    print(f"\n{RED}Users you follow ({len(following)}) but who donâ€™t follow you back ({len(not_following_back)}):{RESET}")
    for user in sorted(not_following_back):
        print(f"{RED}[-] {user}{RESET}")
else:
    print(f"{GREEN}Everyone you follow follows you back! ðŸŽ‰{RESET}")
