from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.text import Text
from time import sleep
import sys
from db.database_settings import DatabaseSettings
from publisher.main import StartBot

class CLIG:
    def __init__(self):
        self.console = Console()
        self.openai_api_key = None
        self.username = None
        self.password = None
        self.wordress_api_url = None
        self.sleep_time = 5
        self.max_length = 200
        self.model = None
        self.keywords = []
        self.total_created = 0
        self.max_articles = 0
        self.trends = None
        self.title = None
        self.running = False
        self.data_exists = True
        self.keywords_exists = False
        self.settings = DatabaseSettings()

    def display_main_menu(self):
        layout = Layout()
        layout.split(
            Layout(name="header", size=3),
            Layout(name="body", ratio=1),
            Layout(name="footer", size=3)
        )

        layout["header"].update(Panel(Text("Glimor's Article Generator Main Menu", justify="center", style="bold cyan"), style="bold blue"))
        menu = Table(show_header=False, box=None)
        if self.data_exists:
            menu.add_row("[bold]1.[/bold] Setup (Already Configured)")
        else:
            menu.add_row("[bold]1.[/bold] Setup")
        if self.keywords_exists:
            menu.add_row("[bold]2.[/bold] Add Keywords (Already Added)")
        else:
            menu.add_row("[bold]2.[/bold] Add Keywords")
        menu.add_row("[bold]3.[/bold] Run Bot")
        menu.add_row("[bold]4.[/bold] Exit")
        layout["body"].update(Align.center(menu))
        layout["footer"].update(Panel(Text("Select an option by entering the corresponding number.", justify="center"), style="bold blue"))

        self.console.print(layout)

    def setup(self):
        self.console.print(Panel("Welcome to the [bold]Glimor's Article Generator[/bold] Setup", title="Setup", style="bold green"))
        self.openai_api_key = Prompt.ask("Enter your OpenAI API Key", default="", show_default=False)
        self.username = Prompt.ask("Enter your Wordpress Username", default="")
        self.password = Prompt.ask("Enter your Wordpress Password", password=True)
        while True:
            self.wordress_api_url = Prompt.ask("Enter your Wordpress API URL", default="https://yourwordpresssite.com/wp-json")
            if self.wordress_api_url.startswith("http"):
                break
            self.console.print("[red]Please enter a valid URL starting with 'http' or 'https'.[/red]")

        while True:
            self.sleep_time = Prompt.ask("Enter the sleep time between requests (in seconds)", default="5", show_default=True)
            try:
                self.sleep_time = int(self.sleep_time)
                break
            except ValueError:
                self.console.print("[red]Please enter a valid number.[/red]")
                
        while True:
            self.max_length = Prompt.ask("Enter the max length of the generated text", default="200", show_default=True)
            try:
                self.max_length = int(self.max_length)
                break
            except ValueError:
                self.console.print("[red]Please enter a valid number.[/red]")
                
        self.model = Prompt.ask("Choose the model to use", choices=["gpt-4o", "gpt-4o-mini"], default="gpt-4o-mini")
        while True:
            self.max_articles = Prompt.ask("Enter the maximum number of articles to generate", default="10", show_default=True)
            try:
                self.max_articles = int(self.max_articles)
                break
            except ValueError:
                self.console.print("[red]Please enter a valid number.[/red]")
        try:
            if self.settings.get_api_key() is None:
                self.settings.insert_one(api_key=self.openai_api_key, wp_api_url=self.wordress_api_url, wp_username=self.username, wp_password=self.password, sleep_time=self.sleep_time, max_length=self.max_length, ai_model=self.model, max_articles=self.max_articles)
            else:
                self.settings.update_one(api_key=self.openai_api_key, wp_api_url=self.wordress_api_url, wp_username=self.username, wp_password=self.password, sleep_time=self.sleep_time, max_length=self.max_length, ai_model=self.model, max_articles=self.max_articles)
            self.console.print("[green]Credentials saved successfully![/green]")
        except:
            self.console.print("[red]An error occurred while saving the credentials! Please open an issue on GitHub.[/red]")

    def add_keywords(self):
        self.console.print(Panel("Add Keywords", title="Keywords", style="bold magenta"))
        
        manual_or_file = Prompt.ask("Would you like to enter keywords manually or from a file?", choices=["manual", "file"], default="manual")
        
        if manual_or_file == "manual":
            while True:
                keyword = Prompt.ask("Enter a keyword (or type 'exit' to finish)", default="")
                if keyword.lower() == "exit":
                    break
                elif keyword.strip() == "":
                    self.console.print("[red]Keyword cannot be empty![/red]")
                else:
                    self.keywords.append(keyword.strip())
                    self.console.print(f"[green]Added keyword: {keyword.strip()}[/green]")
        elif manual_or_file == "file":
            file_path = Prompt.ask("Please enter the path to your keywords file (e.g., keywords.txt)", default="keywords.txt")
            try:
                with open(file_path, 'r') as file:
                    loaded_keywords = [line.strip() for line in file if line.strip()]
                self.keywords.extend(loaded_keywords)
                self.console.print(f"[green]Successfully loaded {len(loaded_keywords)} keywords from file.[/green]")
            except FileNotFoundError:
                self.console.print("[red]File not found! Please make sure the file exists.[/red]")
            except:
                self.console.print("[red]An error occurred while loading the keywords! Please open an issue on GitHub.[/red]")
                
        try:
            self.settings.insert_keywords(keywords=self.keywords)
            self.console.print("[green]Keywords saved successfully![/green]")
        except:
            self.console.print("[red]An error occurred while saving the keywords! Please open an issue on GitHub.[/red]")

    def generate_stats_layout(self):
        table = Table(title="Bot Statistics")
        table.add_column("Metric", style="dim", width=20)
        table.add_column("Value", style="bold")
        table.add_row("Total Keywords Processed", str(self.total_created))
        table.add_row("Sleep Time", f"{self.sleep_time} seconds")
        table.add_row("Google Trends", f"{self.trends}")
        table.add_row("Article Title", f"{self.title}")
        return table

    def run_bot(self):
        if not all([self.openai_api_key, self.username, self.password, self.wordress_api_url, self.sleep_time, self.max_length, self.model]):
            self.console.print("[red]Please complete the setup before running the bot.[/red]")
            return
        
        if not self.settings.get_all_data("keywords")[0].keyword:
            self.console.print("[red]Please add keywords before running the bot.[/red]")
            return

        self.running = True
        self.console.print("[yellow]Bot is starting...[/yellow]")
        sleep(1)

        layout = Layout()
        layout.split_column(
            Layout(name="stats", size=10),
            Layout(name="footer", size=3)
        )
        layout["footer"].update(Panel("Press Ctrl+C to stop the bot.", style="bold blue"))
        bot = StartBot(api_key=self.openai_api_key, model_engine=self.model)
        bot.crawl()
        try:
            with Live(layout, refresh_per_second=1, console=self.console):
                keywords = self.settings.get_all_data("suggestions")
                for keyword_data in keywords:
                    if not self.running:
                        self.console.print("\n[red]Bot has been stopped by the user.[/red]")
                        break
                    keyword = keyword_data.suggestion
                    self.title = bot.generate_title(keyword)
                    self.total_created += 1
                    self.keyword = keyword
                    self.trends = keyword
                    bot.post(keyword, self.title)
                    layout["stats"].update(self.generate_stats_layout())
                    sleep(float(self.sleep_time))
            self.console.print("[green]Bot has finished processing all keywords.[/green]")
        except KeyboardInterrupt:
            self.console.print("\n[red]Bot has been stopped by the user.[/red]")
            self.running = False
            
    def fetch_data_from_database(self):
        data = self.settings.get_all_data("settings")
        if self.settings.get_all_data("keywords"):
            self.keywords_exists = True
        if not data:
            self.data_exists = False
            return
        self.openai_api_key = data[0].api_key if data[0].api_key else None
        self.username = data[0].wp_username if data[0].wp_username else None
        self.password = data[0].wp_password if data[0].wp_password else None
        self.wordress_api_url = data[0].wp_api_url if data[0].wp_api_url else None
        self.sleep_time = data[0].sleep_time if data[0].sleep_time else None
        self.max_length = data[0].max_length if data[0].max_length else None
        self.model = data[0].ai_model if data[0].ai_model else None

    def main_menu(self):
        while True:
            self.fetch_data_from_database()
            self.display_main_menu()
            action = Prompt.ask("Choose an action", choices=["1", "2", "3", "4"], default="1")
            
            if action == "1":
                self.setup()
            elif action == "2":
                self.add_keywords()
            elif action == "3":
                self.run_bot()
            elif action == "4":
                self.console.print("[green]Exiting...[/green]")
                sys.exit()

if __name__ == "__main__":
    bot = CLIG()
    bot.main_menu()
