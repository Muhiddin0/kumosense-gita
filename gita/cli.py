import click

@click.group()
def cli():
    """Gita - AI yordamida avtomatik commit yozish CLI"""
    pass

@click.command()
@click.option('--push', is_flag=True, help="Commitdan keyin avtomatik push qilish")
def commit(push):
    """AI tomonidan avtomatik commit yozish"""
    # AI Model API chaqirish logikasi
    commit_message = "AI yozgan commit xabari"  # Bu yerga haqiqiy AI model kodini qo‘shish kerak

    # Git commit
    import subprocess
    subprocess.run(["git", "commit", "-m", commit_message])

    if push:
        subprocess.run(["git", "push"])

    click.echo(f"✅ Commit bajarildi: {commit_message}")

cli.add_command(commit)

if __name__ == "__main__":
    cli()

