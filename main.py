import os
import colorama
from colorama import Fore, Style
from languages import set_language, get_translation
from utils import get_malware_signatures_path, get_malicious_links_path
from scanner import check_link, check_apk, check_file, scan_malware
import json
import requests
import subprocess
import sys

# Initialisation de colorama
colorama.init()

def update_malware_signatures():
    try:
        # Ajouter ici la logique pour mettre à jour la base de données des signatures de logiciels malveillants
        print(Fore.MAGENTA + "Updating malware signatures database..." + Style.RESET_ALL)
        # Exemple : téléchargement du fichier de signatures depuis un serveur distant
        # Enregistrement du fichier localement
        print(Fore.MAGENTA + "Malware signatures database updated successfully!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error updating malware signatures: {e}" + Style.RESET_ALL)

def main():
    install_dependencies()
    install_apktool()
    malicious_links = load_malicious_links()
    malware_signatures = load_malware_signatures()
    while True:
        display_menu()
        choice = input(Fore.BLUE + get_translation("choose_option") + Style.RESET_ALL)
        if choice == '1':
            url = input(Fore.GREEN + get_translation("enter_link") + Style.RESET_ALL)
            result = check_link(url, malicious_links)
            print(result)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '2':
            apk_path = input(Fore.GREEN + get_translation("enter_apk_path") + Style.RESET_ALL)
            result = check_apk(apk_path)
            print(result)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '3':
            file_path = input(Fore.GREEN + get_translation("enter_file_path") + Style.RESET_ALL)
            result = check_file(file_path)
            print(result)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '4':
            scan_malware_result = scan_malware(file_path, malware_signatures)
            print(scan_malware_result)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '5':
            show_info()
        elif choice == '6':
            lang = input(Fore.GREEN + get_translation("enter_language") + Style.RESET_ALL)
            set_language(lang)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause
        elif choice == '7':
            update_script()
        else:
            print(Fore.RED + get_translation("invalid_option") + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)  # Ajout de la pause

if __name__ == "__main__":
    main()
