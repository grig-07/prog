# cli.py 
 
import typer 
from my_package import module_lab7, module_lab8, module_lab9 
 
app = typer.Typer() 
 
@app.command() 
def process(file_path: str): 
    Обработка файла. 
    data = module_lab7.process_file(file_path) 
    typer.echo(f"Data from file: {data}") 
