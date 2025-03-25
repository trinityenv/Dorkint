import webbrowser
import time
def start():

    tiktok = "https://www.tiktok.com/@disturbingyt"
    github = "https://github.com/trinityenv"
    print(f"""\033[92m

  _____             _    _       _   
 |  __ \           | |  (_)     | |  
 | |  | | ___  _ __| | ___ _ __ | |_ 
 | |  | |/ _ \| '__| |/ / | '_ \| __|
 | |__| | (_) | |  |   <| | | | | |_ 
 |_____/ \___/|_|  |_|\_\_|_| |_|\__|
                        
                       \033[96m [ 1.0 ]
                        \033[91m[ by trinityenv ]
                                                              

    \n
\033[91mFollow on tiktok:    \033[96m{tiktok}
\033[91mFollow me on github: \033[96m{github}

""")
    
    
    
    print("\033[90mChoose attack type\033[90m")
    print("1. Filetype attack")
    time.sleep(0.5)
    

    attack_prompt= input(">\033[92m ") 

    if attack_prompt.isdigit() and int(attack_prompt) == 1:
        
        def search():
            website_prompt = input("Website: \033[94m").strip().lower()
            if website_prompt == "":
                print("Invalid input. Please enter a website.")
            else:
                pass

            domain_prompt = input("\033[92mDomain: \033[94m ").strip().lower()
            print("\n")
            if domain_prompt == "":
                print("Invalid input. Please enter a domain.")
            else:
                pass
            
            print("\033[92m----------------------------------")

            print("Choose file type")

            print("1. PDF")
            print("2. XLS")
            print("3. DOC")
            print("4. TXT")
            print("5. PPT")

            filetype_prompt = input("> ")  

            if filetype_prompt.isdigit():  

                filetype_choice = int(filetype_prompt)

                if filetype_choice == 1:
                    filetype = "pdf"
                elif filetype_choice == 2:
                    filetype = "xls"
                elif filetype_choice == 2:
                    filetype = "xls"
                elif filetype_choice == 3:
                    filetype = "doc"
                elif filetype_choice == 4:
                    filetype = "txt"
                elif filetype_choice == 5:
                        filetype = "ppt"       
            else:
                print("Invalid input.")
                return search()
            
            url = f"https://www.google.com/search?q=filetype:{filetype}+site:{website_prompt}.{domain_prompt}"

            webbrowser.open_new(url)
        search()
   
    else:
        print("Invalid choice")

start()


