import asyncio
import random
import time
from actions import ACTIONS, ALL_ACTIONS
import os
from rich.console import Console
from rich.text import Text
from rich.progress import Progress
import sys

console = Console()

os.system("cls")

banner = Text("""

==================================================
==               ___         _  _               ==
==              /   \  __ _ (_)| | _   _        ==
==             / /\ / / _` || || || | | |       ==
==            / /_// | (_| || || || |_| |       ==
==           /___,'   \__,_||_||_| \__, |       ==
==                                 |___/        ==
==                                              ==
==             /\/\    ___   __ _   __ _        ==
==            /    \  / _ \ / _` | / _` |       ==
==           / /\/\ \|  __/| (_| || (_| |       ==
==           \/    \/ \___| \__, | \__,_|       ==
==                          |___/               ==
==               ___         _                  ==
==              /   \ _   _ | | _   _           ==
==             / /\ /| | | || || | | |          ==
==            / /_// | |_| || || |_| |          ==
==           /___,'   \__,_||_| \__,_|          ==
==                                              ==
==================================================                                                                                                
==                 Mang Yeye                    ==                                                                  
==================================================                                                                                                               
            
              """, style="bold cyan")

console.print(banner)

def get_user_choice():
    console.print("\n[bold yellow]Pilih mode:[/bold yellow]")
    console.print("1: Prosedur anu ditangtukeun ku pangguna (ti actions.py) [sakali]", style="green")
    console.print("2: Acak (loop tanpa wates sareng sadaya tindakan)", style="blue")
    console.print("3: Loop tanpa wates (tindakan anu ditangtukeun ku pangguna sacara urut)", style="magenta")
    
    choice = input("\nLebetkeun nomer anjeun: ")
    return choice

async def execute_actions(actions):
    for action_name, action_func, is_async in actions:
        console.print(f"\n🚀 [bold cyan]Ngalaksanakeun:[/bold cyan] {action_name}...")
        with Progress() as progress:
            task = progress.add_task("[cyan]Ngolah...", total=100)
            for _ in range(10):
                time.sleep(0.2)
                progress.update(task, advance=10)
        try:
            if is_async:
                result = await action_func()
            else:
                result = action_func()

            if isinstance(result, str):
                console.print(f"✅ [bold green]{action_name} parantos réngsé![/bold green] TX: {result}")
        except Exception as e:
            console.print(f"❌ [bold red]Kasalahan nalika ngalaksanakeun:[/bold red] {action_name}: {e}")

        time.sleep(2)

async def main():
    choice = get_user_choice()

    if choice == "2":
        while True:
            tasks = ALL_ACTIONS.copy()
            random.shuffle(tasks)
            await execute_actions(tasks)
            console.print("\n🔄 [bold yellow]Mimitian siklus acak anyar.[/bold yellow]\n")
            time.sleep(5)

    elif choice == "3":
        while True:
            await execute_actions(ACTIONS)
            console.print("\n🔄 [bold yellow]Ngulang tindakan anu ditangtukeun ku pangguna...[/bold yellow]\n")
            time.sleep(5)
    else:
        await execute_actions(ACTIONS)

asyncio.run(main())